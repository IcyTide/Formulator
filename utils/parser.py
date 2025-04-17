from collections import defaultdict

from copy import deepcopy
from typing import Union

from base.constant import FRAME_PER_SECOND
from kungfus import *
from utils.lua import parse_lua

FRAME_TYPE, SECOND_TYPE = int, int
PLAYER_ID_TYPE, PLAYER_NAME_TYPE, TARGET_ID_TYPE, PET_ID_TYPE = str, str, str, str
CASTER_ID_TYPE = Union[PLAYER_ID_TYPE, PET_ID_TYPE]
SKILL_ID_TYPE, SKILL_LEVEL_TYPE, SKILL_CRITICAL_TYPE = int, int, bool
BUFF_ID_TYPE, BUFF_LEVEL_TYPE, BUFF_STACK_TYPE = int, int, int
SKILL_TYPE = Tuple[SKILL_ID_TYPE, SKILL_LEVEL_TYPE]
BUFF_TYPE = Dict[BUFF_ID_TYPE, Dict[BUFF_LEVEL_TYPE, BUFF_STACK_TYPE]]
DOT_TYPE = Tuple[BUFF_ID_TYPE, BUFF_LEVEL_TYPE, BUFF_STACK_TYPE]
DOT_DAMAGE_TYPE = Tuple[DOT_TYPE, SKILL_TYPE]
DAMAGE_TYPE = Tuple[SKILL_TYPE, tuple, tuple]

CURRENT_STATUS_TYPE, SNAPSHOT_STATUS_TYPE, TARGET_STATUS_TYPE = tuple, tuple, tuple
TOTAL_STATUS_TUPLE = Tuple[CURRENT_STATUS_TYPE, SNAPSHOT_STATUS_TYPE, TARGET_STATUS_TYPE]
TIMELINE_TYPE = Tuple[FRAME_TYPE, SKILL_CRITICAL_TYPE]
SUB_RECORD_TYPE = Dict[TOTAL_STATUS_TUPLE, List[TIMELINE_TYPE]]
RECORD_TYPE = Dict[Union[DAMAGE_TYPE, DOT_DAMAGE_TYPE], SUB_RECORD_TYPE]

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

IGNORE_TARGETS = [125406]


