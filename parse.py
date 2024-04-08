from typing import Dict

from luadata import unserialize

from base.buff import Buff
from base.skill import Skill


class Parser:
    def __init__(self, skills: Dict[str, Skill], buffs: Dict[str, Buff]):
        self.skills = skills
        self.buffs = buffs

        self.summary = {}
        self.status = {}

        self.start_time = 0
        self.end_time = 0

    def parse_time(self, detail, timestamp):
        if detail[1]:
            self.start_time = timestamp
        else:
            self.end_time = timestamp
            return True

    def parse_buff(self, detail):
        buff_id, buff_stack, buff_level = detail[4], detail[5], detail[8]
        if buff_id not in self.buffs:
            return
        if not buff_stack:
            self.status.pop((buff_id, buff_level))
        else:
            self.status[(buff_id, buff_level)] = buff_stack

    def parse_skill(self, detail):
        skill = detail[4], detail[5]
        if skill[0] not in self.skills:
            return

        if skill not in self.summary:
            self.summary[skill] = {}
        status = tuple(
            (buff_id, buff_level, buff_stack) for (buff_id, buff_level), buff_stack in self.status.items()
        )
        if status not in self.summary[skill]:
            self.summary[skill][status] = 0
        self.summary[skill][status] += 1

    def __call__(self, logs):
        for row in logs:
            if row[4] == "5" and self.parse_time(unserialize(row[-1]), row[3]):
                break
            elif row[4] == "13":
                self.parse_buff(unserialize(row[-1]))
            elif row[4] == "21":
                self.parse_skill(unserialize(row[-1]))
        return self.summary
