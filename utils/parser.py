from collections import defaultdict

from base.constant import FRAME_PER_SECOND
from schools import *
from utils.lua import parse

FRAME_TYPE, SECOND_TYPE = int, int
PLAYER_ID_TYPE, PLAYER_NAME_TYPE, TARGET_ID_TYPE, PET_ID_TYPE = int, int, int, int
CASTER_ID_TYPE = PLAYER_ID_TYPE | PET_ID_TYPE
SKILL_ID_TYPE, SKILL_LEVEL_TYPE, SKILL_STACK_TYPE, SKILL_CRITICAL_TYPE = int, int, int, bool
SKILL_TYPE = Tuple[SKILL_ID_TYPE, SKILL_LEVEL_TYPE, SKILL_STACK_TYPE]
BUFF_ID_TYPE, BUFF_LEVEL_TYPE, BUFF_STACK_TYPE = int, int, int
BUFF_TYPE = Tuple[BUFF_ID_TYPE, BUFF_LEVEL_TYPE]

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


class Parser:
    current_player: PLAYER_ID_TYPE
    current_caster: CASTER_ID_TYPE
    current_target: TARGET_ID_TYPE
    current_skill: SKILL_ID_TYPE

    current_frame: FRAME_TYPE
    current_second: SECOND_TYPE

    id2name: Dict[PLAYER_ID_TYPE | TARGET_ID_TYPE, PLAYER_NAME_TYPE]
    name2id: Dict[PLAYER_NAME_TYPE, PLAYER_ID_TYPE | TARGET_ID_TYPE]
    pets: Dict[PET_ID_TYPE, PLAYER_ID_TYPE]
    records: Dict[PLAYER_ID_TYPE, Dict[TARGET_ID_TYPE, RECORD_TYPE]]

    frame_shift_buffs: Dict[FRAME_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]]
    second_shift_buffs: Dict[SECOND_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]]
    hidden_buffs: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_TYPE, FRAME_TYPE]]]

    player_buffs: Dict[PLAYER_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]
    target_buffs: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]]

    stacks: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, int]]]
    ticks: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, int]]]

    pet_snapshot: Dict[PET_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]
    dot_snapshot: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]]]

    last_dot: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, Tuple[SKILL_TYPE, Tuple[tuple, tuple]]]]]
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
        return self.records[self.current_player][self.current_target]

    @property
    def current_hidden_buffs(self):
        return self.hidden_buffs[self.current_target][self.current_player]

    @property
    def current_player_buffs(self):
        return self.player_buffs[self.current_player]

    @property
    def current_target_buffs(self):
        return self.target_buffs[self.current_target][self.current_player]

    @property
    def current_snapshot(self):
        if self.current_caster in self.pet_snapshot:
            return self.pet_snapshot[self.current_caster]
        else:
            return self.dot_snapshot[self.current_target][self.current_player].get(self.current_skill, {})

    @property
    def current_dot_snapshot(self):
        return self.dot_snapshot[self.current_target][self.current_player]

    @property
    def current_stacks(self):
        return self.stacks[self.current_target][self.current_player]

    @property
    def current_ticks(self):
        return self.ticks[self.current_target][self.current_player]

    @property
    def current_last_dot(self):
        return self.last_dot[self.current_target][self.current_player]

    @property
    def current_next_dot(self):
        return self.next_dot[self.current_target][self.current_player]

    @property
    def duration(self):
        return round((self.end_frame - self.start_frame) / FRAME_PER_SECOND, 3)

    def reset(self):
        self.current_frame = 0
        self.current_second = 0

        self.id2name = {}
        self.name2id = {}
        self.pets = {}

        self.records = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))

        self.hidden_buffs = defaultdict(lambda: defaultdict(dict))
        self.frame_shift_buffs = defaultdict(lambda: defaultdict(dict))
        self.second_shift_buffs = defaultdict(lambda: defaultdict(dict))

        self.player_buffs = defaultdict(dict)
        self.target_buffs = defaultdict(lambda: defaultdict(dict))

        self.stacks = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 1)))
        self.ticks = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0)))

        self.pet_snapshot = dict()
        self.dot_snapshot = defaultdict(lambda: defaultdict(dict))
        self.last_dot = defaultdict(lambda: defaultdict(dict))
        self.next_dot = defaultdict(lambda: defaultdict(dict))

        self.start_frame = 0

        self.select_talents = {}
        self.select_equipments = {}

        self.players = {}
        self.targets = defaultdict(list)

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
        player_id, school_id = int(detail[0]), int(detail[3])
        if player_id in self.id2name or school_id not in SUPPORT_SCHOOL:
            return

        if isinstance(detail := parse(row), list) and (school := SUPPORT_SCHOOL.get(detail[3])):
            player_name = detail[1]
            self.id2name[player_id] = player_name
            self.name2id[player_name] = player_id
            self.select_equipments[player_id] = self.parse_equipments(detail[5])
            self.select_talents[player_id] = self.parse_talents(detail[6])
            if any(talent not in school.talent_gains for talent in self.select_talents[player_id]):
                return
            self.players[player_id] = school

    def parse_npc(self, row):
        detail = row.strip("{}").split(",")
        npc_id, player_id = int(detail[0]), int(detail[3])
        if npc_id in self.id2name:
            return

        npc_name = detail[1]
        self.id2name[npc_id] = npc_name
        self.name2id[npc_name] = npc_id
        if player_id:
            self.pets[npc_id] = player_id

    def parse_pet(self, row):
        detail = row.strip("{}").split(",")
        pet_id, player_id = int(detail[0]), int(detail[3])
        if pet_id in self.pets:
            self.pet_snapshot[pet_id] = self.player_buffs[player_id].copy()

    def parse_shift_buff(self, row):
        detail = row.strip("{}").split(",")
        player_id = int(detail[0])
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
                        self.player_buffs[player_id][buff] = buff_stack
                    else:
                        self.player_buffs[player_id].pop(buff, None)

    def parse_second_shift_status(self):
        for second in list(self.second_shift_buffs):
            if second > self.current_second:
                break
            for player_id, shift_buffs in self.second_shift_buffs.pop(second).items():
                for buff, buff_stack in shift_buffs.items():
                    if buff_stack:
                        self.player_buffs[player_id][buff] = buff_stack
                    else:
                        self.player_buffs[player_id].pop(buff, None)

    def parse_hidden_buffs(self):
        for target_id in self.hidden_buffs:
            for player_id, hidden_buffs in self.hidden_buffs[target_id].items():
                for buff, end_frame in hidden_buffs.items():
                    if end_frame < self.current_frame:
                        self.target_buffs[target_id][player_id].pop(buff, None)

    def parse_buff(self, row):
        detail = row.strip("{}").split(",")
        player_id = int(detail[0])
        if player_id not in self.players:
            return

        buff_id, buff_stack, buff_level = int(detail[4]), int(detail[5]), int(detail[8])
        if buff_id not in self.players[player_id].buffs:
            return

        frame_shift = self.players[player_id].buffs[buff_id].frame_shift
        if frame_shift:
            return

        if buff_stack:
            self.player_buffs[player_id][(buff_id, buff_level)] = buff_stack
        else:
            self.player_buffs[player_id].pop((buff_id, buff_level), None)

    def parse_skill(self, row):
        detail = row.strip("{}").split(",")
        caster_id, target_id = int(detail[0]), int(detail[1])
        if caster_id in self.pets:
            player_id = self.pets[caster_id]
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
        if target_id not in self.current_targets:
            self.current_targets.append(target_id)
        self.current_target = target_id
        self.current_skill = skill_id
        skill = self.players[player_id].skills[skill_id]
        skill.skill_level = skill_level
        skill.record(critical, self)

    def status(self, skill_id):
        current_status = []
        for (buff_id, buff_level), buff_stack in self.current_player_buffs.items():
            buff = self.current_school.buffs[buff_id]
            if buff.gain_attributes:
                current_status.append((buff_id, buff_level, buff_stack))
            elif buff.gain_skills and skill_id in buff.gain_skills:
                current_status.append((buff_id, buff_level, buff_stack))

        self.current_skill = skill_id
        snapshot_status = []
        for (buff_id, buff_level), buff_stack in self.current_snapshot.items():
            buff = self.current_school.buffs[buff_id]
            if buff.gain_attributes:
                snapshot_status.append((buff_id, buff_level, buff_stack))
            elif buff.gain_skills and skill_id in buff.gain_skills:
                snapshot_status.append((buff_id, buff_level, buff_stack))

        target_status = []
        for (buff_id, buff_level), buff_stack in self.current_target_buffs.items():
            buff = self.current_school.buffs[buff_id]
            if buff.gain_attributes:
                target_status.append((buff_id, buff_level, buff_stack))
            elif buff.gain_skills and skill_id in buff.gain_skills:
                target_status.append((buff_id, buff_level, buff_stack))

        return tuple(current_status), tuple(snapshot_status), tuple(target_status)

    def __call__(self, file_name):
        self.file_name = file_name
        self.reset()
        lines = open(file_name).readlines()
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
            self.current_frame = int(row[1])
            # self.current_second = int(row[3])
            if row[4] == "13":
                self.parse_shift_buff(row[-1])

        for row in rows:
            if (current_frame := int(row[1])) != self.current_frame:
                self.current_frame = current_frame
                self.parse_frame_shift_status()
                self.parse_hidden_buffs()
            # if (current_second := int(row[3])) != self.current_second:
            #     self.current_second = current_second
            #     self.parse_frame_shift_status()

            if row[4] == "8":
                self.parse_pet(row[-1])
            elif row[4] == "13":
                self.parse_buff(row[-1])
            elif row[4] == "21":
                self.parse_skill(row[-1])

        self.end_frame = self.current_frame

        for player_id, school in self.players.items():
            for talent_id in self.select_talents[player_id]:
                school.talent_gains[talent_id].sub_skills(school.skills)

        for player_id in self.records:
            player_record = defaultdict(lambda: defaultdict(list))
            for target_id, records in self.records[player_id].items():
                for skill_tuple, status in records.items():
                    for status_tuple, timeline in status.items():
                        player_record[skill_tuple][status_tuple] += timeline
            self.records[player_id][0] = player_record
