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


class 蛇悉(Gain):
    def add_dots(self, dots: Dict[int, Dot]):
        for dot_id in (2296, 25917):
            dots[dot_id].tick_add += 2

    def sub_dots(self, dots: Dict[int, Dot]):
        for dot_id in (2296, 25917):
            dots[dot_id].tick_add -= 2


TALENTS: List[Dict[int, Gain]] = [
    {
        6618: Gain("尻尾", recipes=[(677, 2)]),
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
        6625: 蟾啸("蟾啸"),
    },
    {
        34640: Gain("忘情"),
        40069: Gain("裕蛊")
    },
    {
        30088: 嗜蛊("嗜蛊"),
    },
    {
        18330: Gain("固灵"),
        37351: Gain("释灵")
    },
    {
        25018: Gain("荒息")
    },
    {
        21302: 蛇悉("蛇悉")
    },
    {
        38581: Gain("急星")
    },
    {
        38455: Gain("残香", recipes=[(5608, 1)])
    }
]
