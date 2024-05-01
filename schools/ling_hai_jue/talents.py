from typing import Dict

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from base.skill import Skill


class 江汉(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[19819].skill_critical_strike += 1000
        skills[19819].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[19819].skill_critical_strike -= 1000
        skills[19819].skill_critical_power -= 102


class 扶桑(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[20016].skill_damage_addition += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[20016].skill_damage_addition -= 102


class 神降(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[20054].skill_critical_strike += 5000
        skills[20054].skill_critical_power += 512

    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[14029].activate = True

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[20054].skill_critical_strike -= 5000
        skills[20054].skill_critical_power -= 512

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[14029].activate = False


class 梦悠(Gain):
    def add_attribute(self, attribute: Attribute):
        attribute.all_shield_ignore += 307

    def sub_attribute(self, attribute: Attribute):
        attribute.all_shield_ignore -= 307


class 濯流(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[31250].skill_pve_addition += 1536

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[31250].skill_pve_addition -= 1536


TALENT_GAINS: Dict[int, Gain] = {
    20333: 江汉("江汉"),
    20335: 扶桑("扶桑"),
    20746: Gain("羽彰"),
    20348: Gain("清源"),
    30912: Gain("游仙"),
    25272: Gain("青冥"),
    20751: Gain("鸿轨"),
    25270: Gain("烟涛"),
    21293: Gain("溯徊"),
    20374: Gain("驰行"),
    20758: 神降("神降"),
    20747: 梦悠("梦悠"),
    20701: 濯流("濯流")
}

TALENTS = [
    [20333],
    [20335],
    [20746],
    [20348],
    [30912],
    [25272],
    [20751],
    [25270],
    [21293],
    [20374, 20758],
    [20747],
    [20701]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
