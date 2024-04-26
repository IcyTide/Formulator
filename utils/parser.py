from dataclasses import dataclass
from typing import Dict, List, Type, Union, Tuple
from collections import defaultdict

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from base.skill import Skill, DotSkill, DotConsumeSkill, Damage, DotDamage
from schools import bei_ao_jue, shan_hai_xin_jue, ling_hai_jue
from utils.lua import parse

SKILL_TYPE = Tuple[int, int, int]
BUFF_TYPE = Tuple[int, int, int]
TIMELINE_TYPE = List[Tuple[int, bool]]
SUB_RECORD_TYPE = Dict[Tuple[tuple, tuple], TIMELINE_TYPE]
RECORD_TYPE = Dict[SKILL_TYPE, SUB_RECORD_TYPE]
STATUS_TYPE = Dict[Tuple[int, int], int]
SNAPSHOT_TYPE = Dict[int, STATUS_TYPE]


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


PHYSICAL_DISPLAY_ATTRS = {
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

SUPPORT_SCHOOL = {
    10464: School(
        school="霸刀", major="力道", kind="外功", attribute=bei_ao_jue.BeiAoJue, formation="霜岚洗锋阵",
        skills=bei_ao_jue.SKILLS, buffs=bei_ao_jue.BUFFS,
        talent_gains=bei_ao_jue.TALENT_GAINS, talents=bei_ao_jue.TALENTS,
        talent_decoder=bei_ao_jue.TALENT_DECODER, talent_encoder=bei_ao_jue.TALENT_ENCODER,
        recipe_gains=bei_ao_jue.RECIPE_GAINS, recipes=bei_ao_jue.RECIPES,
        gains=bei_ao_jue.GAINS, display_attrs={"strength": "力道", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10756: School(
        school="万灵", major="身法", kind="外功", attribute=shan_hai_xin_jue.ShanHaiXinJue, formation="苍梧引灵阵",
        skills=shan_hai_xin_jue.SKILLS, buffs=shan_hai_xin_jue.BUFFS,
        talent_gains=shan_hai_xin_jue.TALENT_GAINS, talents=shan_hai_xin_jue.TALENTS,
        talent_decoder=shan_hai_xin_jue.TALENT_DECODER, talent_encoder=shan_hai_xin_jue.TALENT_ENCODER,
        recipe_gains=shan_hai_xin_jue.RECIPE_GAINS, recipes=shan_hai_xin_jue.RECIPES,
        gains=shan_hai_xin_jue.GAINS, display_attrs={"agility": "身法", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10533: School(
        school="蓬莱", major="身法", kind="外功", attribute=ling_hai_jue.LingHaiJue, formation="墟海引归阵",
        skills=ling_hai_jue.SKILLS, buffs=ling_hai_jue.BUFFS,
        talent_gains=ling_hai_jue.TALENT_GAINS, talents=ling_hai_jue.TALENTS,
        talent_decoder=ling_hai_jue.TALENT_DECODER, talent_encoder=ling_hai_jue.TALENT_ENCODER,
        recipe_gains=ling_hai_jue.RECIPE_GAINS, recipes=ling_hai_jue.RECIPES,
        gains=ling_hai_jue.GAINS, display_attrs={"agility": "身法", **PHYSICAL_DISPLAY_ATTRS}
    ),
}

LABEL_MAPPING = {
    2: "远程武器",
    3: "上衣",
    4: "帽子",
    5: "项链",
    6: "戒指1",
    7: "戒指2",
    8: "腰带",
    9: "腰坠",
    10: "下装",
    11: "鞋子",
    12: "护腕",
    0: "近战武器"
}
EMBED_MAPPING = {(5, 24449 - i): 8 - i for i in range(8)}


class Parser:
    current_player: int
    id2name: Dict[int, str]
    name2id: Dict[str, int]
    records: Dict[int, List[RECORD_TYPE]]
    status: Dict[int, STATUS_TYPE]
    snapshot: Dict[int, SNAPSHOT_TYPE]
    last_dot: Dict[int, Dict[int, Tuple[Tuple[int, int, int], Tuple[tuple, tuple]]]]
    stacks: Dict[int, Dict[int, int]]
    ticks: Dict[int, Dict[int, int]]
    pets: Dict[int, int]

    start_time: Dict[int, List[int]]
    end_time: Dict[int, List[int]]
    record_index: Dict[int, Dict[str, int]]

    select_talents: Dict[int, List[int]]
    select_equipments: Dict[int, Dict[int, Dict[str, int | list]]]

    school: Dict[int, School]

    def duration(self, player_id, i):
        return round((self.end_time[player_id][i] - self.start_time[player_id][i]) / 1000, 3)

    def available_status(self, player_id, skill_id):
        current_status = []
        for (buff_id, buff_level), buff_stack in self.status[player_id].items():
            buff = self.school[player_id].buffs[buff_id]
            if buff.gain_attributes:
                current_status.append((buff_id, buff_level, buff_stack))
            elif buff.gain_skills and skill_id in buff.gain_skills:
                current_status.append((buff_id, buff_level, buff_stack))

        snapshot_status = []
        for (buff_id, buff_level), buff_stack in self.snapshot[player_id].get(skill_id, {}).items():
            buff = self.school[player_id].buffs[buff_id]
            if buff.gain_attributes:
                snapshot_status.append((buff_id, buff_level, buff_stack))
            elif buff.gain_skills and skill_id in buff.gain_skills:
                snapshot_status.append((buff_id, buff_level, buff_stack))

        return tuple(current_status), tuple(snapshot_status)

    def reset(self):
        self.id2name = {}
        self.name2id = {}
        self.records = defaultdict(list)
        self.status = defaultdict(dict)
        self.snapshot = defaultdict(dict)
        self.last_dot = defaultdict(dict)
        self.stacks = defaultdict(lambda: defaultdict(lambda: 1))
        self.ticks = defaultdict(lambda: defaultdict(int))
        self.pets = {}

        self.start_time = defaultdict(list)
        self.end_time = defaultdict(list)

        self.select_talents = {}
        self.select_equipments = {}
        self.school = {}

    @staticmethod
    def parse_equipments(detail):
        select_equipments = {}
        for row in detail:
            if not (label := LABEL_MAPPING.get(row[0])):
                continue
            select_equipment = select_equipments[label] = {}
            select_equipment['equipment'] = row[2]
            select_equipment['strength_level'] = row[3]
            if isinstance(row[4], list):
                select_equipment['embed_levels'] = [EMBED_MAPPING.get(tuple(e), 0) for e in row[4]]
            else:
                select_equipment['embed_levels'] = []
            select_equipment['enchant'] = row[5]
        return select_equipments

    @staticmethod
    def parse_talents(detail):
        return [row[1] for row in detail]

    def parse_info(self, row):
        detail = row.strip("{}").split(",")
        player_id, school_id = int(detail[0]), int(detail[3])
        if player_id in self.id2name or school_id not in SUPPORT_SCHOOL:
            return
        if isinstance(detail := parse(row), list):
            player_name = detail[1]
            self.id2name[player_id] = player_name
            self.name2id[player_name] = player_id
            if school := SUPPORT_SCHOOL.get(detail[3]):
                self.school[player_id] = school
                self.select_equipments[player_id] = self.parse_equipments(detail[5])
                self.select_talents[player_id] = self.parse_talents(detail[6])

    def parse_pet(self, row):
        detail = row.strip("{}").split(",")
        pet_id, player_id = int(detail[0]), int(detail[3])
        if player_id in self.school:
            self.pets[pet_id] = player_id

    def parse_time(self, row, timestamp):
        detail = row.strip("{}").split(",")
        player_id = int(detail[0])
        if player_id not in self.school:
            return
        if detail[1] == "true" and len(self.start_time[player_id]) == len(self.end_time[player_id]):
            self.start_time[player_id].append(int(timestamp))
            self.records[player_id].append(defaultdict(lambda: defaultdict(list)))
        elif detail[1] == "false" and len(self.start_time[player_id]) - len(self.end_time[player_id]) == 1:
            self.end_time[player_id].append(int(timestamp))

    def parse_buff(self, row):
        detail = row.strip("{}").split(",")
        player_id = int(detail[0])
        if player_id not in self.school:
            return
        buff_id, buff_stack, buff_level = int(detail[4]), int(detail[5]), int(detail[8])
        if buff_id not in self.school[player_id].buffs:
            return
        if not buff_stack:
            self.status[player_id].pop((buff_id, buff_level), None)
        else:
            self.status[player_id][(buff_id, buff_level)] = buff_stack

    def parse_skill(self, row, timestamp):
        detail = row.strip("{}").split(",")
        caster_id = int(detail[0])
        if caster_id in self.pets:
            player_id = self.pets[caster_id]
        else:
            player_id = caster_id

        if player_id not in self.school:
            return
        react, skill_id, skill_level, critical = int(detail[2]), int(detail[4]), int(detail[5]), detail[6] == "true"
        if react or skill_id not in self.school[player_id].skills:
            return
        if len(self.start_time[player_id]) == len(self.end_time[player_id]):
            self.start_time[player_id].append(int(timestamp))
            self.records[player_id].append(defaultdict(lambda: defaultdict(list)))
        timestamp = int(timestamp) - self.start_time[player_id][-1]
        skill_stack = self.stacks[player_id][skill_id]

        skill = self.school[player_id].skills[skill_id]
        if isinstance(skill, DotSkill):
            bind_skill = skill.bind_skill
            if not self.ticks[player_id][bind_skill]:
                self.stacks[player_id][bind_skill] = 0
            self.ticks[player_id][bind_skill] = skill.tick
            self.stacks[player_id][bind_skill] = min(self.stacks[player_id][bind_skill] + 1, skill.max_stack)
            self.snapshot[player_id][bind_skill] = self.status[player_id].copy()
        elif isinstance(skill, DotConsumeSkill):
            bind_skill = skill.bind_skill
            skill_tuple, status_tuple = self.last_dot[player_id][bind_skill]
            skill_id, skill_level, skill_stack = skill_tuple
            self.ticks[player_id][skill_id] += 1
            tick = min(self.ticks[player_id][skill_id], skill.tick)
            current_record = self.records[player_id][-1]
            current_record[(skill_id, skill_level, skill_stack * tick)][status_tuple].append(
                current_record[skill_tuple][status_tuple].pop()
            )
            self.ticks[player_id][skill_id] -= tick
        elif isinstance(skill, Damage):
            skill_tuple = (skill_id, skill_level, skill_stack)
            status_tuple = self.available_status(player_id, skill_id)
            current_record = self.records[player_id][-1]
            current_record[skill_tuple][status_tuple].append((timestamp, critical))
            if isinstance(skill, DotDamage):
                self.last_dot[player_id][skill_id] = (skill_tuple, status_tuple)
                self.ticks[player_id][skill_id] -= 1

    def __call__(self, file_name):
        self.reset()
        lines = open(file_name).readlines()
        for line in lines:
            row = line.split("\t")
            if row[4] == "4":
                self.parse_info(row[-1])

        for player_id, school in self.school.items():
            for talent_id in self.select_talents[player_id]:
                school.talent_gains[talent_id].add_skills(school.skills)

        for line in lines:
            row = line.split("\t")
            if row[4] == "5":
                self.parse_time(row[-1], row[3])
            if row[4] == "8":
                self.parse_pet(row[-1])
            elif row[4] == "13":
                self.parse_buff(row[-1])
            elif row[4] == "21":
                self.parse_skill(row[-1], row[3])

        for player_id, school in self.school.items():
            for talent_id in self.select_talents[player_id]:
                school.talent_gains[talent_id].sub_skills(school.skills)

        self.record_index = {
            player_id: {
                f"{i + 1}:{round((end_time - self.start_time[player_id][i]) / 1000, 3)}": i
                for i, end_time in enumerate(self.end_time[player_id])
            }
            for player_id in self.end_time
        }
