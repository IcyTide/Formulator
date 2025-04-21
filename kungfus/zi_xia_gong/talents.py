from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


class 固本(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2681].post_buffs[2757] = {3: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2681].post_buffs[2757] = {1: 1}


TALENTS: List[Dict[int, Gain]] = [
    {
        5827: Gain("白虹", recipes=[(4092, 3)])
    },
    {
        5823: Gain("心固"),
    },
    {
        5846: Gain("无形", skill_ids=list(range(6091, 6100 + 1))),
        357: Gain("化三清"),
        33098: Gain("归衡")
    },
    {
        30821: Gain("绝云", skill_ids=[40158])
    },
    {
        5819: Gain("同尘", buff_ids=[9966])
    },
    {
        18695: Gain("跬步", buff_ids=list(range(12779, 12783 + 1)) + [-12550, -12551])
    },
    {
        32411: Gain("正气", skill_ids=[36438])
    },
    {
        14834: Gain("抱阳")
    },
    {
        18679: Gain("浮生", skill_ids=[18670])
    },
    {
        24945: Gain("破势", buff_ids=[17918])
    },
    {
        23614: Gain("归元")
    },
    {
        14613: 固本("固本")
    }
]
