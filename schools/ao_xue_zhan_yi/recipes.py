from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "穿云": {
        "4%伤害": damage_addition_recipe([18207], 41),
        "3%伤害": damage_addition_recipe([18207], 31),
        "3%会心": critical_strike_recipe([18207], 300),
        "2%会心": critical_strike_recipe([18207], 200),
    },
    "龙吟": {
        "5%伤害": damage_addition_recipe([18603], 51),
        "4%伤害": damage_addition_recipe([18603], 41),
        "3%伤害": damage_addition_recipe([18603], 31),
    },
    "龙牙": {
        "5%伤害": damage_addition_recipe([18773, 15002], 51),
        "4%伤害": damage_addition_recipe([18773, 15002], 41),
        "3%伤害": damage_addition_recipe([18773, 15002], 31),
        "4%会心": critical_strike_recipe([18773, 15002], 400),
        "3%会心": critical_strike_recipe([18773, 15002], 300),
        "2%会心": critical_strike_recipe([18773, 15002], 200),
    },
    "灭": {
        "4%伤害": damage_addition_recipe([702, 24898, 6526], 41),
        "3%伤害": damage_addition_recipe([702, 24898, 6526], 31),
        "3%会心": critical_strike_recipe([702, 24898, 6526], 300),
        "2%会心": critical_strike_recipe([702, 24898, 6526], 200),
    },
    "突": {
        "4%伤害": damage_addition_recipe([431, 14882], 41),
        "3%伤害": damage_addition_recipe([431, 14882], 31),
    },
    "断魂刺": {
        "4%伤害": damage_addition_recipe([409], 41),
        "3%伤害": damage_addition_recipe([409], 31),
    }
}

RECIPES: Dict[str, List[str]] = {
    "穿云": ["4%伤害", "3%伤害", "3%会心", "2%会心"],
    "龙吟": ["5%伤害", "4%伤害", "3%伤害"],
    "龙牙": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "灭": ["4%伤害", "3%伤害", "3%会心", "2%会心"],
    "突": ["4%伤害", "3%伤害"],
    "断魂刺": ["4%伤害", "3%伤害"]
}
