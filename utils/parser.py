import os
import time
from collections import defaultdict

import pandas as pd
from line_profiler import profile

from base.constant import FRAME_PER_SECOND
from schools import *
from utils.lua import parse_player, parse_damage

FRAME_TYPE, INDEX_TYPE = int, int
PLAYER_ID_TYPE, TARGET_ID_TYPE, PET_ID_TYPE = str, str, str
CASTER_ID_TYPE = PLAYER_ID_TYPE | PET_ID_TYPE
ENTITY_ID_TYPE, ENTITY_NAME_TYPE = CASTER_ID_TYPE | TARGET_ID_TYPE, str
SKILL_ID_TYPE, SKILL_LEVEL_TYPE, SKILL_STACK_TYPE = int, int, int
ACTUAL_DAMAGE, ACTUAL_CRITICAL_STRIKE = int, bool
SKILL_TYPE = Tuple[SKILL_ID_TYPE, SKILL_LEVEL_TYPE, SKILL_STACK_TYPE]
BUFF_ID_TYPE, BUFF_LEVEL_TYPE, BUFF_STACK_TYPE = int, int, int
BUFF_TYPE = Tuple[BUFF_ID_TYPE, BUFF_LEVEL_TYPE]

TAG_COLUMNS = ["frame", "time", "player_id", "caster_id", "target_id", "skill", "skill_name"]
CALCULATE_COLUMNS = ["skill_id", "skill_level", "skill_stack", "current_status", "target_status", "snapshot_index"]
COMPARE_COLUMNS = ["actual_critical_strike", "actual_damage"]
COLUMNS = TAG_COLUMNS + CALCULATE_COLUMNS + COMPARE_COLUMNS

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
EMBED_MAPPING: Dict[tuple, int] = {(5, 24449 - i): 8 - i for i in range(8)}


