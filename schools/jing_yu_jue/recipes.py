from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe, interval_recipe, shield_gain_recipe, \
    attack_power_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "暴雨梨花针": {
        "5%伤害": damage_addition_recipe([3227], 51),
        "4%伤害": damage_addition_recipe([3227], 41),
        "4%会心": critical_strike_recipe([3227], 400),
        "3%伤害": damage_addition_recipe([3227], 31),
        "3%会心": critical_strike_recipe([3227], 300),
    },
    "夺魄箭": {
        "-0.125运功": interval_recipe([3095, 37504], -2),
        "5%会心": critical_strike_recipe([3095, 37504], 500),
        "4%会心": critical_strike_recipe([3095, 37504], 400),
        "4%伤害": damage_addition_recipe([3095, 37504], 41),
        "3%伤害": damage_addition_recipe([3095, 37504], 31),
        "3%会心": critical_strike_recipe([3095, 37504], 300),
    },
    "追命箭": {
        "20%无视防御": shield_gain_recipe([6920], -205),
        "5%伤害": damage_addition_recipe([6920], 51),
        "4%伤害": damage_addition_recipe([6920], 41),
        "4%会心": critical_strike_recipe([6920], 400),
        "3%伤害": damage_addition_recipe([6920], 31),
        "3%会心": critical_strike_recipe([6920], 300),
    },
    "逐星箭": {
        "5%伤害": damage_addition_recipe([3187], 51),
        "4%伤害": damage_addition_recipe([3187], 41),
        "3%伤害": damage_addition_recipe([3187], 31),
    },
    "穿心弩": {
        "10%伤害": attack_power_recipe([2237], 1.1),
        "5%伤害": attack_power_recipe([2237], 1.05)
    }
}

RECIPES: Dict[str, List[str]] = {
    "暴雨梨花针": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "夺魄箭": ["-0.125运功", "-0.125运功", "5%会心", "4%伤害", "4%会心", "3%伤害"],
    "追命箭": ["20%无视防御", "5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "逐星箭": ["5%伤害", "4%伤害", "3%伤害"],
    "穿心弩": ["10%伤害", "5%伤害"],
}
