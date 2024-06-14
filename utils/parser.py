from collections import defaultdict
from copy import deepcopy

from base.constant import FRAME_PER_SECOND
from schools import *
from utils.lua import parse

FRAME_TYPE, SECOND_TYPE = int, int
PLAYER_ID_TYPE, PLAYER_NAME_TYPE, TARGET_ID_TYPE, PET_ID_TYPE = str, str, str, str
CASTER_ID_TYPE = Union[PLAYER_ID_TYPE, PET_ID_TYPE]
SKILL_ID_TYPE, SKILL_LEVEL_TYPE, SKILL_CRITICAL_TYPE = int, int, bool
BUFF_ID_TYPE, BUFF_LEVEL_TYPE, BUFF_STACK_TYPE = int, int, int
DAMAGE_TYPE = Tuple[SKILL_ID_TYPE, SKILL_LEVEL_TYPE]
BUFF_TYPE = Tuple[BUFF_ID_TYPE, BUFF_LEVEL_TYPE]
DOT_DAMAGE_TYPE = Tuple[SKILL_ID_TYPE, SKILL_LEVEL_TYPE, BUFF_STACK_TYPE]
SKILL_TYPE = Tuple[DAMAGE_TYPE, DOT_DAMAGE_TYPE]

CURRENT_STATUS_TYPE, SNAPSHOT_STATUS_TYPE, TARGET_STATUS_TYPE = tuple, tuple, tuple
STATUS_TUPLE = Tuple[CURRENT_STATUS_TYPE, SNAPSHOT_STATUS_TYPE, TARGET_STATUS_TYPE]
TIMELINE_TYPE = Tuple[FRAME_TYPE, SKILL_CRITICAL_TYPE]
SUB_RECORD_TYPE = Dict[STATUS_TUPLE, List[TIMELINE_TYPE]]
RECORD_TYPE = Dict[SKILL_TYPE, SUB_RECORD_TYPE]

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
    current_second: SECOND_TYPE

    id2name: Dict[Union[CASTER_ID_TYPE, TARGET_ID_TYPE], PLAYER_NAME_TYPE]
    name2id: Dict[PLAYER_NAME_TYPE, Union[CASTER_ID_TYPE, TARGET_ID_TYPE]]
    pet2employer: Dict[PET_ID_TYPE, PLAYER_ID_TYPE]

    records: Dict[PLAYER_ID_TYPE, Dict[TARGET_ID_TYPE, RECORD_TYPE]]

    frame_shift_buffs: Dict[FRAME_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]]
    second_shift_buffs: Dict[SECOND_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]]

    buff_stacks: Dict[CASTER_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]
    buff_intervals: Dict[CASTER_ID_TYPE, Dict[BUFF_TYPE, FRAME_TYPE]]
    target_buff_stacks: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]]
    target_buff_intervals: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_TYPE, FRAME_TYPE]]]

    dot_stacks: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, int]]]
    dot_ticks: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, int]]]
    dot_skills: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, DAMAGE_TYPE]]]

    dot_snapshot: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]]]
    pet_snapshot: Dict[PET_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]

    next_pet_buff_stacks: Dict[PLAYER_ID_TYPE, List[Dict[BUFF_TYPE, BUFF_STACK_TYPE]]]

    last_dot: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, Tuple[SKILL_TYPE, Tuple[tuple, tuple]]]]]

    start_frame: FRAME_TYPE
    end_frame: FRAME_TYPE

    select_talents: Dict[PLAYER_ID_TYPE, List[int]]
    select_equipments: Dict[PLAYER_ID_TYPE, Dict[int, Dict[str, Union[int, list]]]]

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
        return self.records[self.current_player][self.current_target]

    @property
    def current_buff_stacks(self):
        if self.current_caster in self.pet2employer:
            return self.buff_stacks[self.current_caster]
        else:
            return self.buff_stacks[self.current_player]

    @property
    def current_buff_intervals(self):
        return self.buff_intervals[self.current_player]

    @property
    def current_target_buff_stacks(self):
        return self.target_buff_stacks[self.current_target][self.current_player]

    @property
    def current_target_buff_intervals(self):
        return self.target_buff_intervals[self.current_target][self.current_player]

    @property
    def current_snapshot(self):
        if self.current_caster in self.pet2employer:
            return self.current_pet_snapshot
        else:
            return self.current_dot_snapshot.get(self.current_skill, {})

    @property
    def current_next_pet_buff_stacks(self):
        return self.next_pet_buff_stacks[self.current_player]

    @property
    def current_pet_snapshot(self):
        return self.pet_snapshot[self.current_caster]

    @property
    def current_dot_snapshot(self):
        return self.dot_snapshot[self.current_target][self.current_player]

    @property
    def current_dot_stacks(self):
        return self.dot_stacks[self.current_target][self.current_player]

    @property
    def current_dot_ticks(self):
        return self.dot_ticks[self.current_target][self.current_player]

    @property
    def current_dot_skills(self):
        return self.dot_skills[self.current_target][self.current_player]

    @property
    def current_last_dot(self):
        return self.last_dot[self.current_target][self.current_player]

    def reset(self):
        self.current_frame = 0
        self.current_second = 0

        self.id2name = {}
        self.name2id = {}
        self.pet2employer = {}

        self.records = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))

        self.frame_shift_buffs = defaultdict(lambda: defaultdict(dict))
        self.second_shift_buffs = defaultdict(lambda: defaultdict(dict))

        self.buff_stacks = defaultdict(dict)
        self.buff_intervals = defaultdict(dict)
        self.target_buff_stacks = defaultdict(lambda: defaultdict(dict))
        self.target_buff_intervals = defaultdict(lambda: defaultdict(dict))

        self.dot_stacks = defaultdict(lambda: defaultdict(dict))
        self.dot_ticks = defaultdict(lambda: defaultdict(dict))
        self.dot_skills = defaultdict(lambda: defaultdict(dict))

        self.next_pet_buff_stacks = defaultdict(list)
        self.dot_snapshot = defaultdict(lambda: defaultdict(dict))
        self.pet_snapshot = defaultdict(dict)
        self.last_dot = defaultdict(lambda: defaultdict(dict))

        self.start_frame = 0

        self.select_talents = {}
        self.select_equipments = {}

        self.players = {}
        self.targets = defaultdict(list)

    def refresh_buff(self, buff_id, buff_level, buff_stack=1):
        buff = self.current_school.buffs[buff_id]
        buff_tuple = (buff_id, buff_level)
        stack = max(min(self.current_buff_stacks.get(buff_tuple, 0) + buff_stack, buff.max_stack), 0)
        if stack:
            self.current_buff_stacks[buff_tuple] = stack
            if buff.interval > 0:
                self.current_buff_intervals[buff_tuple] = self.current_frame + buff.interval + 1
        else:
            self.current_buff_stacks.pop(buff_tuple, None)
            self.current_buff_intervals.pop(buff_tuple, None)

    def refresh_target_buff(self, buff_id, buff_level, buff_stack=1):
        buff = self.current_school.buffs[buff_id]
        buff_tuple = (buff_id, buff_level)
        stack = max(min(self.current_target_buff_stacks.get(buff_tuple, 0) + buff_stack, buff.max_stack), 0)
        if stack:
            self.current_target_buff_stacks[buff_tuple] = stack
            if buff.interval > 0:
                self.current_target_buff_intervals[buff_tuple] = self.current_frame + buff.interval + 1
        else:
            self.current_target_buff_stacks.pop(buff_tuple, None)
            self.current_target_buff_intervals.pop(buff_tuple, None)

    def clear_buff(self, buff_id, buff_level):
        buff_tuple = (buff_id, buff_level)
        self.current_buff_stacks.pop(buff_tuple, None)
        self.current_buff_intervals.pop(buff_tuple, None)

    def clear_target_buff(self, buff_id, buff_level):
        buff_tuple = (buff_id, buff_level)
        self.current_target_buff_stacks.pop(buff_tuple, None)
        self.current_target_buff_intervals.pop(buff_tuple, None)


