from typing import Dict, Tuple, Union

from base.recipe import Recipe
from general.recipes import *


class 鸩羽奚毒射罔10会心会效(PoisonCriticalStrikeRecipe):
    value = 1000

    def add_skill(self, skill: Skill):
        if skill.skill_id == 27557:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 27557:
            super().sub_skill(skill)


SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        2638: {}, 2639: {},
        2646: {}, 2647: {},
        2652: {}, 2653: {},
        2659: {}, 2660: {},
        2694: {}, 2695: {},
        2579: {}, 2731: {}, 2732: {}, 2764: {}, 5363: {}, 2858: {}, 3173: {},
        2541: {},
        2839: {}, 2840: {}, 2842: {}, 2843: {}, 17458: {}
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
    CriticalStrikeRecipe_306: {
        17459: {}
    },
    鸩羽奚毒射罔10会心会效: {
        2549: {}
    }
}
RECIPES: Dict[Tuple[int, int], Recipe] = {**GENERAL_RECIPES}
for recipe_class, recipes in SCHOOL_RECIPES.items():
    for recipe_key, attrs in recipes.items():
        recipe_key = recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        RECIPES[recipe_key] = recipe = recipe_class(*recipe_key)
        recipe.set_asset(attrs)
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
    },
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
