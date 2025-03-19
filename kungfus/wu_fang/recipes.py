from general.recipes import *


class 鸩羽奚毒射罔10会心会效(PoisonCriticalStrikeRecipe):
    value = 1000

    def add_skill(self, skill: Skill):
        if skill.skill_id == 27557:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 27557:
            super().sub_skill(skill)


RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        2638: {}, 2639: {},
        2646: {}, 2647: {},
        2652: {}, 2653: {},
        2659: {}, 2660: {},
        2694: {}, 2695: {},
        # buff
        2731: {}, 2732: {}, 2764: {},
        # 装备
        2839: {}, 2840: {}, 2842: {}, 2843: {}
    },
    CriticalStrikeRecipe_200: {
        2643: {}
    },
    CriticalStrikeRecipe_300: {
        2636: {},
        2644: {},
        2650: {}
    },
    CriticalStrikeRecipe_400: {
        2637: {},
        2645: {},
        2651: {},
        2692: {}
    },
    CriticalStrikeRecipe_500: {
        2693: {},
        2841: {}
    },
    鸩羽奚毒射罔10会心会效: {
        2549: {}
    }
}
RECIPE_CHOICES: Dict[str, Dict[str, int]] = {
    "商陆缀寒": {
        "增加会心4%": 2637,
        "增加伤害3%": 2639,
        "增加会心3%": 2636,
        "增加伤害2%": 2638
    },
    "钩吻断肠": {
        "增加会心4%": 2645,
        "增加伤害3%": 2647,
        "增加会心3%": 2644,
        "增加伤害2%": 2646,
        "增加会心2%": 2643
    },
    "川乌射罔": {
        "增加会心4%": 2651,
        "增加伤害3%": 2653,
        "增加会心3%": 2650,
        "增加伤害2%": 2652
    },
    "且待时休": {
        "增加伤害3%": 2660,
        "增加伤害2%": 2659
    },
    "银光照雪": {
        "增加会心5%": 2693,
        "增加会心4%": 2692,
        "增加伤害3%": 2695,
        "增加伤害2%": 2694
    }
}
