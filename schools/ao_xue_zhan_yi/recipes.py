from typing import Dict, Tuple

from base.recipe import Recipe, DotRecipe
from general.recipes import *


class 增加会心10(PhysicalCriticalRecipe):
    value = (1000, 102)


class 流血伤害提高10(ChannelIntervalRecipe):
    value = 1.12

    def add_skill(self, skill: Skill):
        if skill.skill_id in (18591, 15000, 18610, 26773, 401):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (18591, 15000, 18610, 26773, 401):
            super().sub_skill(skill)


class 天策流血20(ChannelIntervalRecipe):
    value = 1.2

    def add_skill(self, skill: Skill):
        if skill.skill_id in (18591, 15000, 18610, 26773, 401):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (18591, 15000, 18610, 26773, 401):
            super().sub_skill(skill)


SCHOOL_RECIPES: Dict[type(Recipe), Dict[int, dict]] = {
    DotRecipe: {
        -132: {}, -153: {}
    },
    SkillRecipe: {
        338: {}, 339: {},
        345: {}, 346: {},
        356: {}, 361: {}, 362: {},
        369: {}, 370: {},
        398: {}, 399: {},
        1557: {}, 1558: {}, 1559: {},
        **{(recipe_id, i + 1): {} for recipe_id in (4504, 4505, 4506, 4507) for i in range(5)},
        (4038, 3): {},
        (817, 2): {}, 1508: {}, 1509: {}, 17362: {},
    },
    增加会心10: {
        1224: {}, 1225: {},
    },
    流血伤害提高10: {
        4686: {}, 4687: {}, 4688: {}, 4689: {}
    },
    天策流血20: {
        3257: {}
    },
    CriticalStrikeRecipe_200: {
        334: {},
        357: {},
        367: {}
    },
    CriticalStrikeRecipe_300: {
        335: {},
        358: {},
        368: {}
    },
    CriticalStrikeRecipe_400: {
        355: {},
    },
    CriticalStrikeRecipe_500: {
        1133: {}
    },
    CriticalStrikeRecipe_306: {
        17367: {}
    }
}
RECIPES: Dict[Tuple[int, int], Recipe] = {**GENERAL_RECIPES}
for recipe_class, recipes in SCHOOL_RECIPES.items():
    for recipe_key, attrs in recipes.items():
        recipe_key = recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        recipe = recipe_class(*recipe_key)
        for attr, value in attrs.items():
            setattr(recipe, attr, value)
        recipe.set_asset()
        RECIPES[recipe_key] = recipe
RECIPE_CHOICES: Dict[str, Dict[str, int]] = {
    "穿云": {
        "增加伤害4%": 339,
        "增加伤害3%": 338,
        "增加会心3%": 335,
        "增加会心2%": 334
    },
    "断魂刺": {
        "增加伤害4%": 346,
        "增加伤害3%": 345,
    },
    "龙牙": {
        "增加伤害5%": 356,
        "增加伤害4%": 362,
        "增加会心4%": 355,
        "增加伤害3%": 361,
        "增加会心3%": 358,
        "增加会心2%": 357
    },
    "灭": {
        "增加伤害4%": 370,
        "增加伤害3%": 369,
        "增加会心3%": 367,
        "增加会心2%": 368
    },
    "突": {
        "增加伤害4%": 398,
        "增加伤害3%": 399
    },
    "龙吟": {
        "增加伤害5%": 1559,
        "增加伤害4%": 1558,
        "增加伤害3%": 1557
    },
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
