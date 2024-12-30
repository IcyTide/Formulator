from general.recipes import *


class 增加会心10会心后伤害20(PhysicalCriticalRecipe):
    value = (1000, 102)


class 无我增加会心10会心后伤害20(PhysicalCriticalRecipe):
    value = (1000, 307)

    def add_skill(self, skill: Skill):
        if skill.skill_id in (390, 391, 392, 393, 394):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (390, 391, 392, 393, 394):
            super().sub_skill(skill)


class 叠刃伤害实际提高(ChannelIntervalRecipe):
    value = 1.45


class 万剑10会心会效(PhysicalCriticalRecipe):
    value = (1000, 102)


RECIPES: Dict[int, Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]]] = {
    0: {
        SkillRecipe: {
            60: {}, 61: {},
            70: {}, 71: {}, 72: {},
            105: {}, 106: {}, 107: {},
            1589: {}, 1590: {}, 1591: {},
            3253: {}, 2860: {}, 5616: {}, (5613, 2): {},
            5722: {}, 5758: {}, 5772: {},
            (818, 1): {}, 1522: {}, 1523: {}
        },
        CriticalStrikeRecipe_200: {
            65: {},
            100: {},
        },
        CriticalStrikeRecipe_300: {
            66: {},
            101: {},
        },
        CriticalStrikeRecipe_400: {
            67: {},
            102: {},
        },
        CriticalStrikeRecipe_500: {
            1135: {}
        },
        增加会心10会心后伤害20: {
            (638, 3): {}
        },
        无我增加会心10会心后伤害20: {
            2263: {}
        },
        叠刃伤害实际提高: {
            4583: {}
        },
        万剑10会心会效: {
            5173: {}
        }
    },
    1: {
        SkillRecipe: {
            17301: {}, 17305: {}, 17341: {}
        },
        CriticalStrikeRecipe_306: {
            17313: {}
        }
    }
}
RECIPE_CHOICES: Dict[int, Dict[str, Dict[str, int]]] = {
    0: {
        "人剑合一": {
            "增加伤害60%": 61,
            "增加伤害40%": 60
        },
        "三环套月": {
            "增加伤害5%": 72,
            "增加伤害4%": 71,
            "增加会心4%": 67,
            "增加伤害3%": 70,
            "增加会心3%": 66,
            "增加会心2%": 65
        },
        "无我无剑": {
            "增加伤害5%": 107,
            "增加伤害4%": 106,
            "增加会心4%": 102,
            "增加伤害3%": 105,
            "增加会心3%": 101,
            "增加会心2%": 100
        },
        "八荒归元": {
            "增加伤害5%": 1591,
            "增加伤害4%": 1590,
            "增加伤害3%": 1589
        }
    }
}
