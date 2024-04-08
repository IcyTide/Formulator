from typing import Dict

from luadata import unserialize

from base.buff import Buff
from base.skill import Skill


class Parser:
    def __init__(self, skills: Dict[str, Skill], buffs: Dict[str, Buff]):
        self.skills = skills
        self.buffs = buffs

        self.records = {}
        self.status = {}

        self.start_time = 0
        self.end_time = 0

    def parse_time(self, detail, timestamp):
        if detail[1]:
            self.start_time = int(timestamp)
        else:
            self.end_time = int(timestamp)
            return True

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

        if skill not in self.records:
            self.records[skill] = {}
        status = tuple(
            (buff_id, buff_level, buff_stack) for (buff_id, buff_level), buff_stack in self.status.items()
        )
        if status not in self.records[skill]:
            self.records[skill][status] = []
        self.records[skill][status].append(int(timestamp) - self.start_time)

    def __call__(self, file_name):
        for line in open(file_name):
            row = line.split("\t")
            if row[4] == "5" and self.parse_time(unserialize(row[-1]), row[3]):
                break
            elif row[4] == "13":
                self.parse_buff(unserialize(row[-1]))
            elif row[4] == "21":
                self.parse_skill(unserialize(row[-1]), row[3])
        return self.records
