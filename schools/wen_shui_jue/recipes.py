from typing import Dict, Tuple, Union

from base.recipe import Recipe
from general.recipes import *


class 提高10会心几率(PhysicalCriticalRecipe):
    value = (1000, 102)


SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        546: {}, 547: {}, 548: {},
        555: {}, 556: {}, 557: {},
        562: {}, 563: {}, 564: {},
        569: {}, 570: {}, 571: {},
        579: {}, 580: {}, 581: {},
        583: dict(clone_id=18333), 584: dict(clone_id=18333), 585: dict(clone_id=18333),
        596: {}, 597: {}, 598: {},
        1565: {}, 1566: {}, 1567: {},
        1573: {}, 1574: {}, 1575: {},
        4880: {}, 2348: {}, 2883: {}, 2882: {}, 2817: {}, 2818: {}, 2819: {}, 2820: {}, 2821: {}, 3280: {}, 3281: {},
        3282: {}, 5306: {},
        (818, 6): {}, 4347: {}, 1536: {}, 1537: {}, 1538: {}, 1539: {}, 17368: {}
    },
    CriticalStrikeRecipe_200: {
        545: {},
        552: {},
        560: {},
        588: dict(clone_id=18333),
        594: {},
        1568: {},
        1576: {}
    },
    CriticalStrikeRecipe_300: {
        553: {},
        561: {},
        574: {},
        582: {},
        589: dict(clone_id=18333),
        595: {},
    },
    CriticalStrikeRecipe_400: {
        554: {},
    },
    CriticalStrikeRecipe_500: {
        1141: {}, 1142: {}
    },
    CriticalStrikeRecipe_306: {
        17369: {}
    },
    提高10会心几率: {
        1235: {}, 1236: {}
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
    "平湖断月": {
        "增加伤害5%": 548,
        "增加伤害4%": 547,
        "增加伤害3%": 546,
        "增加会心2%": 545,
    },
    "黄龙吐翠": {
        "增加伤害5%": 557,
        "增加伤害4%": 556,
        "增加会心4%": 554,
        "增加伤害3%": 555,
        "增加会心3%": 553,
        "增加会心2%": 552,
    },
    "九溪弥烟": {
        "增加伤害5%": 564,
        "增加伤害4%": 563,
        "增加伤害3%": 562,
        "增加会心3%": 561,
        "增加会心2%": 560,
    },
    "云飞玉皇": {
        "增加伤害4%": 571,
        "增加伤害3%": 570,
        "增加会心3%": 574,
        "增加伤害2%": 569,
    },
    "夕照雷峰": {
        "增加伤害4%": 581,
        "增加伤害3%": 580,
        "增加会心3%": 582,
        "增加伤害2%": 579,
    },
    "风来吴山": {
        "增加伤害4%": 585,
        "增加伤害3%": 584,
        "增加会心3%": 589,
        "增加伤害2%": 583,
        "增加会心2%": 588,
    },
    "听雷": {
        "增加伤害5%": 598,
        "增加伤害4%": 597,
        "增加伤害3%": 596,
        "增加会心3%": 595,
        "增加会心2%": 594,
    },
    "鹤归孤山": {
        "增加伤害5%": 1567,
        "增加伤害4%": 1566,
        "增加伤害3%": 1565,
        "增加会心2%": 1568,
    },
    "梦泉虎跑": {
        "增加伤害5%": 1575,
        "增加伤害4%": 1574,
        "增加伤害3%": 1573,
        "增加会心2%": 1576,
    }
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