class Parser(BaseParser):
    @property
    def duration(self):
        return round((self.end_frame - self.start_frame) / FRAME_PER_SECOND, 3)

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
        if player_id in self.id2name or school_id not in SUPPORT_SCHOOLS:
            return

        detail = parse(row)
        if isinstance(detail, list) and (school := SUPPORT_SCHOOLS.get(detail[3])):
            player_name = detail[1]
            self.id2name[player_id] = player_name
            self.name2id[player_name] = player_id
            self.select_equipments[player_id] = self.parse_equipments(detail[5])
            self.select_talents[player_id] = self.parse_talents(detail[6])
            if any(talent not in school.talent_gains for talent in self.select_talents[player_id]):
                return
            self.players[player_id] = deepcopy(school)
        elif (isinstance(detail, dict) and all(i in detail for i in (1, 4, 6, 7)) and
              (school := SUPPORT_SCHOOLS.get(detail[4]))):
            player_name = detail[1]
            self.id2name[player_id] = player_name
            self.name2id[player_name] = player_id
            self.select_equipments[player_id] = self.parse_equipments(detail[6])
            self.select_talents[player_id] = self.parse_talents(detail[7])
            if any(talent not in school.talent_gains for talent in self.select_talents[player_id]):
                return
            self.players[player_id] = deepcopy(school)

    def parse_npc(self, row):
        detail = row.strip("{}").split(",")
        npc_id, employer_id = detail[0], detail[3]
        if npc_id in self.id2name:
            return

        npc_name = detail[1].strip('"')

        self.id2name[npc_id] = npc_name
        self.name2id[npc_name] = npc_id
        if employer_id in self.players:
            self.pet2employer[npc_id] = employer_id

    def parse_pet(self, row):
        pet_id = row.strip().strip("{}")
        if player_id := self.pet2employer.get(pet_id):
            if self.next_pet_buff_stacks[player_id]:
                self.buff_stacks[pet_id] = self.next_pet_buff_stacks[player_id].pop()
            self.pet_snapshot[pet_id] = self.buff_stacks[player_id].copy()

    def parse_shift_buff(self, row):
        detail = row.strip("{}").split(",")
        player_id = detail[0]
        if player_id not in self.players:
            return

        buff_id, buff_stack, buff_level = int(detail[4]), int(detail[5]), int(detail[8])
        if buff_id not in self.players[player_id].buffs:
            return
        buff = self.players[player_id].buffs[buff_id]
        if frame_shift := buff.frame_shift:
            self.frame_shift_buffs[self.current_frame + frame_shift][player_id][(buff_id, buff_level)] = buff_stack
        # elif second_shift := buff.second_shift:
        #     self.second_shift_buffs[self.current_second + second_shift][player_id][(buff_id, buff_level)] = buff_stack

    def parse_frame_shift_status(self):
        for frame in list(self.frame_shift_buffs):
            if frame > self.current_frame:
                break
            for player_id, shift_buffs in self.frame_shift_buffs.pop(frame).items():
                for buff, buff_stack in shift_buffs.items():
                    if buff_stack:
                        self.buff_stacks[player_id][buff] = buff_stack
                    else:
                        self.buff_stacks[player_id].pop(buff, None)

    def parse_buff_intervals(self):
        for caster_id, buffs in self.buff_intervals.items():
            pop_buffs = []
            for buff, end_frame in buffs.items():
                if end_frame < self.current_frame:
                    self.buff_stacks[caster_id].pop(buff, None)
                    pop_buffs.append(buff)
            for pop_buff in pop_buffs:
                buffs.pop(pop_buff)
        for target_id in self.target_buff_intervals:
            for caster_id, buffs in self.target_buff_intervals[target_id].items():
                pop_buffs = []
                for buff, end_frame in buffs.items():
                    if end_frame < self.current_frame:
                        self.target_buff_stacks[target_id][caster_id].pop(buff, None)
                        pop_buffs.append(buff)
                for pop_buff in pop_buffs:
                    buffs.pop(pop_buff)

    def parse_buff(self, row):
        detail = row.strip("{}").split(",")
        caster_id = detail[0]
        if caster_id in self.pet2employer:
            player_id = self.pet2employer[caster_id]
            if caster_id in self.buff_stacks:
                buff_stacks = self.buff_stacks[caster_id]
            elif self.next_pet_buff_stacks[player_id]:
                buff_stacks = self.next_pet_buff_stacks[player_id][0]
            else:
                buff_stacks = {}
                self.next_pet_buff_stacks[player_id].append(buff_stacks)
        else:
            player_id = caster_id
            buff_stacks = self.buff_stacks[player_id]

        if player_id not in self.players:
            return

        buff_id, buff_stack, buff_level = int(detail[4]), int(detail[5]), int(detail[8])
        if buff_id not in self.players[player_id].buffs:
            return

        buff = self.players[player_id].buffs[buff_id]
        if buff.frame_shift:
            return

        self.current_player = player_id
        self.current_caster = caster_id
        if buff_stack:
            buff_stacks[(buff_id, buff_level)] = buff_stack
            buff.begin(self)
        else:
            buff_stacks.pop((buff_id, buff_level), None)
            buff.end(self)

    def parse_skill(self, row):
        detail = row.strip("{}").split(",")
        caster_id, target_id = detail[0], detail[1]
        if caster_id in self.pet2employer:
            player_id = self.pet2employer[caster_id]
        else:
            player_id = caster_id

        if player_id not in self.players:
            return

        react, skill_id, skill_level, critical = int(detail[2]), int(detail[4]), int(detail[5]), detail[6] == "true"
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
        skill.parse(critical, self)

    @staticmethod
    def filter_buff(buff, skill):
        if buff.gains:
            return True
        if buff.attributes:
            if buff.attributes is True:
                return True
            elif all("attack_power" in attr for attr in buff.attributes) and not skill.attack_power_call:
                return False
            elif all("surplus" in attr for attr in buff.attributes) and not skill.surplus_call:
                return False
            return True

    @property
    def status(self):
        skill = self.current_school.skills[self.current_skill]
        current_status = []
        for (buff_id, buff_level), buff_stack in self.current_buff_stacks.items():
            buff = self.current_school.buffs[buff_id]
            if self.filter_buff(buff, skill):
                current_status.append((buff_id, buff_level, buff_stack))

        snapshot_status = []
        for (buff_id, buff_level), buff_stack in self.current_snapshot.items():
            buff = self.current_school.buffs[buff_id]
            if self.filter_buff(buff, skill):
                snapshot_status.append((buff_id, buff_level, buff_stack))

        target_status = []
        for (buff_id, buff_level), buff_stack in self.current_target_buff_stacks.items():
            target_status.append((buff_id, buff_level, buff_stack))

        return tuple(current_status), tuple(snapshot_status), tuple(target_status)

    def __call__(self, file_name):
        self.file_name = file_name
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
            for talent_id in self.select_talents[player_id]:
                school.talent_gains[talent_id].add(school.attribute(), school.skills, school.buffs)
            school.prepare(self, player_id)

        for row in rows:
            self.current_frame = int(row[1])
            if row[4] == "13":
                self.parse_shift_buff(row[-1])

        for row in rows:
            if (current_frame := int(row[1])) != self.current_frame:
                self.current_frame = current_frame
                self.parse_frame_shift_status()
                self.parse_buff_intervals()

            if row[4] == "6":
                self.parse_pet(row[-1])
            elif row[4] == "13":
                self.parse_buff(row[-1])
            elif row[4] == "21":
                self.parse_skill(row[-1])

        self.end_frame = self.current_frame

        for player_id, school in self.players.items():
            for talent_id in self.select_talents[player_id]:
                school.talent_gains[talent_id].sub(school.attribute(), school.skills, school.buffs)

        for player_id in self.records:
            player_record = defaultdict(lambda: defaultdict(list))
            for target_id, records in self.records[player_id].items():
                for skill_tuple, status in records.items():
                    for status_tuple, timeline in status.items():
                        player_record[skill_tuple][status_tuple] += timeline
            self.records[player_id][""] = player_record
