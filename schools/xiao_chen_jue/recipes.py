from typing import Dict, Tuple, Union

from base.recipe import Recipe
from general.recipes import *

SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        1340: {}, 1341: {},
        1348: {}, 1349: {}, 1350: {},
        1355: {}, 1356: {}, 1357: {},
        1363: {}, 1364: {}, 1365: {},
        1372: {}, 1373: {}, 1374: {},
        1384: {}, 1385: {}, 1386: {},
        1392: {}, 1393: {}, 1394: {},
        1399: {}, 1400: {}, 1401: {},
        1406: {}, 1407: {}, 1408: {},
        1413: {}, 1414: {}, 1415: {},
        1420: {}, 1421: {},
        1597: {}, 1598: {}, 1599: {},
        1714: {}, 4764: {}, 4765: {},
        1548: {}, 1540: {}, 1541: {}, 17441: {}
    },
    CriticalStrikeRecipe_200: {
        1344: {},
        1600: {}
    },
    CriticalStrikeRecipe_300: {
        1345: {},
        1360: {},
        1366: {},
        1375: {},
        1387: {},
        1422: {},
        1601: {}
    },
    CriticalStrikeRecipe_400: {
        1346: {},
        1361: {},
        1367: {},
        1376: {},
        1388: {},
        1423: {}
    },
    CriticalStrikeRecipe_500: {
        1368: {},
        1389: {},
        1424: {},
        1980: {}, 1981: {}, 1982: {}, 1983: {}
    },
    CriticalStrikeRecipe_306: {
        17442: {}
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
    "拨狗朝天": {
        "增加伤害4%": 1341,
        "增加会心4%": 1346,
        "增加伤害3%": 1340,
        "增加会心3%": 1345,
        "增加会心2%": 1344,
    },
    "恶狗拦路": {
        "增加伤害5%": 1350,
        "增加伤害4%": 1349,
        "增加伤害3%": 1348,
    },
    "横打双獒": {
        "增加伤害5%": 1357,
        "增加伤害4%": 1356,
        "增加会心4%": 1361,
        "增加伤害3%": 1355,
        "增加会心3%": 1360,
    },
    "蜀犬吠日": {
        "增加伤害5%": 1365,
        "增加会心5%": 1368,
        "增加伤害4%": 1364,
        "增加会心4%": 1367,
        "增加伤害3%": 1363,
        "增加会心3%": 1366,
    },
    "亢龙有悔": {
        "增加伤害5%": 1374,
        "增加伤害4%": 1373,
        "增加会心4%": 1376,
        "增加伤害3%": 1372,
        "增加会心3%": 1375,
    },
    "神龙降世": {
        "增加伤害5%": 1386,
        "增加会心5%": 1389,
        "增加伤害4%": 1385,
        "增加会心4%": 1388,
        "增加伤害3%": 1384,
        "增加会心3%": 1387,
    },
    "天下无狗": {
        "增加伤害5%": 1394,
        "增加伤害4%": 1393,
        "增加伤害3%": 1392,
    },
    "狂龙乱舞": {
        "增加伤害5%": 1401,
        "增加伤害4%": 1400,
        "增加伤害3%": 1399,
    },
    "龙啸九天": {
        "增加伤害5%": 1408,
        "增加伤害4%": 1407,
        "增加伤害3%": 1406,
    },
    "龙跃于渊": {
        "增加伤害5%": 1415,
        "增加伤害4%": 1414,
        "增加伤害3%": 1413,
    },
    "龙腾五岳": {
        "增加会心5%": 1424,
        "增加伤害4%": 1421,
        "增加会心4%": 1423,
        "增加伤害3%": 1420,
        "增加会心3%": 1422,
    },
    "龙战于野": {
        "增加伤害5%": 1599,
        "增加伤害4%": 1598,
        "增加伤害3%": 1597,
        "增加会心3%": 1601,
        "增加会心2%": 1600,
    },
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
