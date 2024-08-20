from typing import Dict, Tuple, Union

from base.recipe import Recipe
from general.recipes import *


class 气剑增伤(PveAdditionRecipe):
    value = 1331


class 增加会心10会心后伤害20(NeutralCriticalRecipe):
    value = (1000, 102)


SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        24: {}, 25: {}, 26: {},
        97: {}, 98: {}, 99: {},
        1581: {}, 1582: {}, 1583: {},
        3253: {}, 2360: {}, 2361: {}, 2362: {}, 2363: {}, **{recipe_id: {} for recipe_id in range(4467, 4476 + 1)},
        (1116, 3): {}, (1115, 3): {}, 1216: {}, 2593: {}, 2594: {}, 2595: {}, 2596: {},
        (818, 2): {}, 4602: {}, 1520: {}, 1521: {}, 17300: {}
    },
    CriticalStrikeRecipe_200: {
        19: {},
        84: {},
        92: {}
    },
    CriticalStrikeRecipe_300: {
        20: {},
        85: {},
        93: {}
    },
    CriticalStrikeRecipe_400: {
        21: {},
        86: {},
        94: {}
    },
    CriticalStrikeRecipe_500: {
        1136: {}
    },
    CriticalStrikeRecipe_306: {
        17312: {}
    },
    气剑增伤: {
        5172: {}
    },
    增加会心10会心后伤害20: {
        (4092, 3): {}
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
    "两仪化形": {
        "增加伤害5%": 26,
        "增加伤害4%": 25,
        "增加会心4%": 21,
        "增加伤害3%": 24,
        "增加会心3%": 20,
        "增加会心2%": 19,
    },
    "四象轮回": {
        "增加会心4%": 86,
        "增加会心3%": 85,
        "增加会心2%": 84,
    },
    "太极无极": {
        "增加伤害20%": 99,
        "增加伤害15%·1": 98,
        "增加伤害15%·2": 97,
        "增加会心4%": 94,
        "增加会心3%": 93,
        "增加会心2%": 92,
    },
    "万世不竭": {
        "增加伤害5%": 1583,
        "增加伤害4%": 1582,
        "增加伤害3%": 1581
    }
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
