from typing import Dict, Tuple, Union

from base.recipe import Recipe
from general.recipes import *


class 明教_秘籍_烈日斩_静止目标加伤害(SkillRecipe):
    value = 102

    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.move_state_damage_addition += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.move_state_damage_addition -= self.value


class 生死劫必会心(SolarLunarCriticalStrikeRecipe):
    value = 10000


class 净世破魔击必会心(SolarLunarCriticalStrikeRecipe):
    value = 10000


class 新明光_阳性终结技增强(SkillRecipe):
    value = 246

    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.solar_attack_power_gain_extra += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.solar_attack_power_gain_extra -= self.value


class 新明光_阴性终结技增强(SkillRecipe):
    value = 246

    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.lunar_attack_power_gain_extra += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.lunar_attack_power_gain_extra -= self.value


class 明教通用会心10(SolarLunarCriticalRecipe):
    value = (1000, 102)


SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        984: {}, 985: {},
        999: {}, 1000: {}, 1001: {},
        1007: {}, 1008: {}, 1009: {},
        1014: {}, 1015: {}, 1016: {},
        1051: {}, 1052: {}, 1053: {},
        1621: {}, 1622: {}, 1623: {},
        5149: {}, 5150: {},
        (948, 2): {}, 1542: {}, 1543: {}, 17332: {}
    },
    CriticalStrikeRecipe_200: {
    },
    CriticalStrikeRecipe_300: {
        988: {},
        992: {},
        1004: {},
        1010: {},
        1017: {},
        1054: {},
    },
    CriticalStrikeRecipe_400: {
        989: {},
        993: {},
        1005: {},
        1011: {},
        1018: {},
        1055: {},
    },
    CriticalStrikeRecipe_500: {
        990: {},
        994: {},
        1019: {},
        1056: {},
        1148: {}, 1149: {}
    },
    CriticalStrikeRecipe_306: {
        17334: {}
    },
    明教_秘籍_烈日斩_静止目标加伤害: {
        1013: {}
    },
    生死劫必会心: {
        4545: {}
    },
    净世破魔击必会心: {
        4546: {}
    },
    新明光_阳性终结技增强: {
        3222: {}, 3223: {}, 3224: {}
    },
    新明光_阴性终结技增强: {
        3225: {}, 3226: {}, 3227: {}
    },
    明教通用会心10: {
        1314: {}, 1315: {}
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
    "幽月轮": {
        "增加会心5%": 990,
        "增加伤害4%": 985,
        "增加会心4%": 989,
        "增加伤害3%": 984,
        "增加会心3%": 988
    },
    "银月斩": {
        "增加会心5%": 994,
        "增加会心4%": 993,
        "增加会心3%": 992
    },
    "赤日轮": {
        "增加伤害5%": 1001,
        "增加伤害4%": 1000,
        "增加会心4%": 1005,
        "增加伤害3%": 999,
        "增加会心3%": 1004
    },
    "烈日斩": {
        "增加伤害10%": 1013,
        "增加伤害5%": 1009,
        "增加伤害4%": 1008,
        "增加会心4%": 1011,
        "增加伤害3%": 1007,
        "增加会心3%": 1010
    },
    "净世破魔击": {
        "增加伤害5%": 1016,
        "增加会心5%": 1019,
        "增加伤害4%": 1015,
        "增加会心4%": 1018,
        "增加伤害3%": 1014,
        "增加会心3%": 1017
    },
    "驱夜断愁": {
        "增加伤害5%": 1053,
        "增加会心5%": 1056,
        "增加伤害4%": 1052,
        "增加会心4%": 1055,
        "增加伤害3%": 1051,
        "增加会心3%": 1054
    },
    "生死劫": {
        "增加伤害5%": 1623,
        "增加伤害4%": 1622,
        "增加伤害3%": 1621
    },
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