class BaseParser:
    CONTINUOUS_DELAY = 2

    current_player: PLAYER_ID_TYPE
    current_caster: CASTER_ID_TYPE
    current_target: TARGET_ID_TYPE
    current_damage: SKILL_ID_TYPE

    current_frame: FRAME_TYPE

    id2name: Dict[Union[CASTER_ID_TYPE, TARGET_ID_TYPE], PLAYER_NAME_TYPE]
    name2id: Dict[PLAYER_NAME_TYPE, Union[CASTER_ID_TYPE, TARGET_ID_TYPE]]
    pet2employer: Dict[PET_ID_TYPE, PLAYER_ID_TYPE]

    records: Dict[PLAYER_ID_TYPE, Dict[TARGET_ID_TYPE, RECORD_TYPE]]

    frame_shift_buffs: Dict[FRAME_TYPE, Dict[PLAYER_ID_TYPE, BUFF_TYPE]]
    begin_shift_buffs: Dict[PLAYER_ID_TYPE, BUFF_TYPE]

    id2buff: Dict[int, Tuple[BUFF_ID_TYPE, BUFF_LEVEL_TYPE, BUFF_STACK_TYPE]]
    buff_stacks: Dict[CASTER_ID_TYPE, BUFF_TYPE]
    buff_intervals: Dict[CASTER_ID_TYPE, BUFF_TYPE]
    target_buff_stacks: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, BUFF_TYPE]]
    target_buff_intervals: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, BUFF_TYPE]]

    dot_stacks: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_ID_TYPE, int]]]
    dot_ticks: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_ID_TYPE, int]]]
    dot_skills: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_ID_TYPE, DOT_DAMAGE_TYPE]]]

    dot_snapshot: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_ID_TYPE, BUFF_TYPE]]]
    pet_snapshot: Dict[PET_ID_TYPE, BUFF_TYPE]

    next_pet_buff_stacks: Dict[PLAYER_ID_TYPE, List[BUFF_TYPE]]

    last_dot: Dict[
        TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, Dict[BUFF_ID_TYPE, List[Tuple[DOT_DAMAGE_TYPE, TOTAL_STATUS_TUPLE]]]]]
    last_dot_frame: Dict[TARGET_ID_TYPE, Dict[PLAYER_ID_TYPE, FRAME_TYPE]]

    start_frame: FRAME_TYPE
    end_frame: FRAME_TYPE

    stop_frames: Dict[PLAYER_ID_TYPE, int]

    select_talents: Dict[PLAYER_ID_TYPE, List[int]]
    select_equipments: Dict[PLAYER_ID_TYPE, Dict[int, Dict[str, Union[int, list]]]]

    attributes: Dict[PLAYER_ID_TYPE, Attribute]
    gains: Dict[PLAYER_ID_TYPE, List[Gain]]
    recipes: Dict[PLAYER_ID_TYPE, List[Recipe]]

    players: Dict[PLAYER_ID_TYPE, Kungfu]
    targets: Dict[PLAYER_ID_TYPE, List[TARGET_ID_TYPE]]

    @property
    def current_kungfu(self):
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
    def current_next_pet_buff_stacks(self):
        return self.next_pet_buff_stacks[self.current_player]

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

    @property
    def current_last_dot_frame(self):
        return self.last_dot_frame[self.current_target][self.current_player]

    @property
    def current_stop_time(self):
        stop_frame = self.stop_frames.get(self.current_player, self.end_frame)
        return round((stop_frame - self.start_frame) / FRAME_PER_SECOND, 3)

    def reset(self):
        self.current_frame = 0

        self.id2name = {}
        self.name2id = {}
        self.pet2employer = {}

        self.records = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))

        self.frame_shift_buffs = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
        self.begin_shift_buffs = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

        self.id2buff = {}
        self.buff_stacks = defaultdict(lambda: defaultdict(dict))
        self.buff_intervals = defaultdict(lambda: defaultdict(dict))
        self.target_buff_stacks = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
        self.target_buff_intervals = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))

        self.dot_stacks = defaultdict(lambda: defaultdict(dict))
        self.dot_ticks = defaultdict(lambda: defaultdict(dict))
        self.dot_skills = defaultdict(lambda: defaultdict(dict))

        self.next_pet_buff_stacks = defaultdict(list)
        self.dot_snapshot = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
        self.pet_snapshot = defaultdict(dict)
        self.last_dot = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
        self.last_dot_frame = defaultdict(lambda: defaultdict(int))

        self.start_frame = 0

        self.stop_frames = {}

        self.select_talents = {}
        self.select_equipments = {}

        self.attributes = {}
        self.gains = {}
        self.recipes = {}

        self.players = {}
        self.targets = defaultdict(list)

    def refresh_buff(self, buff_id, buff_level, buff_stack=1):
        buff, buff.buff_level = self.current_kungfu.buffs[buff_id], buff_level
        stack = max(min(self.current_buff_stacks[buff_id].get(buff_level, 0) + buff_stack, buff.max_stack), 0)
        if stack:
            self.current_buff_stacks[buff_id][buff_level] = stack
            if buff.interval > 0:
                self.current_buff_intervals[buff_id][buff_level] = self.current_frame + buff.interval + 1
        else:
            self.clear_buff(buff_id, buff_level)

    def refresh_target_buff(self, buff_id, buff_level, buff_stack=1):
        buff, buff.buff_level = self.current_kungfu.buffs[buff_id], buff_level
        stack = max(min(self.current_target_buff_stacks[buff_id].get(buff_level, 0) + buff_stack, buff.max_stack), 0)
        if stack:
            self.current_target_buff_stacks[buff_id][buff_level] = stack
            if buff.interval:
                self.current_target_buff_intervals[buff_id][buff_level] = self.current_frame + buff.interval + 1
        else:
            self.clear_target_buff(buff_id, buff_level)

    def clear_buff(self, buff_id, buff_level=None):
        if buff_level:
            self.current_buff_stacks[buff_id].pop(buff_level, None)
            self.current_buff_intervals[buff_id].pop(buff_level, None)
            if not self.current_buff_stacks[buff_id]:
                self.current_buff_stacks.pop(buff_id, None)
                self.current_buff_intervals.pop(buff_id, None)
        else:
            self.current_buff_stacks.pop(buff_id, None)
            self.current_buff_intervals.pop(buff_id, None)

    def clear_target_buff(self, buff_id, buff_level=None):
        if buff_level:
            self.current_target_buff_stacks[buff_id].pop(buff_level, None)
            self.current_target_buff_intervals[buff_id].pop(buff_level, None)
            if not self.current_target_buff_stacks[buff_id]:
                self.current_target_buff_stacks.pop(buff_id, None)
                self.current_target_buff_intervals.pop(buff_id, None)
        else:
            self.current_target_buff_stacks.pop(buff_id, None)
            self.current_target_buff_intervals.pop(buff_id, None)


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
            select_equipment['enchant'] = row[5]
            if label == "近战武器" and -1 in row[4]:
                select_equipment['stone'] = row[4][-1][1]
        return select_equipments

    @staticmethod
    def parse_talents(detail):
        return [row[1] for row in detail]

    def parse_player(self, row):
        detail = parse_lua(row)
        player_id, kungfu_id = detail[0], detail[3]
        if kungfu_id not in SUPPORT_KUNGFU:
            return
        if player_id in self.select_talents and player_id in self.select_equipments:
            return

        try:
            player_name = detail[1]
            if equipments := detail.get(5):
                self.select_equipments[player_id] = self.parse_equipments(equipments.values())
            if talents := detail.get(6):
                self.select_talents[player_id] = self.parse_talents(talents.values())
                if player_id not in self.players:
                    self.players[player_id] = deepcopy(SUPPORT_KUNGFU[kungfu_id])
                for talent_id in self.select_talents[player_id]:
                    if (talent_id, 1) not in self.players[player_id].gains:
                        self.players.pop(player_id)
                        break
            self.id2name[player_id] = player_name
            self.name2id[player_name] = player_id
        except KeyError:
            return
        except IndexError:
            return

    def parse_npc(self, row):
        detail = parse_lua(row)
        npc_id, template_id, employer_id = detail[0], detail[2], detail[3]
        if npc_id in self.id2name or template_id in IGNORE_TARGETS:
            return

        npc_name = detail[1].strip('"')

        self.id2name[npc_id] = npc_name
        self.name2id[npc_name] = npc_id
        if employer_id in self.players:
            self.pet2employer[npc_id] = employer_id

    def parse_pet(self, row):
        pet_id = parse_lua(row)[0]
        if player_id := self.pet2employer.get(pet_id):
            if self.next_pet_buff_stacks[player_id]:
                self.buff_stacks[pet_id] = self.next_pet_buff_stacks[player_id].pop()
            self.pet_snapshot[pet_id] = deepcopy(self.buff_stacks[player_id])

    def prepare_shift_buff(self, row):
        detail = parse_lua(row)
        player_id = detail[0]
        if player_id not in self.players:
            return

        buff_id, buff_stack, buff_level = detail[4], detail[5], detail[8]
        if buff_id not in self.players[player_id].buffs:
            return
        buff = self.players[player_id].buffs[buff_id]
        if buff.begin_frame_shift and buff_stack:
            shift_frame = self.current_frame + buff.begin_frame_shift
            self.frame_shift_buffs[shift_frame][player_id][buff_id] = {buff_level: buff_stack}
        if buff.end_frame_shift and not buff_stack:
            shift_frame = self.current_frame + buff.end_frame_shift
            self.frame_shift_buffs[shift_frame][player_id][buff_id] = {buff_level: buff_stack}

    def parse_shift_buff(self):
        for frame in list(self.frame_shift_buffs):
            if frame > self.current_frame:
                break
            for player_id, shift_buffs in self.frame_shift_buffs.pop(frame).items():
                for buff_id, buff_levels in shift_buffs.items():
                    for buff_level, buff_stack in buff_levels.items():
                        if buff_stack:
                            self.buff_stacks[player_id][buff_id] = {buff_level: buff_stack}
                            self.begin_shift_buffs[player_id][buff_id][buff_level] += 1
                        else:
                            self.buff_stacks[player_id].pop(buff_id, None)

    def parse_custom_buff(self):
        for caster_id, buff_ids in self.buff_intervals.items():
            pop_buff_ids = []
            for buff_id, buff_levels in buff_ids.items():
                pop_buff_levels = []
                for buff_level, end_frame in buff_levels.items():
                    if end_frame < self.current_frame:
                        self.buff_stacks[caster_id][buff_id].pop(buff_level, None)
                        pop_buff_levels.append(buff_level)
                for buff_level in pop_buff_levels:
                    buff_levels.pop(buff_level)
                if not buff_levels:
                    pop_buff_ids.append(buff_id)
            for buff_id in pop_buff_ids:
                buff_ids.pop(buff_id)
        for target_id, buffs in self.target_buff_intervals.items():
            for caster_id, buff_ids in buffs.items():
                pop_buff_ids = []
                for buff_id, buff_levels in buff_ids.items():
                    pop_buff_levels = []
                    for buff_level, end_frame in buff_levels.items():
                        if end_frame < self.current_frame:
                            self.target_buff_stacks[target_id][caster_id][buff_id].pop(buff_level, None)
                            pop_buff_levels.append(buff_level)
                    for buff_level in pop_buff_levels:
                        buff_levels.pop(buff_level)
                    if not buff_levels:
                        pop_buff_ids.append(buff_id)
                for buff_id in pop_buff_ids:
                    buff_ids.pop(buff_id)

    def parse_buff(self, row):
        detail = parse_lua(row)
        caster_id = detail[0]
        if caster_id in self.pet2employer:
            player_id = self.pet2employer[caster_id]
            if caster_id in self.buff_stacks:
                buff_stacks = self.buff_stacks[caster_id]
            elif self.next_pet_buff_stacks[player_id]:
                buff_stacks = self.next_pet_buff_stacks[player_id][0]
            else:
                self.next_pet_buff_stacks[player_id].append(defaultdict(dict))
                buff_stacks = self.next_pet_buff_stacks[player_id][0]
        else:
            player_id = caster_id
            buff_stacks = self.buff_stacks[player_id]

        if player_id not in self.players:
            return

        # unique_id, end_frame = int(detail[2]), int(detail[6])
        buff_id, buff_stack, buff_level = detail[4], detail[5], detail[8]

        if buff_id not in self.players[player_id].buffs:
            return

        buff = self.players[player_id].buffs[buff_id]
        if buff.begin_frame_shift and buff_stack:
            self.begin_shift_buffs[player_id][buff_id][buff_level] -= 1
            return
        if buff.end_frame_shift and not buff_stack:
            return

        self.current_player = player_id
        self.current_caster = caster_id

        if buff_stack:
            if buff.continuous:
                self.current_buff_intervals.pop(buff_id, None)
            buff_stacks[buff_id][buff_level] = buff_stack
            buff.begin(self)
        else:
            if buff.continuous:
                self.current_buff_intervals[buff_id][buff_level] = self.CONTINUOUS_DELAY + 1
                return
            if self.begin_shift_buffs[player_id][buff_id].get(buff_level):
                return
            buff_stacks[buff_id].pop(buff_level, None)
            if not buff_stacks[buff_id]:
                buff_stacks.pop(buff_id, None)
            buff.end(self)

    def parse_damage(self, row):
        detail = parse_lua(row)
        caster_id, target_id = detail[0], detail[1]
        if caster_id in self.pet2employer:
            player_id = self.pet2employer[caster_id]
        else:
            player_id = caster_id

        if player_id not in self.players:
            return
        if target_id not in self.id2name:
            return

        react = detail[2]
        if react:
            return
        damage_id = detail[4]
        if damage_id not in self.players[player_id].skills and damage_id not in self.players[player_id].dots:
            return

        if not self.start_frame:
            self.start_frame = self.current_frame

        self.current_player = player_id
        self.current_caster = caster_id
        self.current_target = target_id
        self.current_damage = damage_id

        damage_type, damage_level  = detail[3], detail[5]
        actual_critical_strike, actual_damage = detail[6], detail[8].get(12, 0)
        self.record_damage(damage_id, damage_level, damage_type, actual_critical_strike, actual_damage)

    def record_damage(self, damage_id, damage_level, damage_type=1, actual_critical_strike=0, actual_damage=0):
        if damage_type == 1:
            damage, damage.skill_level = self.players[self.current_player].skills[damage_id], damage_level
            self.stop_frames[self.current_player] = self.current_frame
        elif damage_type == 2:
            damage, damage.buff_level = self.players[self.current_player].dots[damage_id], damage_level
            if self.current_last_dot_frame != self.current_frame:
                self.current_last_dot[damage_id] = []
                self.last_dot_frame[self.current_target][self.current_player] = self.current_frame
        else:
            return

        if damage.damage_call:
            if self.current_target not in self.current_targets:
                self.current_targets.append(self.current_target)
        else:
            actual_critical_strike, actual_damage = 0, 0
        damage.parse(actual_critical_strike, actual_damage, self)

    @staticmethod
    def filter_buff(buff, damage):
        if not damage.damage_call:
            return False
        if buff.recipes:
            return True
        if buff.attribute_effects:
            if all("attack_power" in attr for attr in buff.attribute_effects) and not damage.attack_power_call:
                return False
            elif all("surplus" in attr for attr in buff.attribute_effects) and not damage.surplus_call:
                return False
            return True

    @property
    def status(self):
        damage = self.current_kungfu.skills[self.current_damage]
        current_status = []
        for buff_id, buff_levels in self.current_buff_stacks.items():
            buff = self.current_kungfu.buffs[buff_id]
            for buff_level, buff_stack in buff_levels.items():
                buff.buff_level = buff_level
                if self.filter_buff(buff, damage):
                    current_status.append((buff_id, buff_level, buff_stack))

        snapshot_status = []
        for buff_id, buff_levels in self.pet_snapshot.get(self.current_caster, {}).items():
            buff = self.current_kungfu.buffs[buff_id]
            for buff_level, buff_stack in buff_levels.items():
                buff.buff_level = buff_level
                if self.filter_buff(buff, damage):
                    snapshot_status.append((buff_id, buff_level, buff_stack))

        target_status = []
        for buff_id, buff_levels in self.current_target_buff_stacks.items():
            buff = self.current_kungfu.buffs[buff_id]
            for buff_level, buff_stack in buff_levels.items():
                buff.buff_level = buff_level
                if self.filter_buff(buff, damage):
                    target_status.append((buff_id, buff_level, buff_stack))

        return tuple(current_status), tuple(snapshot_status), tuple(target_status)

    @property
    def dot_status(self):
        damage = self.current_kungfu.dots[self.current_damage]
        current_status = []
        for buff_id, buff_levels in self.current_buff_stacks.items():
            buff = self.current_kungfu.buffs[buff_id]
            for buff_level, buff_stack in buff_levels.items():
                buff.buff_level = buff_level
                if self.filter_buff(buff, damage):
                    current_status.append((buff_id, buff_level, buff_stack))
        snapshot_status = []
        for buff_id, buff_levels in self.current_dot_snapshot.get(self.current_damage, {}).items():
            buff = self.current_kungfu.buffs[buff_id]
            for buff_level, buff_stack in buff_levels.items():
                buff.buff_level = buff_level
                if self.filter_buff(buff, damage):
                    snapshot_status.append((buff_id, buff_level, buff_stack))

        target_status = []
        for buff_id, buff_levels in self.current_target_buff_stacks.items():
            buff = self.current_kungfu.buffs[buff_id]
            for buff_level, buff_stack in buff_levels.items():
                buff.buff_level = buff_level
                if self.filter_buff(buff, damage):
                    target_status.append((buff_id, buff_level, buff_stack))

        return tuple(current_status), tuple(snapshot_status), tuple(target_status)

    def kungfu_add(self):
        for player_id, kungfu in self.players.items():
            attribute = self.attributes[player_id] = kungfu.attribute()
            gains = self.gains[player_id] = []
            recipes = self.recipes[player_id] = []
            for talent_id in self.select_talents[player_id]:
                gain = kungfu.gains[(talent_id, 1)]
                gain.add(attribute, kungfu.buffs, kungfu.dots, kungfu.skills)
                gains.append(gain)
                for recipe_key in gain.recipes:
                    recipe = kungfu.recipes[recipe_key]
                    recipe.add(attribute, kungfu.buffs, kungfu.dots, kungfu.skills)
                    recipes.append(recipe)
            kungfu.prepare(self, player_id)

    def kungfu_sub(self):
        for player_id, kungfu in self.players.items():
            attribute = self.attributes[player_id]
            for gain in self.gains[player_id]:
                gain.sub(attribute, kungfu.buffs, kungfu.dots, kungfu.skills)
            for recipe in self.recipes[player_id]:
                recipe.sub(attribute, kungfu.buffs, kungfu.dots, kungfu.skills)

    def merge_targets(self):
        for player_id in self.records:
            player_record = defaultdict(lambda: defaultdict(list))
            for target_id, records in self.records[player_id].items():
                for damage_tuple, status in records.items():
                    for status_tuple, timeline in status.items():
                        player_record[damage_tuple][status_tuple] += timeline
            self.records[player_id][""] = player_record

    def __call__(self, file_name):
        self.file_name = file_name
        self.reset()
        try:
            lines = open(file_name, encoding="gbk").readlines()
        except UnicodeDecodeError:
            lines = open(file_name, encoding="utf-8").readlines()
        rows = []
        for line in lines:
            row = line.split("\t")
            if row[4] == "4":
                self.parse_player(row[-1])
            elif row[4] == "8":
                self.parse_npc(row[-1])
            if row[4] in ("6", "13", "21"):
                rows.append(row)

        self.kungfu_add()

        for row in rows:
            self.current_frame = int(row[1])
            if row[4] == "13":
                self.prepare_shift_buff(row[-1])

        for row in rows:
            if (current_frame := int(row[1])) != self.current_frame:
                self.current_frame = current_frame
                self.parse_shift_buff()
                self.parse_custom_buff()

            if row[4] == "6":
                self.parse_pet(row[-1])
            elif row[4] == "13":
                self.parse_buff(row[-1])
            elif row[4] == "21":
                self.parse_damage(row[-1])

        self.end_frame = self.current_frame

        self.kungfu_sub()
        self.merge_targets()
