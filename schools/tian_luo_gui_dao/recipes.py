from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe, interval_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "暴雨梨花针": {
        "5%伤害": damage_addition_recipe([3228], 51),
        "4%伤害": damage_addition_recipe([3228], 41),
        "3%伤害": damage_addition_recipe([3228], 31),
        "4%会心": critical_strike_recipe([3228], 400),
        "3%会心": critical_strike_recipe([3228], 300),
    },
    "蚀肌弹": {
        "-0.125运功": interval_recipe([3105], -2),
        "5%伤害": damage_addition_recipe([3105], 51),
        "4%伤害": damage_addition_recipe([3105], 41),
        "3%伤害": damage_addition_recipe([3105], 31),
        "4%会心": critical_strike_recipe([3105], 400),
        "3%会心": critical_strike_recipe([3105], 300),
    },
    "天绝地灭": {
        "5%伤害": damage_addition_recipe([36502, 30894, 30727], 51),
        "4%伤害": damage_addition_recipe([36502, 30894, 30727], 41),
        "3%伤害": damage_addition_recipe([36502, 30894, 30727], 31),
    },
    "暗藏杀机": {
        "5%伤害": damage_addition_recipe([3313], 51),
        "4%伤害": damage_addition_recipe([3313], 41),
        "3%伤害": damage_addition_recipe([3313], 31),
        "2%会心": critical_strike_recipe([3313], 200),
    },
}

RECIPES: Dict[str, List[str]] = {
    "暴雨梨花针": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "蚀肌弹": ["-0.125运功", "-0.125运功", "5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "天绝地灭": ["5%伤害", "4%伤害", "3%伤害"],
    "暗藏杀机": ["5%伤害", "4%伤害", "3%伤害", "2%会心"],
}
