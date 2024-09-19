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
            5827: Gain("白虹", recipes=[(4092, 3)]),
            17752: Gain("不善")
        },
        {
            5828: Gain("霜锋", recipes=[(1115, 3), (1216, 1)]),
            5823: Gain("心固"),
            17747: Gain("吐故纳新")
        },
        {
            22703: Gain("抱一"),
            33098: Gain("归衡"),
            5846: Gain("无形"),
            357: Gain("化三清")
        },
        {
            14837: Gain("规焉"),
            23614: Gain("归元"),
            21707: Gain("抱元"),
            370: Gain("八卦洞玄")
        },
        {
            5829: Gain("雨集"),
            5819: Gain("同尘"),
            14041: Gain("玄德"),
            5830: Gain("不移")
        },
        {
            5802: Gain("解牛"),
            18695: Gain("跬步", buff_ids=[-12550, -12551]),
            26683: Gain("北辰"),
            24942: Gain("厚亡")
        },
        {
            6798: Gain("有涯"),
            6481: Gain("雾外江山"),
            18694: Gain("万物", recipes=[(4464, 1)]),
            32411: Gain("正气")
        },
        {
            14834: Gain("抱阳"),
            5813: Gain("无我"),
            21712: Gain("羽化"),
            26684: Gain("若冲", recipes=[(2963, 1)]),
            34631: Gain("定迹")
        },
        {
            34580: Gain("归本"),
            18679: Gain("浮生"),
            18798: Gain("玄通"),
            6904: Gain("霜寒"),
            24953: Gain("大成")
        },
        {
            37387: Gain("悉归"),
            5844: Gain("心眼"),
            32412: Gain("星辰"),
            6796: Gain("临风"),
            24945: Gain("破势", buff_ids=[17918])
        },
        {
            18669: Gain("重光", recipes=[(recipe_id, 1) for recipe_id in (2593, 2594, 2595, 2596)]),
            14835: Gain("凶年"),
            30821: Gain("绝云"),
            14836: Gain("自化"),
            32413: Gain("流转")
        },
        {
            14598: 若水("若水"),
            14613: 固本("固本"),
            36099: Gain("际地蟠天"),
            23969: Gain("剑出鸿蒙"),
            24955: Gain("穹隆化生")
        }
    ]
}
