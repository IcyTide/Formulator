from typing import Dict

from base.gain import Gain
from base.skill import Skill


class 飞帆(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (14227, 18859):
            skills[skill_id].attack_power_cof_gain *= 1.1

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (14227, 18859):
            skills[skill_id].attack_power_cof_gain /= 1.1


class 师襄(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[14100].skill_shield_gain -= 614

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[14100].skill_shield_gain += 614


class 刻梦(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[15076].skill_critical_strike += 1000
        skills[15076].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[15076].skill_critical_strike -= 1000
        skills[15076].skill_critical_power -= 102


TALENT_GAINS: Dict[int, Gain] = {
    14246: 飞帆("飞帆"),
    35981: Gain("明津"),
    32485: Gain("弦风"),
    30562: Gain("流照"),
    14336:  Gain("豪情"),
    14282: 师襄("师襄"),
    30984:  Gain("知止"),
    14873:  刻梦("刻梦"),
    35982:  Gain("争鸣"),
    18712:  Gain("云汉"),
    14350:  Gain("参连"),
    34344:  Gain("正律和鸣")
}

TALENTS = [
    [14246],
    [35981],
    [32485],
    [30562],
    [14336],
    [14282],
    [30984],
    [14873],
    [35982],
    [18712],
    [14350],
    [34344]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