class BaseParser:
    current_player: PLAYER_ID_TYPE
    current_caster: CASTER_ID_TYPE
    current_target: TARGET_ID_TYPE
    current_skill: SKILL_ID_TYPE

    current_frame: FRAME_TYPE
    current_index: INDEX_TYPE

    id2name: Dict[ENTITY_ID_TYPE, ENTITY_NAME_TYPE]
    name2id: Dict[ENTITY_NAME_TYPE, ENTITY_ID_TYPE]
    pet2employer: Dict[PET_ID_TYPE, PLAYER_ID_TYPE]

    records: Dict[PLAYER_ID_TYPE, List[dict] | pd.DataFrame]

    skill_display_names: Dict[tuple, str]
    buff_display_names: Dict[tuple, str]

    buffs: Dict[CASTER_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]
    buff_intervals: Dict[CASTER_ID_TYPE, Dict[BUFF_TYPE, FRAME_TYPE]]
    target_buffs: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]]
    target_buff_intervals: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_TYPE, FRAME_TYPE]]]

    dot_stacks: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, int]]]
    dot_ticks: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, int]]]
    dot_buffs: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, INDEX_TYPE]]]

    next_pet_buffs: Dict[PLAYER_ID_TYPE, List[Dict[BUFF_TYPE, BUFF_STACK_TYPE]]]

    last_dot: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, INDEX_TYPE]]]
    next_dot: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, int]]]

    start_frame: FRAME_TYPE
    end_frame: FRAME_TYPE

    select_talents: Dict[PLAYER_ID_TYPE, List[int]]
    select_equipments: Dict[PLAYER_ID_TYPE, Dict[int, Dict[str, int | list]]]

    players: Dict[PLAYER_ID_TYPE, School]
    targets: Dict[PLAYER_ID_TYPE, List[TARGET_ID_TYPE]]

    @property
    def current_school(self):
        return self.players[self.current_player]

    @property
    def current_targets(self):
        return self.targets[self.current_player]

    @property
    def current_records(self):
        return self.records[self.current_player]

    @property
    def current_record(self):
        return self.current_records[-1]

    @property
    def current_buffs(self):
        return self.buffs[self.current_caster]

    @property
    def current_buff_intervals(self):
        return self.buff_intervals[self.current_player]

    @property
    def current_target_buffs(self):
        return self.target_buffs[self.current_target][self.current_player]

    @property
    def current_target_buff_intervals(self):
        return self.target_buff_intervals[self.current_target][self.current_player]

    @property
    def current_next_pet_buffs(self):
        return self.next_pet_buffs[self.current_player]

    @property
    def current_dot_buffs(self):
        return self.dot_buffs[self.current_target][self.current_player]

    @property
    def current_dot_stacks(self):
        return self.dot_stacks[self.current_target][self.current_player]

    @property
    def current_dot_ticks(self):
        return self.dot_ticks[self.current_target][self.current_player]

    @property
    def current_last_dot(self):
        return self.last_dot[self.current_target][self.current_player]

    @property
    def current_next_dot(self):
        return self.next_dot[self.current_target][self.current_player]

    def reset(self):
        self.current_frame = 0
        self.current_index = 0

        self.id2name = {}
        self.name2id = {}
        self.pet2employer = {}

        self.records = defaultdict(list)

        self.buff_display_names = {}
        self.buffs = defaultdict(dict)
        self.buff_intervals = defaultdict(dict)
        self.target_buffs = defaultdict(lambda: defaultdict(dict))
        self.target_buff_intervals = defaultdict(lambda: defaultdict(dict))

        self.dot_stacks = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 1)))
        self.dot_ticks = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0)))

        self.next_pet_buffs = defaultdict(list)
        self.dot_buffs = defaultdict(lambda: defaultdict(dict))
        self.last_dot = defaultdict(lambda: defaultdict(dict))
        self.next_dot = defaultdict(lambda: defaultdict(dict))

        self.start_frame = 0

        self.select_talents = {}
        self.select_equipments = {}

        self.players = {}
        self.targets = defaultdict(list)

    def refresh_buff(self, buff_id, buff_level, buff_stack=1):
        buff = self.current_school.buffs[buff_id]
        buff_tuple = (buff_id, buff_level)
        stack = max(min(self.current_buffs.get(buff_tuple, 0) + buff_stack, buff.max_stack), 0)
        if stack:
            self.current_buffs[buff_tuple] = stack
            if buff.interval > 0:
                self.current_buff_intervals[buff_tuple] = self.current_frame + buff.interval + 1
        else:
            self.current_buffs.pop(buff_tuple, None)
            self.current_buff_intervals.pop(buff_tuple, None)

    def refresh_target_buff(self, buff_id, buff_level, buff_stack=1):
        buff = self.current_school.buffs[buff_id]
        buff_tuple = (buff_id, buff_level)
        stack = max(min(self.current_target_buffs.get(buff_tuple, 0) + buff_stack, buff.max_stack), 0)
        if stack:
            self.current_target_buffs[buff_tuple] = stack
            if buff.interval > 0:
                self.current_target_buff_intervals[buff_tuple] = self.current_frame + buff.interval + 1
        else:
            self.current_target_buffs.pop(buff_tuple, None)
            self.current_target_buff_intervals.pop(buff_tuple, None)

    def clear_buff(self, buff_id, buff_level):
        buff_tuple = (buff_id, buff_level)
        self.current_buffs.pop(buff_tuple, None)
        self.current_buff_intervals.pop(buff_tuple, None)

    def clear_target_buff(self, buff_id, buff_level):
        buff_tuple = (buff_id, buff_level)
        self.current_target_buffs.pop(buff_tuple, None)
        self.current_target_buff_intervals.pop(buff_tuple, None)

    def buff_timer(self):
        for caster_id, buffs in self.buff_intervals.items():
            pop_buffs = []
            for buff, end_frame in buffs.items():
                if end_frame < self.current_frame:
                    self.buffs[caster_id].pop(buff, None)
                    pop_buffs.append(buff)
            for pop_buff in pop_buffs:
                buffs.pop(pop_buff)
        for target_id in self.target_buff_intervals:
            for caster_id, buffs in self.target_buff_intervals[target_id].items():
                pop_buffs = []
                for buff, end_frame in buffs.items():
                    if end_frame < self.current_frame:
                        self.target_buffs[target_id][caster_id].pop(buff, None)
                        pop_buffs.append(buff)
                for pop_buff in pop_buffs:
                    buffs.pop(pop_buff)


