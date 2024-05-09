from typing import Dict

from base.gain import Gain
from base.skill import Skill


class 心固(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[32408].skill_critical_strike += 1000
        skills[32408].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[32408].skill_critical_strike -= 1000
        skills[32408].skill_critical_power -= 102


class 无意(Gain):

    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (390, 391, 392, 393, 394):
            skills[skill_id].skill_critical_strike += 1000
            skills[skill_id].skill_critical_power += 307

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (390, 391, 392, 393, 394):
            skills[skill_id].skill_critical_strike -= 1000
            skills[skill_id].skill_critical_power -= 307


class 裂云(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[748].max_stack += 2

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[748].max_stack -= 2


class 虚极(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[748].attack_power_cof_gain *= 1.2

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[748].attack_power_cof_gain /= 1.2


TALENT_GAINS: Dict[int, Gain] = {
    5807: 心固("心固"),
    32407: Gain("环月"),
    5800: Gain("白虹"),
    357: Gain("化三清"),
    5818: 无意("无意"),
    21812: Gain("云中剑"),
    17742: Gain("风逝"),
    5821: Gain("叠刃"),
    6481: Gain("雾外江山"),
    21725: Gain("长生"),
    24962: 裂云("裂云"),
    18799: Gain("故长"),
    34656: Gain("剑入"),
    14832: 虚极("虚极"),
    14833: Gain("玄门"),
}

TALENTS = [
    [5807],
    [32407],
    [5800, 357],
    [5818, 21812],
    [17742],
    [5821],
    [6481, 21725],
    [24962],
    [18799],
    [34656],
    [14832],
    [14833]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
