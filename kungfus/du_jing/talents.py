from typing import Dict, List

from base.dot import Dot
from base.gain import Gain
from base.skill import Skill


class 虫兽(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2223].pre_buffs[12497] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2223].pre_buffs.pop(12497)


class 蟾啸(Gain):
    def add_dots(self, dots: Dict[int, Dot]):
        dots[2295].tick_add += 2

    def sub_dots(self, dots: Dict[int, Dot]):
        dots[2295].tick_add -= 2


class 嗜蛊(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2226].pre_buffs[22232] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2226].pre_buffs.pop(22232)


class 引魂(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2223].pet_buffs[16102] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2223].pet_buffs.pop(16102)


class 蛇悉(Gain):
    def add_dots(self, dots: Dict[int, Dot]):
        dots[2296].tick_add += 2

    def sub_dots(self, dots: Dict[int, Dot]):
        dots[2296].tick_add -= 2


TALENTS: List[Dict[int, Gain]] = [
    {
        6618: Gain("尻尾", skill_ids=[40198], recipes=[(677, 2)]),
    },
    {
        6649: Gain("食髓", skill_ids=[6648]),
        6622: Gain("无常", recipes=[(1265, 1), (2427, 1)])
    },
    {
        6629: Gain("黯影", skill_ids=[34389], recipes=[
            (recipe_id, 1) for recipe_id in (1269, 1270, 1271, 1272, 2436, 4550, 3263, 5538)
        ]),
        30572: Gain("不僵", dot_ids=[22730, 22731], skill_ids=[30578, 30579])
    },
    {
        6879: 虫兽("虫兽", buff_ids=[12497])
    },
    {
        6625: 蟾啸("蟾啸", skill_ids=[13473]),
        34388: Gain("重蛊", buff_ids=[25769]),
        18312: Gain("蝎噬")
    },
    {
        40617: Gain("忘情", recipes=[(5891, 1), (5898, 1), (5901, 1)]),
        37952: Gain("不鸣", skill_ids=[37959])
    },
    {
        30088: 嗜蛊("嗜蛊", buff_ids=[22232]),
    },
    {
        18330: Gain("固灵", dot_ids=[12557, 22731], skill_ids=[18700, 30579]),
        37351: Gain("释灵", skill_ids=[37352], dot_ids=[28210])
    },
    {
        25018: Gain("荒息"),
        32741: Gain("驭虫")
    },
    {
        38455: Gain("残香", skill_ids=[38454], recipes=[(5608, 1)])
    },
    {
        38581: Gain("急星"),
        18325: 引魂("引魂", skill_ids=[22997, 36292], buff_ids=[16102, 16103]),
        25038: Gain("二圣", skill_ids=[25039])
    },
    {
        21302: 蛇悉("蛇悉", skill_ids=[21303]),
        25043: Gain("连缘蛊", skill_ids=[25044, 30918], buff_ids=[19513])
    }
]
