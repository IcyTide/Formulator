from collections import defaultdict

from base.constant import FRAME_PER_SECOND
from schools import *
from utils.lua import parse

FRAME_TYPE, PLAYER_ID_TYPE, PLAYER_NAME_TYPE, PET_ID_TYPE = int, int, int, int
CASTER_ID_TYPE = PLAYER_ID_TYPE | PET_ID_TYPE
SKILL_ID_TYPE, SKILL_LEVEL_TYPE, SKILL_STACK_TYPE, SKILL_CRITICAL_TYPE = int, int, int, bool
SKILL_BUFFER_TYPE = Tuple[SKILL_ID_TYPE, SKILL_LEVEL_TYPE, SKILL_CRITICAL_TYPE]
SKILL_TYPE = Tuple[SKILL_ID_TYPE, SKILL_LEVEL_TYPE, SKILL_STACK_TYPE]
BUFF_ID_TYPE, BUFF_LEVEL_TYPE, BUFF_STACK_TYPE = int, int, int
BUFF_TYPE = Tuple[BUFF_ID_TYPE, BUFF_LEVEL_TYPE]
STATUS_TYPE = Tuple[BUFF_ID_TYPE, BUFF_LEVEL_TYPE, BUFF_STACK_TYPE]

SNAPSHOT_TYPE = Dict[SKILL_ID_TYPE | PET_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]

TIMELINE_TYPE = List[Tuple[FRAME_TYPE, SKILL_CRITICAL_TYPE]]
SUB_RECORD_TYPE = Dict[Tuple[tuple, tuple], TIMELINE_TYPE]
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

BUFFER_DELAY = 0


