from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "三环套月": {
        "5%伤害": damage_addition_recipe([32408], 51),
        "4%伤害": damage_addition_recipe([32408], 41),
        "3%伤害": damage_addition_recipe([32408], 31),
        "4%会心": critical_strike_recipe([32408], 400),
        "3%会心": critical_strike_recipe([32408], 300),
        "2%会心": critical_strike_recipe([32408], 200),
    },
    "无我无剑": {
        "5%伤害": damage_addition_recipe([386, 387, 388, 389, 390, 391, 392, 393, 394], 51),
        "4%伤害": damage_addition_recipe([386, 387, 388, 389, 390, 391, 392, 393, 394], 41),
        "3%伤害": damage_addition_recipe([386, 387, 388, 389, 390, 391, 392, 393, 394], 31),
        "4%会心": critical_strike_recipe([386, 387, 388, 389, 390, 391, 392, 393, 394], 400),
        "3%会心": critical_strike_recipe([386, 387, 388, 389, 390, 391, 392, 393, 394], 300),
        "2%会心": critical_strike_recipe([386, 387, 388, 389, 390, 391, 392, 393, 394], 200),
    },
    "八荒归元": {
        "5%伤害": damage_addition_recipe([13853, 4954], 51),
        "4%伤害": damage_addition_recipe([13853, 4954], 41),
        "3%伤害": damage_addition_recipe([13853, 4954], 31),
    },
    "人剑合一": {
        "60%伤害": damage_addition_recipe([589], 614),
        "40%伤害": damage_addition_recipe([589], 410),
    }
}

RECIPES: Dict[str, List[str]] = {
    "三环套月": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "无我无剑": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "八荒归元": ["5%伤害", "4%伤害", "3%伤害"],
    "人剑合一": ["60%伤害", "40%伤害"]
}
