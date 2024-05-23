from typing import Dict

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from base.skill import Skill


class 明心(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (24676, 24558, 24675, 24677):
            skills[skill_id].skill_critical_strike += 1000
            skills[skill_id].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (24676, 24558, 24675, 24677):
            skills[skill_id].skill_critical_strike -= 1000
            skills[skill_id].skill_critical_power -= 102


class 正夏(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (24676, 24558, 24675, 24677):
            skills[skill_id].skill_damage_addition += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (24676, 24558, 24675, 24677):
            skills[skill_id].skill_damage_addition -= 102


class 望旗(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (24813, 24811, 24812, 24814):
            skills[skill_id].skill_damage_addition += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (24813, 24811, 24812, 24814):
            skills[skill_id].skill_damage_addition -= 102


class 重山(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (24676, 24813, 24823, 34683):
            skills[skill_id].attack_power_cof_gain *= 1.286

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (24676, 24813, 24823, 34683):
            skills[skill_id].attack_power_cof_gain /= 1.286


class 神元(Gain):
    def add_attribute(self, attribute: Attribute):
        attribute.spunk_gain += 102

    def sub_attribute(self, attribute: Attribute):
        attribute.spunk_gain -= 102


TALENT_GAINS: Dict[int, Gain] = {
    24936: Gain("水盈"),
    24925: 正夏("正夏"),
    24930: 明心("明心"),
    24932: Gain("天网"),
    24934: 望旗("望旗"),
    25034: Gain("顺祝"),
    32791: Gain("列宿游"),
    24994: Gain("龙回首"),
    24983: 重山("重山"),
    25025: Gain("地遁"),
    25072: Gain("鬼遁"),
    25137: Gain("堪卜"),
    25368: Gain("亘天"),
    37456: Gain("追叙"),
    25378: Gain("连断"),
    25066: 神元("神元"),
    25085: Gain("荧入白"),
    25379: Gain("征凶"),
    25173: Gain("灵器"),
    37505: Gain("镇星入舆")
}

TALENTS = [
    [24936, 24925, 24930],
    [24932, 24934],
    [25034],
    [32791, 24994],
    [24983, 25025],
    [25072, 25137],
    [25368, 37456],
    [25378, 25066],
    [25085],
    [25379],
    [25173],
    [37505]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
