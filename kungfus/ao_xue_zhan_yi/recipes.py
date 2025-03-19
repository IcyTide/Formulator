from general.recipes import *


class 增加会心10(PhysicalCriticalRecipe):
    value = (1000, 102)


class 天策流血20(ChannelIntervalRecipe):
    value = 1.2

    def add_skill(self, skill: Skill):
        if skill.skill_id in (18591, 15000, 18610, 26773, 401):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (18591, 15000, 18610, 26773, 401):
            super().sub_skill(skill)


RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        338: {}, 339: {},
        345: {}, 346: {},
        356: {}, 361: {}, 362: {},
        369: {}, 370: {},
        398: {}, 399: {},
        1557: {}, 1558: {}, 1559: {},
        # 奇穴
        **{(recipe_id, i + 1): {} for recipe_id in (4504, 4505, 4506, 4507) for i in range(5)},
        # 装备
        (817, 2): {}, 1508: {}, 1509: {}
    },
    增加会心10: {
        1225: {}, 5649: {}
    },
    天策流血20: {
        3257: {}
    },
    CriticalStrikeRecipe_200: {
        334: {},
        357: {},
        367: {}
    },
    CriticalStrikeRecipe_300: {
        335: {},
        358: {},
        368: {}
    },
    CriticalStrikeRecipe_400: {
        355: {},
    },
    CriticalStrikeRecipe_500: {
        1133: {}
    }

}
RECIPE_CHOICES: Dict[str, Dict[str, int]] = {
    "穿云": {
        "增加伤害4%": 339,
        "增加伤害3%": 338,
        "增加会心3%": 335,
        "增加会心2%": 334
    },
    "断魂刺": {
        "增加伤害4%": 346,
        "增加伤害3%": 345,
    },
    "龙牙": {
        "增加伤害5%": 356,
        "增加伤害4%": 362,
        "增加会心4%": 355,
        "增加伤害3%": 361,
        "增加会心3%": 358,
        "增加会心2%": 357
    },
    "灭": {
        "增加伤害4%": 370,
        "增加伤害3%": 369,
        "增加会心3%": 368,
        "增加会心2%": 367
    },
    "突": {
        "增加伤害4%": 398,
        "增加伤害3%": 399
    },
    "龙吟": {
        "增加伤害5%": 1559,
        "增加伤害4%": 1558,
        "增加伤害3%": 1557
    }
}
