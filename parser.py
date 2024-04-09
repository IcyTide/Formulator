from typing import Dict

from base.buff import Buff
from base.skill import Skill
from utils.lua import parse


class Parser:
    records: dict
    status: dict

    start_time: list
    end_time: list

    info_flag: bool
    fight_flag: bool

    school: int

    def __init__(self, skills: Dict[str, Skill], buffs: Dict[str, Buff]):
        self.skills = skills
        self.buffs = buffs

    def reset(self):
        self.info_flag = True
        self.fight_flag = False

        self.records = {}
        self.status = {}

        self.start_time = []
        self.end_time = []

    def parse_info(self, detail):
        if isinstance(detail, list):
            self.info_flag = False

    def parse_time(self, detail, timestamp):
        if detail[1]:
            self.start_time.append(int(timestamp))
            self.records[self.start_time[-1]] = {}
            self.fight_flag = True
        else:
            self.end_time.append(int(timestamp))
            self.fight_flag = False

    def parse_buff(self, detail):
        buff_id, buff_stack, buff_level = detail[4], detail[5], detail[8]
        if buff_id not in self.buffs:
            return
        if not buff_stack:
            self.status.pop((buff_id, buff_level))
        else:
            self.status[(buff_id, buff_level)] = buff_stack

    def parse_skill(self, detail, timestamp):
        skill = detail[4], detail[5]
        if skill[0] not in self.skills:
            return

        current_record = self.records[self.start_time[-1]]
        if skill not in current_record:
            current_record[skill] = {}
        status = tuple(
            (buff_id, buff_level, buff_stack) for (buff_id, buff_level), buff_stack in self.status.items()
        )
        if status not in current_record[skill]:
            current_record[skill][status] = []
        current_record[skill][status].append(int(timestamp) - self.start_time[-1])

    def __call__(self, file_name):
        self.reset()

        for line in open(file_name):
            row = line.split("\t")
            if row[4] == "4" and self.info_flag:
                self.parse_info(parse(row[-1]))
            elif row[4] == "5":
                self.parse_time(parse(row[-1]), row[3])
            elif row[4] == "13":
                self.parse_buff(parse(row[-1]))
            elif row[4] == "21" and self.fight_flag:
                self.parse_skill(parse(row[-1]), row[3])

        return self.records
