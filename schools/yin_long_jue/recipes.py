from typing import Dict, Tuple, Union

from base.recipe import Recipe
from general.recipes import *


class 乱天狼对静止目标增加10伤害(MoveStateDamageAdditionRecipe):
    value = 307


SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        4986: {}, 4987: {}, 4988: {},
        4996: {}, 4997: {},
        5001: {}, 5002: {},
        5004: {}, 5005: {}, 5006: {},
        5010: {}, 5011: {},
        5050: {}, 5051: {},
        5069: {}, 5070: {}, 5071: {},
        **{recipe_id: {} for recipe_id in range(4965, 4976 + 1)}, 4946: {}, 4947: {},
        **{recipe_id: {} for recipe_id in range(3154, 3166 + 1)},
        4950: {},
        5037: {}, 5038: {}, 5091: {}, 5092: {}, 17348: {}, 17324: {}
    },
    CriticalStrikeRecipe_200: {
        4983: {},
        5018: {},
        5063: {}
    },
    CriticalStrikeRecipe_300: {
        4984: {},
        4994: {},
        5019: {},
        5044: {},
        5046: {},
        5064: {}
    },
    CriticalStrikeRecipe_400: {
        4985: {},
        4995: {},
        5045: {},
        5047: {},
        5065: {}
    },
    CriticalStrikeRecipe_500: {
        5093: {}
    },
    CriticalStrikeRecipe_306: {
        17330: {}
    },
    乱天狼对静止目标增加10伤害: {
        4952: {}
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
    "星垂平野": {
        "增加伤害5%": 4988,
        "增加伤害4%": 4987,
        "增加会心4%": 4985,
        "增加伤害3%": 4986,
        "增加会心3%": 4984,
        "增加会心2%": 4983,
    },
    "金戈回澜": {
        "增加伤害5%": 4997,
        "增加伤害4%": 4996,
        "增加会心4%": 4995,
        "增加会心3%": 4994,
    },
    "乱天狼": {
        "增加伤害5%": 5002,
        "增加伤害4%": 5001,
        "增加会心4%": 5045,
        "增加会心3%": 5044,
    },
    "寂洪荒": {
        "增加伤害5%": 5006,
        "增加伤害4%": 5005,
        "增加伤害3%": 5004,
    },
    "斩无常": {
        "增加伤害5%": 5011,
        "增加伤害4%": 5010,
        "增加会心4%": 5047,
        "增加会心3%": 5046,
    },
    "幽冥窥月": {
        "增加伤害5%·1": 5050,
        "增加伤害5%·2": 5051,
        "增加会心3%": 5019,
        "增加会心2%": 5018,
    },
    "隐风雷": {
        "增加伤害5%": 5071,
        "增加伤害4%": 5070,
        "增加会心4%": 5065,
        "增加伤害3%": 5069,
        "增加会心3%": 5064,
        "增加会心2%": 5063,
    }
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
