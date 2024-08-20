from typing import Dict, Tuple, Union

from base.recipe import Recipe
from general.recipes import *


class 布泽80非侠士(PveAdditionRecipe):
    value = 820


class 守缺10会心会效(SolarCriticalRecipe):
    value = (1000, 102)


class 横扫10会心会效(SolarCriticalRecipe):
    value = (1000, 205)


class 拿云委托无视目标50内防(MagicalShieldGainRecipe):
    value = -614

    def add_skill(self, skill: Skill):
        if skill.skill_id in (
                3833, 3842, 3845, 3836, 3843, 3846, 3839, 3844, 3847, 13681, 13682, 13683, 13684, 13685, 13686, 3848,
                3849, 3850, 6787, 3816, 3815, 3814, 2866, 17642, 17641):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (
                3833, 3842, 3845, 3836, 3843, 3846, 3839, 3844, 3847, 13681, 13682, 13683, 13684, 13685, 13686, 3848,
                3849, 3850, 6787, 3816, 3815, 3814, 2866, 17642, 17641):
            super().sub_skill(skill)


SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        233: {}, 234: {}, 235: {},
        259: {},
        268: {}, 269: {}, 270: {},
        287: {}, 288: {}, 289: {},
        295: {}, 296: {}, 297: {},
        1645: {}, 1646: {}, 1647: {},
        2862: {},
        (959, 3): {},
        (818, 5): {}, 1147: {}, 1512: {}, 1513: {}, 17351: {}
    },
    CriticalStrikeRecipe_200: {
        285: {},
        290: {},
    },
    CriticalStrikeRecipe_300: {
        286: {},
        291: {},
    },
    CriticalStrikeRecipe_400: {
        281: {},
        292: {},
    },
    CriticalStrikeRecipe_500: {
        1139: {}
    },
    CriticalStrikeRecipe_306: {
        17352: {}
    },
    布泽80非侠士: {
        5543: {}, 5544: {}, 5564: {}, 5568: {}
    },
    守缺10会心会效: {
        2299: {}
    },
    横扫10会心会效: {
        5157: {}
    },
    拿云委托无视目标50内防: {
        2300: {}, 2301: {}, 5096: {}, 5545: {}
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
    "捕风式": {
        "增加伤害15%": 235,
        "增加伤害10%·1": 233,
        "增加伤害10%·2": 234
    },
    "横扫六合": {
        "增加伤害50%": 259,
    },
    "普渡四方": {
        "增加伤害5%": 270,
        "增加伤害4%": 269,
        "增加伤害3%": 268,
    },
    "守缺式": {
        "增加伤害5%": 289,
        "增加伤害4%": 288,
        "增加会心4%": 281,
        "增加伤害3%": 287,
        "增加会心3%": 286,
        "增加会心2%": 285,
    },
    "韦陀献杵": {
        "增加伤害5%": 297,
        "增加伤害4%": 296,
        "增加会心4%": 292,
        "增加伤害3%": 295,
        "增加会心3%": 291,
        "增加会心2%": 290,
    },
    "拿云式": {
        "增加伤害5%": 1647,
        "增加伤害4%": 1646,
        "增加伤害3%": 1645
    }
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
