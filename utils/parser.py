from dataclasses import dataclass
from typing import Dict, List, Type, Union, Tuple
from collections import defaultdict

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from base.skill import Skill
from schools import bei_ao_jue
from utils.lua import parse


@dataclass
class School:
    school: str
    major: str
    kind: str
    attribute: Type[Attribute]
    formation: str
    skills: Dict[int, Skill]
    buffs: Dict[int, Buff]
    talent_gains: Dict[int, Gain]
    talents: List[List[int]]
    talent_decoder: Dict[int, str]
    talent_encoder: Dict[str, int]
    recipe_gains: Dict[str, Dict[str, Gain]]
    recipes: Dict[str, List[str]]
    gains: Dict[Union[Tuple[int, int], int], Gain]
    display_attrs: Dict[str, str]

    def attr_content(self, attribute):
        content = []
        for attr, name in self.display_attrs.items():
            value = getattr(attribute, attr)
            if isinstance(value, int):
                content.append([name, f"{value}"])
            else:
                content.append([name, f"{round(value * 100, 2)}%"])
        return content


SUPPORT_SCHOOL = {
    10464: School(
        school="霸刀",
        major="力道",
        kind="外功",
        attribute=bei_ao_jue.BeiAoJue,
        formation="霜岚洗锋阵",
        skills=bei_ao_jue.SKILLS,
        buffs=bei_ao_jue.BUFFS,
        talent_gains=bei_ao_jue.TALENT_GAINS,
        talents=bei_ao_jue.TALENTS,
        talent_decoder=bei_ao_jue.TALENT_DECODER,
        talent_encoder=bei_ao_jue.TALENT_ENCODER,
        recipe_gains=bei_ao_jue.RECIPE_GAINS,
        recipes=bei_ao_jue.RECIPES,
        gains=bei_ao_jue.GAINS,
        display_attrs={
            "strength": "力道",
            "base_physical_attack_power": "基础攻击",
            "physical_attack_power": "攻击",
            "base_physical_critical_strike": "会心等级",
            "physical_critical_strike": "会心",
            "physical_critical_power_base": "会效等级",
            "physical_critical_power": "会效",
            "base_physical_overcome": "基础破防",
            "final_physical_overcome": "最终破防",
            "physical_overcome": "破防",
            "weapon_damage_base": "基础武器伤害",
            "weapon_damage_rand": "浮动武器伤害",
            "strain_base": "无双等级",
            "strain": "无双",
            "surplus": "破招",
        }
    )
}


class Parser:
    records: list
    status: dict
    snapshot: dict
    stacks: dict
    ticks: dict

    start_time: list
    end_time: list
    record_index: Dict[str, int]

    fight_flag: bool

    select_talents: List[int]

    school: School | None

    def duration(self, i):
        return round((self.end_time[i] - self.start_time[i]) / 1000, 3)

    @property
    def current_record(self):
        return self.records[len(self.start_time) - 1]

    def available_status(self, skill_id):
        current_status = []
        for (buff_id, buff_level), buff_stack in self.status.items():
            buff = self.school.buffs[buff_id]
            if buff.gain_attributes:
                current_status.append((buff_id, buff_level, buff_stack))
            elif buff.gain_skills and skill_id in buff.gain_skills:
                current_status.append((buff_id, buff_level, buff_stack))

        snapshot_status = []
        for (buff_id, buff_level), buff_stack in self.snapshot.get(skill_id, {}).items():
            buff = self.school.buffs[buff_id]
            if buff.gain_attributes:
                snapshot_status.append((buff_id, buff_level, buff_stack))
            elif buff.gain_skills and skill_id in buff.gain_skills:
                snapshot_status.append((buff_id, buff_level, buff_stack))

        return tuple(current_status), tuple(snapshot_status)

    def reset(self):
        self.fight_flag = False

        self.records = []
        self.status = {}
        self.snapshot = {}
        self.stacks = defaultdict(int)
        self.ticks = defaultdict(int)

        self.start_time = []
        self.end_time = []

        self.record_index = {}

        self.school = None

    def parse_info(self, detail):
        if isinstance(detail, list):
            self.school = SUPPORT_SCHOOL.get(detail[3])
            if not self.school:
                raise AttributeError(f"Cannot support {detail[3]} now")
            self.select_talents = [row[1] for row in detail[6]]
            return self.school

    def parse_time(self, detail, timestamp):
        if detail[1]:
            self.start_time.append(int(timestamp))
            self.records.append({})
            self.fight_flag = True
        else:
            self.end_time.append(int(timestamp))
            self.fight_flag = False

    def parse_buff(self, row):
        detail = row.split(",")
        buff_id, buff_stack, buff_level = int(detail[4]), int(detail[5]), int(detail[8])
        if buff_id not in self.school.buffs:
            return
        if not buff_stack:
            self.status.pop((buff_id, buff_level))
        else:
            self.status[(buff_id, buff_level)] = buff_stack

    def parse_skill(self, row, timestamp):
        detail = row.split(",")
        skill_id, skill_level, critical = int(detail[4]), int(detail[5]), detail[6] == "true"
        if skill_id not in self.school.skills:
            return
        timestamp = int(timestamp) - self.start_time[-1]
        skill_stack = max(1, self.stacks[skill_id])
        if self.ticks[skill_id]:
            self.ticks[skill_id] -= 1
            if not self.ticks[skill_id]:
                self.stacks[skill_id] = 0

        skill_tuple = (skill_id, skill_level, skill_stack)
        skill = self.school.skills[skill_id]
        if bind_skill := skill.bind_skill:
            self.stacks[bind_skill] = min(self.stacks[bind_skill] + 1, skill.max_stack)
            self.ticks[bind_skill] = skill.tick if not self.ticks[bind_skill] else skill.tick - 1
            self.snapshot[bind_skill] = self.status.copy()
        else:
            if skill_tuple not in self.current_record:
                self.current_record[skill_tuple] = {}
            status_tuple = self.available_status(skill_id)
            if status_tuple not in self.current_record[skill_tuple]:
                self.current_record[skill_tuple][status_tuple] = []
            self.current_record[skill_tuple][status_tuple].append((timestamp, critical))

    def __call__(self, file_name):
        self.reset()
        lines = open(file_name).readlines()
        for line in lines:
            row = line.split("\t")
            if row[4] == "4" and self.parse_info(parse(row[-1])):
                break

        for line in lines:
            row = line.split("\t")
            if row[4] == "5":
                self.parse_time(parse(row[-1]), row[3])
            elif row[4] == "13":
                self.parse_buff(row[-1])
            elif row[4] == "21" and self.fight_flag:
                self.parse_skill(row[-1], row[3])

        self.record_index = {
            f"{i + 1}:{round((end_time - self.start_time[i]) / 1000, 3)}": i for i, end_time in enumerate(self.end_time)
        }
