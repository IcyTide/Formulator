from typing import Dict, Tuple, Union

from base.recipe import Recipe
from general.recipes import *


class 上将军印无视外防(PhysicalShieldGainRecipe):
    value = -205

    def add_skill(self, skill: Skill):
        if skill.skill_id in (16800, 16801, 16802, 16803, 16804, 17043, 19423, 19424):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (16800, 16801, 16802, 16803, 16804, 17043, 19423, 19424):
            super().sub_skill(skill)


class 新冥鼓无视防御(PhysicalShieldGainRecipe):
    value = -512

    def add_skill(self, skill: Skill):
        if skill.skill_id in (16758, 16759, 16760, 16382, 20991):
            super().add_skill(skill)

    def add_skills(self, skills: Dict[int, Skill]):
        skills[32823].physical_shield_gain = [self.value, 0, 0, self.value]
        skills[37458].physical_shield_gain = self.value
        return super().add_skills(skills)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (16758, 16759, 16760, 16382, 20991):
            super().sub_skill(skill)

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[32823].physical_shield_gain = 0
        skills[37458].physical_shield_gain = 0
        super().sub_skills(skills)


class 绝期_闹须弥增加持续伤害(ChannelIntervalRecipe):
    value = 1.7


SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        4127: dict(clone_id=16629), 4128: dict(clone_id=16629), 4129: dict(clone_id=16629),
        4143: {}, 4144: {}, 4145: {},
        4151: {}, 4152: {}, 4153: {},
        4167: {}, 4168: {},
        4183: {}, 4184: {}, 4185: {},
        4374: {}, 4375: {}, 4376: {},
        2946: {}, 2947: {}, 2948: {},
        3251: {},
        4290: {}, 4291: {}, 4294: {}, 4295: {},
        17374: {}
    },
    CriticalStrikeRecipe_200: {
        4124: dict(clone_id=16629),
        4140: {},
        4148: {},
        4164: {},
        4180: {},
        4371: {},
    },
    CriticalStrikeRecipe_300: {
        4125: dict(clone_id=16629),
        4141: {},
        4149: {},
        4165: {},
        4181: {},
        4372: {}
    },
    CriticalStrikeRecipe_400: {
        4126: dict(clone_id=16629),
        4142: {},
        4150: {},
        4166: {},
        4182: {},
        4373: {}
    },
    CriticalStrikeRecipe_500: {
        4296: {}, 4297: {}
    },
    CriticalStrikeRecipe_306: {
        17375: {}
    },
    上将军印无视外防: {
        4298: {}
    },
    新冥鼓无视防御: {
        2510: {}, 2511: {}
    },
    绝期_闹须弥增加持续伤害: {
        4319: {}, 2833: {}
    }
}
RECIPES: Dict[Tuple[int, int], Recipe] = {**GENERAL_RECIPES}
for recipe_class, recipes in SCHOOL_RECIPES.items():
    for recipe_key, attrs in recipes.items():
        if not isinstance(recipe_key, tuple):
            recipe_key = (recipe_key, 1)
        recipe = recipe_class(*recipe_key)
        for attr, value in attrs.items():
            setattr(recipe, attr, value)
        recipe.set_asset()
        RECIPES[recipe_key] = recipe
RECIPE_CHOICES: Dict[str, Dict[str, int]] = {
    "雷走风切": {
        "增加伤害5%": 4129,
        "增加伤害4%": 4128,
        "增加会心4%": 4126,
        "增加伤害3%": 4127,
        "增加会心3%": 4125,
        "增加会心2%": 4124,
    },
    "项王击鼎": {
        "增加伤害5%": 4145,
        "增加伤害4%": 4144,
        "增加会心4%": 4142,
        "增加伤害3%": 4143,
        "增加会心3%": 4141,
        "增加会心2%": 4140,
    },
    "破釜沉舟": {
        "增加伤害5%": 4153,
        "增加伤害4%": 4152,
        "增加会心4%": 4150,
        "增加伤害3%": 4151,
        "增加会心3%": 4149,
        "增加会心2%": 4148,
    },
    "刀啸风吟": {
        "增加伤害5%": 4168,
        "增加伤害4%": 4167,
        "增加会心4%": 4166,
        "增加会心3%": 4165,
        "增加会心2%": 4164,
    },
    "擒龙六斩": {
        "增加伤害5%": 4185,
        "增加伤害4%": 4184,
        "增加会心4%": 4182,
        "增加伤害3%": 4183,
        "增加会心3%": 4181,
        "增加会心2%": 4180,
    },
    "上将军印": {
        "增加伤害4%": 4376,
        "增加会心4%": 4373,
        "增加伤害3%": 4375,
        "增加会心3%": 4372,
        "增加会心2%": 4371,
        "增加伤害2%": 4374,
    },
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
