from typing import Dict

from base.gain import Gain
from base.skill import Skill


class 青梅嗅(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (6234, 6554):
            skills[skill_id].skill_critical_strike += 1000
            skills[skill_id].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (6234, 6554):
            skills[skill_id].skill_critical_strike -= 1000
            skills[skill_id].skill_critical_power -= 102


class 惊寒(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[30524].skill_damage_addition += 154
        skills[6559].skill_damage_addition += 154

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[30524].skill_damage_addition -= 154
        skills[6559].skill_damage_addition -= 154


class 千里冰封(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2716].skill_critical_strike += 1000
        skills[2716].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2716].skill_critical_strike -= 1000
        skills[2716].skill_critical_power -= 102


TALENT_GAINS: Dict[int, Gain] = {
    6569: Gain("明妃"),
    5849: 青梅嗅("青梅嗅"),
    5869: 惊寒("惊寒"),
    5868: 千里冰封("千里冰封"),
    5852: Gain("新妆"),
    37316: Gain("芳姿畅音"),
    5864: Gain("枕上"),
    23935: Gain("广陵月"),
    34604: Gain("流玉"),
    22732: Gain("钗燕"),
    24995: Gain("盈袖"),
    24996: Gain("化冰"),
    14934: Gain("夜天"),
    34603: Gain("凝华")
}

TALENTS = [
    [6569, 5849],
    [5869],
    [5852],
    [37316],
    [5864],
    [23935],
    [34604],
    [22732],
    [24995],
    [24996],
    [14934],
    [34603]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
