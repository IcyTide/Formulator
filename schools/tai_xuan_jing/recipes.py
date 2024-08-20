from typing import Dict, Tuple, Union

from base.recipe import Recipe
from general.recipes import *


class 山艮状态伤害技能系数提高叠1(ChannelIntervalRecipe):
    value = 1.074

    def add_skill(self, skill: Skill):
        if skill.skill_id in (24823, 24676, 24813, 34683):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (24823, 24676, 24813, 34683):
            super().sub_skill(skill)


class 山艮状态伤害技能系数提高叠2(ChannelIntervalRecipe):
    value = 1.14815

    def add_skill(self, skill: Skill):
        if skill.skill_id in (24823, 24676, 24813, 34683):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (24823, 24676, 24813, 34683):
            super().sub_skill(skill)


class 山艮状态伤害技能系数提高叠3(ChannelIntervalRecipe):
    value = 1.2223

    def add_skill(self, skill: Skill):
        if skill.skill_id in (24823, 24676, 24813, 34683):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (24823, 24676, 24813, 34683):
            super().sub_skill(skill)


class 临会心会效提高(NeutralCriticalRecipe):
    value = (1000, 102)


class 山艮状态伤害技能系数提高(ChannelIntervalRecipe):
    value = 1.286

    def add_skill(self, skill: Skill):
        if skill.skill_id in (24823, 24676, 24813, 34683):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (24823, 24676, 24813, 34683):
            super().sub_skill(skill)


SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        5241: {}, 5242: {}, 5279: {},
        5246: {}, 5247: {}, 5280: {},
        5274: {}, 5275: {},
        5299: {}, 5300: {}, 5301: {},
        5166: {}, 5170: {},
        5321: {}, 5322: {}, 5325: {}, 5326: {}, 17414: {}
    },
    CriticalStrikeRecipe_200: {
        5165: {},
        5250: {},
    },
    CriticalStrikeRecipe_300: {
        5240: {},
        5244: {},
        5251: {},
        5272: {},
    },
    CriticalStrikeRecipe_400: {
        5245: {},
        5252: {},
        5273: {},
        5278: {},
    },
    CriticalStrikeRecipe_500: {
        5327: {}
    },
    CriticalStrikeRecipe_306: {
        17415: {}
    },
    山艮状态伤害技能系数提高叠1: {
        5548: {}, 5549: {}, 5550: {}
    },
    山艮状态伤害技能系数提高叠2: {
        5551: {}, 5552: {}, 5553: {}
    },
    山艮状态伤害技能系数提高叠3: {
        5554: {}, 5555: {}, 5556: {}
    },
    临会心会效提高: {
        5167: {}
    },
    山艮状态伤害技能系数提高: {
        5179: {}, 5180: {}, 5181: {}
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
    "三星临": {
        "增加伤害5%": 5279,
        "增加伤害4%": 5242,
        "增加会心4%": 5278,
        "增加伤害3%": 5241,
        "增加会心3%": 5240,
        "增加会心2%": 5165,
    },
    "兵主逆": {
        "增加伤害5%": 5247,
        "增加伤害4%": 5246,
        "增加会心4%": 5245,
        "增加伤害3%": 5280,
        "增加会心3%": 5244,
    },
    "天斗旋": {
        "增加伤害5%": 5301,
        "增加伤害4%": 5300,
        "增加会心4%": 5252,
        "增加伤害3%": 5299,
        "增加会心3%": 5251,
        "增加会心2%": 5250,
    },
    "鬼星开穴": {
        "增加伤害5%": 5275,
        "增加伤害4%": 5274,
        "增加会心4%": 5273,
        "增加会心3%": 5272,
    }
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
