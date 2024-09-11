from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


class 固本(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2681].post_buffs.pop(2757)
        skills[2681].post_buffs[2757] = {3: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2681].post_buffs.pop(2757)
        skills[2681].post_buffs[2757] = {1: 1}


class 若水(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2681].post_buffs.pop(2757)
        skills[2681].post_buffs[2757] = {2: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2681].post_buffs.pop(2757)
        skills[2681].post_buffs[2757] = {1: 1}


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            5840: Gain("雾锁", recipes=[(1116, 3)]),
            5827: Gain("白虹", recipes=[(4092, 3)])
        },
        {
            5823: Gain("心固"),
            5828: Gain("霜锋", recipes=[(1115, 3), (1216, 1)])
        },
        {
            357: Gain("化三清"),
            5846: Gain("无形")
        },
        {
            23614: Gain("归元")
        },
        {
            5819: Gain("同尘")
        },
        {
            18695: Gain("跬步", buff_ids=[-12550, -12551])
        },
        {
            32411: Gain("正气")
        },
        {
            14834: Gain("抱阳")
        },
        {
            18679: Gain("浮生")
        },
        {
            24945: Gain("破势", buff_ids=[17918])
        },
        {
            18669: Gain("重光", recipes=[(recipe_id, 1) for recipe_id in (2593, 2594, 2595, 2596)])
        },
        {
            14613: 固本("固本"),
            14598: 若水("若水")
        }
    ],
    1: []
}
