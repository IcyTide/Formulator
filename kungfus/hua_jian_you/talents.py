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
        17510: Gain("倚天", buff_ids=[11809])
    },
    {
        26692: 钟灵("钟灵", buff_ids=[28116])
    },
    {
        5762: Gain("青歌", recipes=[(5497, 1)]),
        38954: Gain("焚玉", skill_ids=[38955])
    },
    {
        21744: Gain("折花", skill_ids=[32501, 601])
    },
    {
        24912: Gain("丹鼎", recipes=[(4661, 1)])
    },
    {
        16855: Gain("清流", skill_ids=[18722])
    },
    {
        38972: Gain("青冠", attributes=dict(neutral_attack_power_gain=102, strain_gain=205))
    },
    {
        6682: Gain("流离")
    },
    {
        30650: Gain("丹青", skill_ids=[32629, 30648, 32630])
    },
    {
        37267: Gain("墨海临源", skill_ids=[37270])
    },
    {
        14643: Gain("涓流", buff_ids=[-9722], skill_ids=[14644])
    }
]
