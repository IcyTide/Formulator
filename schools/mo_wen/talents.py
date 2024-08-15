from typing import Dict

from base.gain import Gain
from base.recipe import MagicalShieldGainRecipe
from base.skill import Skill


class 飞帆(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id not in (14067, 14299):
            skill.channel_interval_extra *= 1.1

    def sub_skill(self, skill: Skill):
        if skill.skill_id not in (14067, 14299):
            skill.channel_interval_extra /= 1.1


class 师襄(MagicalShieldGainRecipe):
    def add_skill(self, skill: Skill):
        if skill.skill_id in (14100, 14101, 14102, 14511, 14512):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (14100, 14101, 14102, 14511, 14512):
            super().sub_skill(skill)


class 刻梦(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[14082].pet_buffs[(23101, 1)] = 1
        skills[14082].pet_count = 2

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[14082].pet_buffs.pop((23101, 1))
        skills[14082].pet_count = 1


TALENTS: Dict[int, Gain] = {
    14246: Gain("飞帆", [飞帆(skill_id=skill_id, recipe_type=skill_id) for skill_id in (14067, 14299)]),
    35981: Gain("明津"),
    32485: Gain("弦风"),
    34341: Gain("连徽"),
    30562: Gain("流照"),
    14336: Gain("豪情"),
    14282: Gain("师襄", [师襄(-614, 14068, 14068)]),
    30984: Gain("知止"),
    14873: Gain("刻梦", [刻梦()]),
    35982: Gain("争鸣"),
    18712: Gain("云汉"),
    14350: Gain("参连"),
    34344: Gain("正律和鸣"),
    37287: Gain("响壑", [MagicalShieldGainRecipe(-410, 0, 14067)])
}

TALENT_CHOICES = [
    [14246],
    [35981],
    [32485, 34341],
    [30562],
    [14336],
    [14282],
    [30984],
    [14873],
    [35982],
    [18712],
    [14350],
    [34344, 37287]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
