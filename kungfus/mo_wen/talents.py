from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


class 刻梦(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[14082].pet_buffs[23101] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[14082].pet_buffs.pop(23101)


class 参连(Gain):
    def add_skills(self, skills):
        skills[14070].post_buffs = {9437: {1: 1}}

    def sub_skills(self, skills):
        skills[14070].post_buffs.pop(9437)


TALENTS: List[Dict[int, Gain]] = [
    {
        14246: Gain("飞帆", recipes=[(2039, 1), (4562, 1)]),
        14236: Gain("号钟", recipes=[(2036, 1), (4561, 1), (2157, 1), (2535, 1)])
    },
    {
        35981: Gain("明津", buff_ids=[9495]),
        14441: Gain("鹿鸣", recipes=[(5833, 1)])
    },
    {
        34341: Gain("连徽", skill_ids=[34514]),
        18704: Gain("削竹", recipes=[(5834, 1)])
    },
    {
        30562: Gain("流照", skill_ids=[30799], recipes=[(2975, 1)]),
        14285: Gain("殊曲", dot_ids=[9358, 9362], skill_ids=[14288, 17789, 14292, 17793]),
        18727: Gain("照月", buff_ids=[30464])
    },
    {
        14336: Gain("豪情"),
        14871: Gain("浮影")
    },
    {
        14282: Gain("师襄", recipes=[(2974, 1)]),
        14151: Gain("爻辰", recipes=[(5915, 1)])
    },
    {
        14350: 参连("参连", buff_ids=[9437])
    },
    {
        14873: 刻梦("刻梦", buff_ids=[23101])
    },
    {
        35982: Gain("争鸣", skill_ids=[38015]),
        30589: Gain("音彻", skill_ids=[40330], recipes=[(recipe_id, 1) for recipe_id in range(5836, 5841 + 1)])
    },
    {
        18712: Gain("云汉", buff_ids=[12576])
    },
    {
        30984: Gain("知止"),
        40743: Gain("崭芒", recipes=[(5922, 1)])
    },
    {
        34344: Gain("正律和鸣", buff_ids=[25997], skill_ids=[34676]),
        37287: Gain("响壑", recipes=[(5496, 1), (5583, 1)]),
        29071: Gain("不愧君", skill_ids=[29077])
    }
]
