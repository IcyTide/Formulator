import json
import os.path

from utils.lua import parse


class Parser:
    buffs: dict = None

    @staticmethod
    def parse_talents(detail):
        return [row[1] for row in detail]

    def parse_buff(self, row):
        detail = row.strip("{}").split(",")
        buff_id, buff_stack, buff_level = int(detail[4]), int(detail[5]), int(detail[8])
        if buff_id not in self.buffs:
            self.buffs[buff_id] = {}
        if buff_level not in self.buffs[buff_id]:
            self.buffs[buff_id][buff_level] = []
        if buff_stack not in self.buffs[buff_id][buff_level]:
            self.buffs[buff_id][buff_level].append(buff_stack)
            self.buffs[buff_id][buff_level].sort()

    def parse_skill(self, row):
        detail = row.strip("{}").split(",")

        skill_id, skill_level, critical = int(detail[4]), int(detail[5]), detail[6] == "true"
        if skill_id not in self.skills:
            self.skills[skill_id] = []
        if skill_level not in self.skills[skill_id]:
            self.skills[skill_id].append(skill_level)
            self.skills[skill_id].sort()

    def __call__(self, file_name):
        self.buffs = {}
        self.skills = {}
        self.talents = []
        lines = open(file_name).readlines()
        for line in lines:
            row = line.split("\t")
            if row[4] == "4":
                detail = parse(row[-1])
                if isinstance(detail, list):
                    self.talents = self.parse_talents(detail[6])
        for line in lines:
            row = line.split("\t")
            if row[4] == "13":
                self.parse_buff(row[-1])
            elif row[4] == "21":
                self.parse_skill(row[-1])
        json.dump(self.skills, open("skills.json", "w", encoding="utf-8"))
        print(len(self.skills))
        json.dump(self.buffs, open("buffs.json", "w", encoding="utf-8"))
        print(len(self.buffs))


if __name__ == '__main__':
    parser = Parser()
    parser("new.jcl")
