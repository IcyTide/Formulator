from typing import Dict, Tuple, Union

from base.recipe import Recipe
from general.recipes import *


class 万灵山庄_饮羽簇人偶图绝章(PveAdditionRecipe):
    value = 154


class 素矰_贯穿10伤害(ChannelIntervalRecipe):
    value = 1.05

    def add_skill(self, skill: Skill):
        if skill.skill_id == 35771:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 35771:
            super().sub_skill(skill)


class 彤弓_劲风簇10双会(PhysicalCriticalRecipe):
    value = (1000, 102)

    def add_skill(self, skill: Skill):
        if skill.skill_id == 35866:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 35866:
            super().sub_skill(skill)


class 贯侯_标鹄伤害增加(PveAdditionRecipe):
    value = 205

    def add_skill(self, skill: Skill):
        if skill.skill_id == 36157:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 36157:
            super().sub_skill(skill)


SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        5408: {}, 5409: {},
        5416: {}, 5417: {},
        5438: {}, 5461: {}, 5462: {}, 17470: {}
    },
    CriticalStrikeRecipe_300: {
        5394: {},
        5414: {}
    },
    CriticalStrikeRecipe_400: {
        5407: {},
        5415: {}
    },
    CriticalStrikeRecipe_500: {
        5463: {}
    },
    CriticalStrikeRecipe_306: {
        17471: {}
    },
    万灵山庄_饮羽簇人偶图绝章: {
        5467: {}
    },
    素矰_贯穿10伤害: {
        5373: {}
    },
    彤弓_劲风簇10双会: {
        5369: {}
    },
    贯侯_标鹄伤害增加: {
        5422: {}
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
    "劲风簇": {
        "增加会心4%": 5407,
        "增加伤害3%": 5409,
        "增加会心3%": 5394,
        "增加伤害2%": 5408,
    },
    "饮羽簇": {
        "增加伤害15%": 5467,
        "增加伤害3%": 5417,
        "增加伤害2%": 5416,
        "增加会心4%": 5415,
        "增加会心3%": 5414,
    },
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
