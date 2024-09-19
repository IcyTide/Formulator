from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


class 引魂(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2223].pet_buffs[16102] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2223].pet_buffs.pop(16102)


class 虫兽(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2223].pre_buffs[12497] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2223].pre_buffs.pop(12497)


class 嗜蛊(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2226].pre_buffs[22232] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2226].pre_buffs.pop(22232)


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            6618: Gain("尻尾"),
            6620: Gain("蝎毒")
        },
        {
            6649: Gain("食髓")
        },
        {
            6629: Gain("黯影", recipes=[
                (recipe_id, 1) for recipe_id in (1269, 1270, 1271, 1272, 2436, 4550, 3263, 5538)
            ])
        },
        {
            6879: 虫兽("虫兽")
        },
        {
            34388: Gain("重蛊")
        },
        {
            37952: Gain("不鸣"),
            34640: Gain("忘情")
        },
        {
            30088: 嗜蛊("嗜蛊"),
            25040: Gain("曲致", buff_ids=[-17988], recipes=[(-134, 1)]),
        },
        {
            18330: Gain("固灵")
        },
        {
            25018: Gain("荒息")
        },
        {
            29545: Gain("篾片蛊")
        },
        {
            18325: 引魂("引魂")
        },
        {
            25043: Gain("连缘蛊")
        }
    ]
}
