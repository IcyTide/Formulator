from general.recipes import *


class 混元内功会心提高(NeutralCriticalRecipe):
    value = (2000, 205)


class 故幽加芙蓉会心(NeutralCriticalRecipe):
    value = (1500, 154)


class 新套装加钟林10(ChannelIntervalRecipe):
    value = 1.15


RECIPES: Dict[int, Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]]] = {
    0: {
        SkillRecipe: {
            492: {}, 493: {},
            1677: {}, 1678: {}, 1679: {},
            4907: {}, 4908: {}, 4909: {},
            4849: {}, 3019: {}, 3020: {}, 3235: {}, 3236: {},
            1546: {}, 1516: {}, 1517: {}
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
        混元内功会心提高: {
            1295: {}, 5497: {}
        },
        故幽加芙蓉会心: {
            2439: {}, 2440: {}, 2441: {}, 2442: {}, 2443: {}, 3151: {}
        },
        新套装加钟林10: {
            (817, 1): {}
        }
    },
    1: {
        SkillRecipe: {
            17399: {}
        },
        CriticalStrikeRecipe_306: {
            17400: {}
        }
    }
}
RECIPE_CHOICES: Dict[int, Dict[str, Dict[str, int]]] = {
    0: {
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
}