class Parser(BaseParser):
    @property
    def duration(self):
        return round((self.end_frame - self.start_frame) / FRAME_PER_SECOND, 2)

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

    def parse_player(self, row):
        detail = row.strip("{}").split(",")
        player_id, school_id = detail[0], int(detail[3])
        if player_id in self.id2name or school_id not in SUPPORT_SCHOOL:
            return

        if detail := parse_player(row):
            player_name = detail[1]
            school = SUPPORT_SCHOOL[school_id]
            self.id2name[player_id] = player_name
            self.name2id[player_name] = player_id
            self.select_equipments[player_id] = self.parse_equipments(detail[5])
            self.select_talents[player_id] = self.parse_talents(detail[6])
            if any(talent not in school.talent_gains for talent in self.select_talents[player_id]):
                return
            self.players[player_id] = school

    def parse_npc(self, row):
        detail = row.strip("{}").split(",")
        npc_id, npc_name, employer_id = detail[0], detail[1].strip('"'), detail[3]
        if npc_id in self.id2name or not npc_name:
            return

        self.id2name[npc_id] = npc_name
        self.name2id[npc_name] = npc_id
        if employer_id in self.players:
            self.pet2employer[npc_id] = employer_id

    def parse_pet(self, row):
        pet_id = row.strip("{}")
        if player_id := self.pet2employer.get(pet_id):
            if self.next_pet_buffs[player_id]:
                pet_buff_stacks = self.next_pet_buffs[player_id].pop()
            else:
                pet_buff_stacks = {}
            self.buffs[pet_id] = {**self.buffs[player_id].copy(), **pet_buff_stacks}

    def parse_buff(self, row):
        detail = row.strip("{}").split(",")
        caster_id = detail[0]
        if caster_id in self.pet2employer:
            player_id = self.pet2employer[caster_id]
            if caster_id in self.buffs:
                buffs = self.buffs[caster_id]
            elif self.next_pet_buffs[player_id]:
                buffs = self.next_pet_buffs[player_id][0]
            else:
                buffs = {}
                self.next_pet_buffs[player_id].append(buffs)
        else:
            player_id = caster_id
            buffs = self.buffs[player_id]

        if player_id not in self.players:
            return

        buff_id, buff_stack, buff_level = int(detail[4]), int(detail[5]), int(detail[8])
        if buff_id not in self.players[player_id].buffs:
            return

        if buff_stack:
            buffs[(buff_id, buff_level)] = buff_stack
        else:
            buffs.pop((buff_id, buff_level), None)

    @profile
    def parse_skill(self, row):
        detail = row.strip("{}").split(",")
        caster_id, target_id = detail[0], detail[1]
        if caster_id in self.pet2employer:
            player_id = self.pet2employer[caster_id]
        else:
            player_id = caster_id

        if player_id not in self.players:
            return

        react, skill_id, skill_level = int(detail[2]), int(detail[4]), int(detail[5])
        actual_critical_strike, actual_damage = detail[6] == "true", parse_damage(row)
        if react or skill_id not in self.players[player_id].skills:
            return

        if not self.start_frame:
            self.start_frame = self.current_frame

        self.current_player = player_id
        self.current_caster = caster_id
        if target_id in self.id2name and target_id not in self.current_targets:
            self.current_targets.append(target_id)
        self.current_target = target_id
        self.current_skill = skill_id

        skill = self.players[player_id].skills[skill_id]
        skill.skill_level = skill_level
        self.current_records.append({
            "frame": self.current_frame, **self.current_buffs, **self.current_target_buffs,
            "player_id": self.current_player, "caster_id": self.current_caster, "target_id": self.current_target,
            "skill_id": skill_id, "skill_level": skill_level, "skill_stack": 1, "skill_name": skill.skill_name,
            "actual_critical_strike": actual_critical_strike, "actual_damage": actual_damage,
           })
        self.set_status()
        skill.parse(self)
        self.current_index += 1

    @profile
    def set_status(self):
        current_status = []
        for (buff_id, buff_level), buff_stack in self.current_buffs.items():
            buff = self.current_school.buffs[buff_id]
            if buff.gain_attributes:
                current_status.append((buff_id, buff_level, buff_stack))
            elif buff.gain_skills and self.current_skill in buff.gain_skills:
                current_status.append((buff_id, buff_level, buff_stack))
        self.current_record['current_status'] = tuple(sorted(current_status))

        target_status = []
        for (buff_id, buff_level), buff_stack in self.current_target_buffs.items():
            buff = self.current_school.buffs[buff_id]
            if buff.gain_attributes:
                target_status.append((buff_id, buff_level, buff_stack))
            elif buff.gain_skills and self.current_skill in buff.gain_skills:
                target_status.append((buff_id, buff_level, buff_stack))
        self.current_record['target_status'] = tuple(sorted(target_status))

    def convert_records(self):
        for player_id, records in self.records.items():
            records = pd.DataFrame(records)
            records.snapshot_index = records.snapshot_index.fillna(-1)
            records = records.fillna(0)
            records['time'] = (records.frame - self.start_frame) / FRAME_PER_SECOND
            skills = [""] * len(records)
            for skill_tuple, indices in records.groupby(["skill_id", "skill_level", "skill_stack"]).indices.items():
                skill_id, skill_level, skill_stack = skill_tuple
                skill = self.players[player_id].skills[skill_id]
                skill.skill_level, skill.skill_stack = skill_level, skill_stack
                for index in indices:
                    skills[index] = skill.display_name
            records["skill"] = skills
            buffs = {}
            for buff_tuple in [column for column in records.columns if isinstance(column, tuple)]:
                buff_id, buff_level = buff_tuple
                buff = self.players[player_id].buffs[buff_id]
                buff.buff_level = buff_level
                buffs[buff_tuple] = buff.display_name
            records = records.rename(columns=buffs)
            columns = [c for c in COLUMNS if c in records.columns] + [c for c in records.columns if c not in COLUMNS]
            records = records[columns]
            self.records[player_id] = records

    @profile
    def __call__(self, file_name):
        self.file_name = os.path.basename(file_name)
        self.reset()
        lines = open(file_name, encoding="gbk").readlines()
        rows = []
        for line in lines:
            row = line.split("\t")
            rows.append(row)
            if row[4] == "4":
                self.parse_player(row[-1])
            elif row[4] == "8":
                self.parse_npc(row[-1])

        for player_id, school in self.players.items():
            school.prepare(self, player_id)
            for talent_id in self.select_talents[player_id]:
                school.talent_gains[talent_id].add_skills(school.skills)

        for row in rows:
            if (current_frame := int(row[1])) != self.current_frame:
                self.current_frame = current_frame
                self.buff_timer()

            if row[4] == "6":
                self.parse_pet(row[-1].strip())
            elif row[4] == "13":
                self.parse_buff(row[-1].strip())
            elif row[4] == "21":
                self.parse_skill(row[-1].strip())

        self.end_frame = self.current_frame

        for player_id, school in self.players.items():
            for talent_id in self.select_talents[player_id]:
                school.talent_gains[talent_id].sub_skills(school.skills)

        self.convert_records()