class Parser:
    current_player: PLAYER_ID_TYPE
    current_caster: CASTER_ID_TYPE
    current_frame: FRAME_TYPE
    frames: List[FRAME_TYPE]

    id2name: Dict[PLAYER_ID_TYPE, PLAYER_NAME_TYPE]
    name2id: Dict[PLAYER_NAME_TYPE, PLAYER_ID_TYPE]
    pets: Dict[PET_ID_TYPE, PLAYER_ID_TYPE]
    records: Dict[PLAYER_ID_TYPE, RECORD_TYPE]

    hidden_buffs: Dict[PLAYER_ID_TYPE, Dict[BUFF_TYPE, FRAME_TYPE]]
    shift_status: Dict[FRAME_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]]
    status: Dict[PLAYER_ID_TYPE, Dict[BUFF_TYPE, BUFF_STACK_TYPE]]

    stacks: Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, int]]
    ticks: Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, int]]

    snapshot: Dict[PLAYER_ID_TYPE, SNAPSHOT_TYPE]
    last_dot: Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, Tuple[SKILL_TYPE, Tuple[tuple, tuple]]]]
    next_dot: Dict[PLAYER_ID_TYPE, Dict[SKILL_ID_TYPE, int]]

    start_frame: FRAME_TYPE
    end_frame: FRAME_TYPE

    select_talents: Dict[PLAYER_ID_TYPE, List[int]]
    select_equipments: Dict[PLAYER_ID_TYPE, Dict[int, Dict[str, int | list]]]

    school: Dict[PLAYER_ID_TYPE, School]

    @property
    def current_school(self):
        return self.school[self.current_player]

    @property
    def current_records(self):
        return self.records[self.current_player]

    @property
    def current_hidden_buffs(self):
        return self.hidden_buffs[self.current_player]

    @property
    def current_status(self):
        return self.status[self.current_player]

    @property
    def current_snapshot(self):
        return self.snapshot[self.current_player]

    @property
    def current_stacks(self):
        return self.stacks[self.current_player]

    @property
    def current_ticks(self):
        return self.ticks[self.current_player]

    @property
    def current_last_dot(self):
        return self.last_dot[self.current_player]

    @property
    def current_next_dot(self):
        return self.next_dot[self.current_player]

    @property
    def duration(self):
        return round((self.end_frame - self.start_frame) / FRAME_PER_SECOND, 3)

    def reset(self):
        self.current_frame = 0

        self.frames = []

        self.id2name = {}
        self.name2id = {}
        self.pets = {}

        self.records = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

        self.hidden_buffs = defaultdict(dict)
        self.shift_status = defaultdict(lambda: defaultdict(dict))
        self.status = defaultdict(lambda: defaultdict(int))

        self.stacks = defaultdict(lambda: defaultdict(lambda: 1))
        self.ticks = defaultdict(lambda: defaultdict(lambda: 0))
        self.snapshot = defaultdict(dict)
        self.last_dot = defaultdict(dict)
        self.next_dot = defaultdict(dict)

        self.start_frame = 0

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
                self.select_equipments[player_id] = self.parse_equipments(detail[5])
                self.select_talents[player_id] = self.parse_talents(detail[6])
                if any(talent not in school.talent_gains for talent in self.select_talents[player_id]):
                    return
                self.school[player_id] = school

    def parse_shift_buff(self, row):
        detail = row.strip("{}").split(",")
        player_id = int(detail[0])
        if player_id not in self.school:
            return
        buff_id, buff_stack, buff_level = int(detail[4]), int(detail[5]), int(detail[8])
        if buff_id not in self.school[player_id].buffs:
            return

        frame_shift = self.school[player_id].buffs[buff_id].frame_shift
        if frame_shift:
            self.shift_status[self.current_frame + frame_shift][player_id][(buff_id, buff_level)] = buff_stack

    def parse_shift_status(self):
        for frame in list(self.shift_status):
            if frame > self.current_frame:
                break
            for player_id, status_buffer in self.shift_status.pop(frame).items():
                for buff, buff_stack in status_buffer.items():
                    if buff_stack:
                        self.status[player_id][buff] = buff_stack
                    else:
                        self.status[player_id].pop(buff, None)

    def parse_hidden_buffs(self):
        for player_id, hidden_buffs in self.hidden_buffs.items():
            for buff, end_frame in hidden_buffs.items():
                if end_frame < self.current_frame:
                    self.status[player_id].pop(buff, None)

    def parse_status(self, row):
        detail = row.strip("{}").split(",")
        player_id = int(detail[0])
        if player_id not in self.school:
            return

        buff_id, buff_stack, buff_level = int(detail[4]), int(detail[5]), int(detail[8])
        if buff_id not in self.school[player_id].buffs:
            return

        frame_shift = self.school[player_id].buffs[buff_id].frame_shift
        if frame_shift:
            return

        if buff_stack:
            self.status[player_id][(buff_id, buff_level)] = buff_stack
        else:
            self.status[player_id].pop((buff_id, buff_level), None)

    def parse_skill(self, row):
        detail = row.strip("{}").split(",")
        caster_id, target_id = int(detail[0]), int(detail[1])
        if caster_id in self.pets:
            player_id = self.pets[caster_id]
        else:
            player_id = caster_id

        if player_id not in self.school:
            return

        react, skill_id, skill_level, critical = int(detail[2]), int(detail[4]), int(detail[5]), detail[6] == "true"
        if react or skill_id not in self.school[player_id].skills:
            return

        if not self.start_frame:
            self.start_frame = self.current_frame - 1

        self.current_player = player_id
        self.current_caster = caster_id
        skill = self.school[player_id].skills[skill_id]
        skill.record(skill_level, critical, self)

    def parse_pet(self, row):
        detail = row.strip("{}").split(",")
        pet_id, player_id = int(detail[0]), int(detail[3])
        if player_id in self.school:
            self.pets[pet_id] = player_id
            self.snapshot[player_id][pet_id] = self.status[player_id].copy()

    def available_status(self, skill_id, snapshot_id=None):
        if not snapshot_id:
            snapshot_id = skill_id

        current_status = []
        for (buff_id, buff_level), buff_stack in self.current_status.items():
            buff = self.current_school.buffs[buff_id]
            if buff.gain_attributes:
                current_status.append((buff_id, buff_level, buff_stack))
            elif buff.gain_skills and skill_id in buff.gain_skills:
                current_status.append((buff_id, buff_level, buff_stack))

        snapshot_status = []
        for (buff_id, buff_level), buff_stack in self.current_snapshot.get(snapshot_id, {}).items():
            buff = self.current_school.buffs[buff_id]
            if buff.gain_attributes:
                snapshot_status.append((buff_id, buff_level, buff_stack))
            elif buff.gain_skills and skill_id in buff.gain_skills:
                snapshot_status.append((buff_id, buff_level, buff_stack))

        return tuple(current_status), tuple(snapshot_status)

    def __call__(self, file_name):
        self.reset()
        lines = open(file_name).readlines()
        rows = []
        for line in lines:
            row = line.split("\t")
            rows.append(row)
            if row[4] == "4":
                self.parse_info(row[-1])

        for player_id, school in self.school.items():
            school.prepare(self, player_id)
            for talent_id in self.select_talents[player_id]:
                school.talent_gains[talent_id].add_skills(school.skills)

        for row in rows:
            self.current_frame = int(row[1])
            if row[4] == "13":
                self.parse_shift_buff(row[-1])

        for row in rows:
            self.current_frame = int(row[1])
            self.parse_shift_status()
            self.parse_hidden_buffs()
            if row[4] == "8":
                self.parse_pet(row[-1])
            elif row[4] == "13":
                self.parse_status(row[-1])
            elif row[4] == "21":
                self.parse_skill(row[-1])

        self.end_frame = self.current_frame

        for player_id, school in self.school.items():
            for talent_id in self.select_talents[player_id]:
                school.talent_gains[talent_id].sub_skills(school.skills)


if __name__ == '__main__':
    parser = Parser()
    parser("../dao_zong.jcl")
    print(1)
