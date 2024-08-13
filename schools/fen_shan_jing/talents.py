from typing import Dict

from base.attribute import Attribute
from base.gain import Gain, Gains
from base.recipe import PhysicalCriticalRecipe
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


TALENT_GAINS: Dict[int, Gains] = {
    13317: Gains("刀魂"),
    13090: Gains("绝返"),
    13087: Gains("分野", [PhysicalCriticalRecipe((1500, 200), 0, 13055)]),
    21281: Gains("血魄", [血魄()]),
    22897: Gains("锋鸣"),
    37239: Gains("麾远"),
    34912: Gains("业火麟光"),
    13126: Gains("恋战"),
    25203: Gains("扶阵"),
    36058: Gains("援戈"),
    36205: Gains("惊涌"),
    14838: Gains("蔑视", [蔑视()]),
    30769: Gains("阵云结晦"),
    32619: Gains("祭血关山")
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
    [30769, 32619]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
