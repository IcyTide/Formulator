from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "两仪化形": {
        "5%伤害": damage_addition_recipe([3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448], 51),
        "4%伤害": damage_addition_recipe([3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448], 41),
        "3%伤害": damage_addition_recipe([3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448], 31),
        "4%会心": critical_strike_recipe([3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448], 400),
        "3%会心": critical_strike_recipe([3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448], 300),
        "2%会心": critical_strike_recipe([3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448], 200),
    },
    "四象轮回": {
        "5%伤害": damage_addition_recipe([896], 51),
        "4%伤害": damage_addition_recipe([896], 41),
        "3%伤害": damage_addition_recipe([896], 31),
        "4%会心": critical_strike_recipe([896], 400),
        "3%会心": critical_strike_recipe([896], 300),
        "2%会心": critical_strike_recipe([896], 200),
    },
    "万世不竭": {
        "5%伤害": damage_addition_recipe([18649, 18650, 18651, 18652, 18653, 22014], 51),
        "4%伤害": damage_addition_recipe([18649, 18650, 18651, 18652, 18653, 22014], 41),
        "3%伤害": damage_addition_recipe([18649, 18650, 18651, 18652, 18653, 22014], 31),
    }
}

RECIPES: Dict[str, List[str]] = {
    "两仪化形": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "四象轮回": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "万世不竭": ["5%伤害", "4%伤害", "3%伤害"]
}
