from general.recipes import *


class 守缺10会心会效(SolarCriticalRecipe):
    value = (1000, 102)


class 横扫10会心会效(SolarCriticalRecipe):
    value = (1000, 205)


RECIPES: Dict[int, Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]]] = {
    0: {
        SkillRecipe: {
            233: {}, 234: {}, 235: {},
            259: {},
            268: {}, 269: {}, 270: {},
            287: {}, 288: {}, 289: {},
            295: {}, 296: {}, 297: {},
            1645: {}, 1646: {}, 1647: {},
            2862: {},
            (959, 3): {},
            (818, 5): {}, 1147: {}, 1512: {}, 1513: {}
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
        守缺10会心会效: {
            2299: {}
        },
        横扫10会心会效: {
            5157: {}
        }
    },
    1: {
        SkillRecipe: {
            17351: {}, 17354: {}, 17355: {}
        },
        CriticalStrikeRecipe_306: {
            17352: {}
        }
    }
}
RECIPE_CHOICES: Dict[int, Dict[str, Dict[str, int]]] = {
    0: {
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
}
