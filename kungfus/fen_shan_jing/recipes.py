from general.recipes import *


class 绝刀加会心(PhysicalCriticalRecipe):
    value = (1500, 200)


SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        1830: {}, 1831: {}, 1832: {},
        1838: {}, 1839: {}, 1840: {},
        1846: {}, 1847: {},
        1852: {}, 1853: {},
        1860: {}, 1861: {}, 1862: {},
        1953: {}, 1954: {},
        1941: {}, 2004: {}, 2006: {}, 2007: {}, 2008: {}, 4918: {}, 4919: {}, 4920: {}, 4921: {},
        1932: {}, 1933: {}, 1937: {}, 1938: {}, 17447: {},
    },
    CriticalStrikeRecipe_200: {
        1833: {},
        1841: {},
        1863: {},
        1955: {}
    },
    CriticalStrikeRecipe_300: {
        1834: {},
        1842: {},
        1848: {},
        1854: {},
        1864: {},
        1956: {}
    },
    CriticalStrikeRecipe_400: {
        1835: {},
        1843: {},
        1849: {},
        1855: {},
        1865: {}
    },
    CriticalStrikeRecipe_500: {
        1934: {}, 1936: {}
    },
    CriticalStrikeRecipe_306: {
        17448: {}
    },
    绝刀加会心: {
        1823: {}
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
    "劫刀": {
        "增加伤害5%": 1832,
        "增加伤害4%": 1831,
        "增加会心4%": 1835,
        "增加伤害3%": 1830,
        "增加会心3%": 1834,
        "增加会心2%": 1833,
    },
    "斩刀": {
        "增加伤害5%": 1840,
        "增加伤害4%": 1839,
        "增加会心4%": 1843,
        "增加伤害3%": 1838,
        "增加会心3%": 1842,
        "增加会心2%": 1841,
    },
    "绝刀": {
        "增加伤害5%": 1847,
        "增加伤害4%": 1846,
        "增加会心4%": 1849,
        "增加会心3%": 1848,
    },
    "盾压": {
        "增加伤害5%": 1853,
        "增加伤害4%": 1852,
        "增加会心4%": 1855,
        "增加会心3%": 1854,
    },
    "盾刀": {
        "增加伤害5%": 1862,
        "增加伤害4%": 1861,
        "增加会心4%": 1865,
        "增加伤害3%": 1860,
        "增加会心3%": 1864,
        "增加会心2%": 1863,
    },
    "盾飞": {
        "增加伤害4%": 1954,
        "增加伤害3%": 1953,
        "增加会心3%": 1956,
        "增加会心2%": 1955,
    },
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
