from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "三环套月": {
        "5%伤害": damage_addition_recipe([19766, 19767], 51),
        "4%伤害": damage_addition_recipe([19766, 19767], 41),
        "3%伤害": damage_addition_recipe([19766, 19767], 31),
        "4%会心": critical_strike_recipe([19766, 19767], 400),
        "3%会心": critical_strike_recipe([19766, 19767], 300),
        "2%会心": critical_strike_recipe([19766, 19767], 200),
    },
    "无我无剑": {
        "5%伤害": damage_addition_recipe([19819], 51),
        "4%伤害": damage_addition_recipe([19819], 41),
        "3%伤害": damage_addition_recipe([19819], 31),
        "4%会心": critical_strike_recipe([19819], 400),
        "3%会心": critical_strike_recipe([19819], 300),
        "2%会心": critical_strike_recipe([19819], 200),
    },
    "八荒归元": {
        "5%伤害": damage_addition_recipe([19819], 51),
        "4%伤害": damage_addition_recipe([19819], 41),
        "3%伤害": damage_addition_recipe([19819], 31),
    },
    "人剑合一": {
        "60%伤害": damage_addition_recipe([20016], 614),
        "40%伤害": damage_addition_recipe([20016], 410),
    }
}

RECIPES: Dict[str, List[str]] = {
    "三环套月": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "无我无剑": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "八荒归元": ["5%伤害", "4%伤害", "3%伤害"],
    "人剑合一": ["60%伤害", "40%伤害"]
}
