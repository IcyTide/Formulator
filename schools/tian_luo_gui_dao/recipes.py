from typing import Dict, Tuple, Union

from base.recipe import Recipe
from general.recipes import *


class 鬼斧无视防御(MagicalShieldGainRecipe):
    value = -512

    def add_skill(self, skill: Skill):
        if skill.skill_id in (3404, 3824, 3825, 3826, 3827, 3828):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (3404, 3824, 3825, 3826, 3827, 3828):
            super().sub_skill(skill)


class 神机车无视防御(MagicalShieldGainRecipe):
    value = -512


class 连弩重弩伤害额外提高(ChannelIntervalRecipe):
    value = 1.75

    def add_skill(self, skill: Skill):
        if skill.skill_id != 3367:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id != 3367:
            super().sub_skill(skill)


class 神机车连弩伤害额外提高(ChannelIntervalRecipe):
    value = 1.75

    def add_skill(self, skill: Skill):
        if skill.skill_id in (21854, 21850):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (21854, 21850):
            super().sub_skill(skill)


class 神机控制天绝地灭10(ChannelIntervalRecipe):
    value = 1.1


class 神机控制暗藏杀机伤害10(ChannelIntervalRecipe):
    value = 1.1


class 暴雨梨花针_加会心(PhysicalCriticalRecipe):
    value = (1000, 100)


SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        834: {}, 835: {}, 836: {},
        868: {}, 869: {}, 870: {}, 871: {}, 872: {},
        884: {}, 885: {}, 886: {},
        1669: {}, 1670: {}, 1671: {},
        5580: {}, 4932: {}, 4933: {}, 2962: {},
        947: {}, 4120: {}, 1532: {}, 1533: {}, 17429: {}
    },
    CriticalStrikeRecipe_200: {
        1672: {}
    },
    CriticalStrikeRecipe_300: {
        837: {},
        873: {}
    },
    CriticalStrikeRecipe_400: {
        838: {},
        874: {}
    },
    CriticalStrikeRecipe_500: {
        1146: {}, 1978: {}
    },
    CriticalStrikeRecipe_306: {
        17430: {}
    },
    鬼斧无视防御: {
        4677: {}
    },
    神机车无视防御: {
        4930: {}, 4931: {}
    },
    连弩重弩伤害额外提高: {
        5421: {}
    },
    神机车连弩伤害额外提高: {
        5459: {}
    },
    神机控制天绝地灭10: {
        2960: {}
    },
    神机控制暗藏杀机伤害10: {
        2961: {}
    },
    暴雨梨花针_加会心: {
        1204: {}
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
    "暴雨梨花针": {
        "增加伤害5%": 836,
        "增加伤害4%": 835,
        "增加会心4%": 838,
        "增加伤害3%": 834,
        "增加会心3%": 837,
    },
    "夺魄箭": {
        "运功减少0.125秒·1": 868,
        "运功减少0.125秒·2": 869,
        "增加伤害5%": 872,
        "增加伤害4%": 871,
        "增加会心4%": 874,
        "增加伤害3%": 870,
        "增加会心3%": 873,
    },
    "天绝地灭": {
        "增加伤害5%": 886,
        "增加伤害4%": 885,
        "增加伤害3%": 884,
    },
    "暗藏杀机": {
        "增加伤害5%": 1671,
        "增加伤害4%": 1670,
        "增加伤害3%": 1669,
        "增加会心2%": 1672,
    },
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
