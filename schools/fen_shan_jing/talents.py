from typing import Dict

from base.attribute import Attribute
from base.gain import Gain
from base.recipe import PhysicalCriticalRecipe
from base.talent import Talent
from base.skill import Skill


class 血魄(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[13040].post_buffs[(-1, 1)] += 25

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[13040].post_buffs[(-1, 1)] -= 25


class 蔑视(Gain):
    def add_attribute(self, attribute: Attribute):
        attribute.all_shield_ignore += 512

    def sub_attribute(self, attribute: Attribute):
        attribute.all_shield_ignore -= 512


TALENT_GAINS: Dict[int, Talent] = {
    13317: Talent("刀魂"),
    13090: Talent("绝返"),
    13087: Talent("分野", [PhysicalCriticalRecipe((1500, 200), 0, 13055)]),
    21281: Talent("血魄", [血魄()]),
    22897: Talent("锋鸣"),
    37239: Talent("麾远"),
    34912: Talent("业火麟光"),
    13126: Talent("恋战"),
    25203: Talent("扶阵"),
    36058: Talent("援戈"),
    36205: Talent("惊涌"),
    14838: Talent("蔑视", [蔑视()]),
    30769: Talent("阵云结晦")
}

TALENTS = [
    [13317],
    [13090],
    [13087],
    [21281],
    [22897],
    [37239],
    [34912],
    [13126, 25203],
    [36058],
    [36205],
    [14838],
    [30769]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
