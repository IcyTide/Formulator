from general.recipes import *


class 气剑增伤(PveAdditionRecipe):
    value = 1331


class 增加会心10会心后伤害20(NeutralCriticalRecipe):
    value = (1000, 102)


RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        24: {}, 25: {}, 26: {},
        97: {}, 98: {}, 99: {},
        1581: {}, 1582: {}, 1583: {},
        # buff
        3253: {},
        # 奇穴
        2360: {}, 2361: {}, 2362: {}, 2363: {}, **{recipe_id: {} for recipe_id in range(4467, 4476 + 1)},
        # 装备
        (818, 2): {}, 4602: {}, 1520: {}, 1521: {}, 5756: {}
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
    气剑增伤: {
        5172: {}
    },
    增加会心10会心后伤害20: {
        (4092, 3): {}
    }
}
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
