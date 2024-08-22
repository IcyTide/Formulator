from typing import Dict

from base.gain import Gain
from base.skill import Skill


class 刻梦(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[14082].pet_buffs[23101] = {1: 1}
        skills[14082].pet_count = 2

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[14082].pet_buffs.pop(23101)
        skills[14082].pet_count = 1


TALENTS: Dict[int, Gain] = {
    14246: Gain("飞帆", recipes=[(2039, 1), (4562, 1)]),
    35981: Gain("明津"),
    32485: Gain("弦风"),
    34341: Gain("连徽"),
    30562: Gain("流照"),
    14336: Gain("豪情"),
    14282: Gain("师襄", recipes=[(2974, 1)]),
    30984: Gain("知止"),
    14873: 刻梦("刻梦"),
    35982: Gain("争鸣"),
    18712: Gain("云汉"),
    14350: Gain("参连"),
    34344: Gain("正律和鸣"),
    37287: Gain("响壑", recipes=[(5496, 1), (5583, 1)])
}

TALENT_CHOICES = [
    [14246],
    [35981],
    [32485, 34341],
    [30562],
    [14336],
    [14282],
    [30984],
    [14873],
    [35982],
    [18712],
    [14350],
    [34344, 37287]
]
