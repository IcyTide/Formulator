from general.recipes import *


class 混元内功会心提高(NeutralCriticalRecipe):
    value = (2000, 205)


class 故幽加芙蓉会心(NeutralCriticalRecipe):
    value = (1500, 154)


class 新套装加钟林10(ChannelIntervalRecipe):
    value = 1.15


SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        492: {}, 493: {},
        1677: {}, 1678: {}, 1679: {},
        4907: {}, 4908: {}, 4909: {},
        4849: {}, 3019: {}, 3020: {}, 3235: {}, 3236: {},
        1546: {}, 1516: {}, 1517: {}, 17399: {}
    },
    CriticalStrikeRecipe_200: {
        490: {},
        4904: {}
    },
    CriticalStrikeRecipe_300: {
        491: {},
        4905: {}
    },
    CriticalStrikeRecipe_400: {
        4906: {}
    },
    CriticalStrikeRecipe_500: {
        1131: {}, 1979: {}
    },
    CriticalStrikeRecipe_306: {
        17400: {}
    },
    混元内功会心提高: {
        1295: {}
    },
    故幽加芙蓉会心: {
        2439: {}, 2440: {}, 2441: {}, 2442: {}, 2443: {}, 3151: {}
    },
    新套装加钟林10: {
        (817, 1): {}
    }
}
RECIPES: Dict[Tuple[int, int], Recipe] = {**GENERAL_RECIPES}
for recipe_class, recipes in SCHOOL_RECIPES.items():
    for recipe_key, attrs in recipes.items():
        if not isinstance(recipe_key, tuple):
            recipe_key = (recipe_key, 1)
        RECIPES[recipe_key] = recipe = recipe_class(*recipe_key)
        recipe.set_asset(attrs)
RECIPE_CHOICES: Dict[str, Dict[str, int]] = {
    "阳明指": {
        "增加伤害4%": 493,
        "增加伤害3%": 492,
        "增加会心3%": 491,
        "增加会心2%": 490,
    },
    "快雪时晴": {
        "增加伤害5%": 1679,
        "增加伤害4%": 1678,
        "增加伤害3%": 1677
    },
    "芙蓉并蒂": {
        "增加伤害5%": 4909,
        "增加伤害4%": 4908,
        "增加会心4%": 4906,
        "增加伤害3%": 4907,
        "增加会心3%": 4905,
        "增加会心2%": 4904,
    }
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    }
    for skill, recipes in RECIPE_CHOICES.items()
}
