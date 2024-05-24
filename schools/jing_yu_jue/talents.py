from typing import Dict

from base.gain import Gain
from base.skill import Skill


class 迅电流光(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (3095, 37504):
            skills[skill_id].skill_critical_strike += 1000
            skills[skill_id].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (3095, 37504):
            skills[skill_id].skill_critical_strike -= 1000
            skills[skill_id].skill_critical_power -= 102


class 穿林打叶(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2237].interval = 32
        skills[2237].tick = 11

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2237].interval = 48
        skills[2237].tick = 6 + 1


class 妙手连环(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[6920].skill_shield_gain -= 512

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[6920].skill_shield_gain += 512


class 逐一击破(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in ():
            skills[skill_id].skill_damage_addition += 103 + 103

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in ():
            skills[skill_id].skill_damage_addition += 103 + 103


TALENT_GAINS: Dict[int, Gain] = {
    6437: 迅电流光("迅电流光"),
    6473: Gain("千里无痕"),
    28366: Gain("寒江夜雨"),
    21724: Gain("掠影穹苍"),
    37324: Gain("蹑景追风"),
    6451: Gain("聚精凝神"),
    14851: Gain("逐一击破"),
    28903: 穿林打叶("穿林打叶"),
    6461: Gain("秋风散影"),
    37325: Gain("牢甲利兵"),
    14850: 妙手连环("妙手连环"),
    18672: Gain("百里追魂")
}

TALENTS = [
    [6437],
    [6473],
    [28366],
    [21724],
    [37324],
    [6451],
    [14851],
    [28903],
    [6461],
    [37325],
    [14850],
    [18672]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
