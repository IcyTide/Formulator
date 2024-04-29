from typing import Dict

from base.attribute import Attribute
from base.gain import Gain
from base.skill import Skill


class 彤弓(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[35866].skill_critical_strike += 102
        skills[35866].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[35866].skill_critical_strike -= 102
        skills[35866].skill_critical_power -= 102


class 素矰(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[26856].attack_power_cof_gain += 0.05

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[26856].attack_power_cof_gain -= 0.05


class 孰湖(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (36056, 36057, 36111, 36112, 36113, 36114):
            skills[skill_id].skill_damage_addition += 62

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (36056, 36057, 36111, 36112, 36113, 36114):
            skills[skill_id].skill_damage_addition -= 62


class 桑柘(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[35771].tick += 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[35771].tick -= 1


class 卢令(Gain):
    def add_attribute(self, attribute: Attribute):
        attribute.agility_gain += 102

    def sub_attribute(self, attribute: Attribute):
        attribute.agility_gain -= 102


class 贯侯(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[36157].skill_pve_addition += 205

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[36157].skill_pve_addition -= 205


TALENT_GAINS: Dict[int, Gain] = {
    35715: 素矰("素矰"),
    35714: 彤弓("彤弓"),
    35718: Gain("棘矢"),
    35719: 孰湖("孰湖"),
    35721: Gain("襄尺"),
    35725: Gain("长右"),
    35729: Gain("鹿蜀"),
    35736: 桑柘("桑柘"),
    35733: Gain("诸怀"),
    35737: Gain("于狩"),
    35745: 卢令("卢令"),
    35749: Gain("托月"),
    35751: Gain("佩弦"),
    35754: Gain("丛云隐月"),
    35757: 贯侯("贯侯"),
    35764: Gain("朝仪万汇"),
    35761: Gain("朱厌")
}

TALENTS = [
    [35715, 35714],
    [35718, 35719],
    [35721],
    [35725],
    [35729],
    [35736, 35733],
    [35737],
    [35745],
    [35749],
    [35751, 35754],
    [35757],
    [35764, 35761]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
