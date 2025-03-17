from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


class 相使(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[27555].pre_buffs = {20680: {1: 1}}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[27555].pre_buffs = {}


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            38631: Gain("连茹")
        },
        {
            28344: Gain("鸩羽", recipes=[(2549, 1)])
        },
        {
            40211: Gain("往馥")
        },
        {
            29498: Gain("灵荆")
        },
        {
            39661: Gain("逆势")
        },
        {
            40194: Gain("六微")
        },
        {
            28413: 相使("相使")
        },
        {
            28419: Gain("凄骨")
        },
        {
            38965: Gain("紫伏")
        },
        {
            36067: Gain("香繁饮露")
        },
        {
            28443: Gain("甘遂")
        },
        {
            28426: Gain("养荣")
        }
    ],
    1: [
        {
            101419: Gain("鬼门")
        },
        {
            101422: Gain("神莹")
        },
        {
            101423: Gain("济世")
        },
        {
            101370: Gain("苍棘缚地")
        }
    ]
}
