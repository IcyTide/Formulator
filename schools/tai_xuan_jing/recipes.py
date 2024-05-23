from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "三星临": {
        "5%伤害": damage_addition_recipe([24676, 24558, 24675, 24677], 51),
        "4%伤害": damage_addition_recipe([24676, 24558, 24675, 24677], 41),
        "3%伤害": damage_addition_recipe([24676, 24558, 24675, 24677], 31),
        "4%会心": critical_strike_recipe([24676, 24558, 24675, 24677], 400),
        "3%会心": critical_strike_recipe([24676, 24558, 24675, 24677], 300),
        "2%会心": critical_strike_recipe([24676, 24558, 24675, 24677], 200),
    },
    "兵主逆": {
        "5%伤害": damage_addition_recipe([24813, 24811, 24812, 24814], 51),
        "4%伤害": damage_addition_recipe([24813, 24811, 24812, 24814], 41),
        "3%伤害": damage_addition_recipe([24813, 24811, 24812, 24814], 31),
        "4%会心": critical_strike_recipe([24813, 24811, 24812, 24814], 400),
        "3%会心": critical_strike_recipe([24813, 24811, 24812, 24814], 300),
    },
    "天斗旋": {
        "5%伤害": damage_addition_recipe([24823, 24821, 24822, 24824, 34683], 51),
        "4%伤害": damage_addition_recipe([24823, 24821, 24822, 24824, 34683], 41),
        "3%伤害": damage_addition_recipe([24823, 24821, 24822, 24824, 34683], 31),
        "4%会心": critical_strike_recipe([24823, 24821, 24822, 24824, 34683], 400),
        "3%会心": critical_strike_recipe([24823, 24821, 24822, 24824, 34683], 300),
        "2%会心": critical_strike_recipe([24823, 24821, 24822, 24824, 34683], 200),
    },
    "鬼星开穴": {
        "5%伤害": damage_addition_recipe([24870], 51),
        "4%伤害": damage_addition_recipe([24870], 41),
        "4%会心": critical_strike_recipe([24870], 400),
        "3%会心": critical_strike_recipe([24870], 300),
    },
}

RECIPES: Dict[str, List[str]] = {
    "三星临": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "兵主逆": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "天斗旋": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "鬼星开穴": ["5%伤害", "4%伤害", "4%会心", "3%会心"]
}
