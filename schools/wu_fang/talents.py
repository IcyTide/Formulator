from typing import Dict

from base.attribute import Attribute
from base.gain import Gain
from base.skill import Skill


class 鸩羽(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[27557].skill_critical_strike += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[27557].skill_critical_strike -= 102


class 疾根(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[27560].tick += 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[27560].tick -= 1


TALENT_GAINS: Dict[int, Gain] = {
    28343: Gain("淮茵"),
    28344: 鸩羽("鸩羽"),
    28361: Gain("结草"),
    29498: Gain("灵荆"),
    29499: Gain("苦苛"),
    28410: Gain("坚阴"),
    28413: Gain("相使"),
    28419: Gain("凄骨"),
    28432: 疾根("疾根"),
    28433: Gain("紫伏"),
    28443: Gain("甘遂"),
    32896: Gain("应理与药")
}

TALENTS = [
    [28343],
    [28344],
    [28361],
    [29498],
    [29499],
    [28410],
    [28413],
    [28419],
    [28432],
    [28433],
    [28443],
    [32896]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
