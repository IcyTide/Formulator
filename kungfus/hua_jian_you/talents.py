from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


class 钟灵(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[182].pre_buffs[28116] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[182].pre_buffs.pop(28116)


TALENTS: List[Dict[int, Gain]] = [
    {
        32477: Gain("雪中行")
    },
    {
        17510: Gain("倚天"),
        5751: Gain("定式黑白")
    },
    {
        26692: 钟灵("钟灵")
    },
    {
        5762: Gain("青歌", recipes=[(5497, 1)]),
        38954: Gain("焚玉")
    },
    {
        21744: Gain("折花")
    },
    {
        24912: Gain("丹鼎", recipes=[(4661, 1)])
    },
    {
        16855: Gain("清流")
    },
    {
        38972: Gain("青冠", attributes=dict(neutral_attack_power_gain=102, strain_gain=205))
    },
    {
        6682: Gain("流离"),
        26694: Gain("碎玉")
    },
    {
        30650: Gain("丹青")
    },
    {
        37267: Gain("墨海临源"),
        26669: Gain("故幽", recipes=[(recipe_id, 1) for recipe_id in (2439, 2440, 2441, 2442, 2443, 3151)])
    },
    {
        14643: Gain("涓流")
    }
]
