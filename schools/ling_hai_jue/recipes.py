from typing import Dict, Tuple, Union

from base.recipe import Recipe
from general.recipes import *


class 神降_增加会心20(PhysicalCriticalRecipe):
    value = (1000, 102)


class 神降_增加会心40(PhysicalCriticalRecipe):
    value = (2000, 205)


class 神降_增加会心60(PhysicalCriticalRecipe):
    value = (3000, 307)


class 神降_增加会心80(PhysicalCriticalRecipe):
    value = (4000, 410)


class 神降_增加会心100(PhysicalCriticalRecipe):
    value = (5000, 512)


class 木落双会(PhysicalCriticalRecipe):
    value = (1000, 102)


class 鸟风车非侠士增伤(PveAdditionRecipe):
    value = 1536


SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        4717: {}, 4718: {}, 4719: {},
        4729: {}, 4730: {}, 4731: {},
        4742: {}, 4743: {}, 4744: {},
        4749: {}, 4750: {}, 4751: {},
        4792: {}, 4793: {}, 4794: {},
        4789: {}, 4790: {}, 4791: {}, **{(17477, i + 1): {} for i in range(3)},
        4691: {}, 4762: {}, 4694: {},
        4816: {}, 4817: {}, 4818: {}, 4819: {}, 17409: {}
    },
    CriticalStrikeRecipe_200: {
        2478: {},
        4714: {},
        4726: {},
        4739: {},
        4746: {},
        4795: {},
    },
    CriticalStrikeRecipe_300: {
        2479: {},
        4715: {},
        4727: {},
        4740: {},
        4747: {},
        4796: {},
    },
    CriticalStrikeRecipe_400: {
        2480: {},
        4716: {},
        4728: {},
        4741: {},
        4748: {},
        4797: {},
    },
    CriticalStrikeRecipe_500: {
        4820: {}, 4821: {}
    },
    CriticalStrikeRecipe_306: {
        17410: {}
    },
    神降_增加会心20: {
        4784: {}
    },
    神降_增加会心40: {
        4785: {}
    },
    神降_增加会心60: {
        4786: {}
    },
    神降_增加会心80: {
        4787: {}
    },
    神降_增加会心100: {
        4788: {}
    },
    木落双会: {
        5426: {}
    },
    鸟风车非侠士增伤: {
        3270: {}
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
    "浮游天地": {
        "增加会心4%": 2480,
        "增加会心3%": 2479,
        "增加会心2%": 2478,
    },
    "击水三千": {
        "增加伤害5%": 4719,
        "增加伤害4%": 4718,
        "增加会心4%": 4716,
        "增加伤害3%": 4717,
        "增加会心3%": 4715,
        "增加会心2%": 4714,
    },
    "木落雁归": {
        "增加伤害5%": 4731,
        "增加伤害4%": 4730,
        "增加会心4%": 4728,
        "增加伤害3%": 4729,
        "增加会心3%": 4727,
        "增加会心2%": 4726,
    },
    "翼绝云天": {
        "增加伤害5%": 4744,
        "增加伤害4%": 4743,
        "增加会心4%": 4741,
        "增加伤害3%": 4742,
        "增加会心3%": 4740,
        "增加会心2%": 4739,
    },
    "振翅图南": {
        "增加伤害5%": 4751,
        "增加伤害4%": 4750,
        "增加会心4%": 4748,
        "增加伤害3%": 4749,
        "增加会心3%": 4747,
        "增加会心2%": 4746,
    },
    "海运南冥": {
        "增加伤害4%": 4794,
        "增加伤害3%": 4793,
        "增加伤害2%": 4792,
        "增加会心4%": 4797,
        "增加会心3%": 4796,
        "增加会心2%": 4795,
    },
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
