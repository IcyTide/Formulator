from typing import Dict

from base.gain import Gain
from base.recipe import MagicalShieldGainRecipe
from base.skill import Skill
from base.talent import Talent


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


TALENT_GAINS: Dict[int, Talent] = {
    14246: Talent("飞帆", [飞帆(skill_id=skill_id, skill_recipe=skill_id) for skill_id in (14067, 14299)]),
    35981: Talent("明津"),
    32485: Talent("弦风"),
    34341: Talent("连徽"),
    30562: Talent("流照"),
    14336: Talent("豪情"),
    14282: Talent("师襄", [师襄(-614, 14068, 14068)]),
    30984: Talent("知止"),
    14873: Talent("刻梦", [刻梦()]),
    35982: Talent("争鸣"),
    18712: Talent("云汉"),
    14350: Talent("参连"),
    34344: Talent("正律和鸣"),
    37287: Talent("响壑", [MagicalShieldGainRecipe(-410, 0, 14067)])
}

TALENTS = [
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
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
