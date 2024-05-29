from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "恶狗拦路": {
        "5%伤害": damage_addition_recipe([13520], 51),
        "4%伤害": damage_addition_recipe([13520], 41),
        "3%伤害": damage_addition_recipe([13520], 31),
    },
    "龙腾五岳": {
        "5%会心": critical_strike_recipe([13529], 500),
        "4%伤害": damage_addition_recipe([13529], 41),
        "4%会心": critical_strike_recipe([13529], 400),
        "3%伤害": damage_addition_recipe([13529], 31),
        "3%会心": critical_strike_recipe([13529], 300),
    },
    "龙战于野": {
        "5%伤害": damage_addition_recipe([6366, 6367, 6368], 51),
        "4%伤害": damage_addition_recipe([6366, 6367, 6368], 41),
        "3%伤害": damage_addition_recipe([6366, 6367, 6368], 31),
        "3%会心": critical_strike_recipe([6366, 6367, 6368], 300),
        "2%会心": critical_strike_recipe([6366, 6367, 6368], 200),
    },
    "龙跃于渊": {
        "5%伤害": damage_addition_recipe([6355, 6356, 6357], 51),
        "4%伤害": damage_addition_recipe([6355, 6356, 6357], 41),
        "3%伤害": damage_addition_recipe([6355, 6356, 6357], 31),
    },
    "亢龙有悔": {
        "5%伤害": damage_addition_recipe([6369, 6370, 6371, 6372, 6373, 6374], 51),
        "4%伤害": damage_addition_recipe([6369, 6370, 6371, 6372, 6373, 6374], 41),
        "4%会心": critical_strike_recipe([6369, 6370, 6371, 6372, 6373, 6374], 400),
        "3%伤害": damage_addition_recipe([6369, 6370, 6371, 6372, 6373, 6374], 31),
        "3%会心": critical_strike_recipe([6369, 6370, 6371, 6372, 6373, 6374], 300),
    }
}

RECIPES: Dict[str, List[str]] = {
    "恶狗拦路": ["5%伤害", "4%伤害", "3%伤害"],
    "龙腾五岳": ["5%会心", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "龙战于野": ["5%伤害", "4%伤害", "3%伤害", "3%会心", "2%会心"],
    "龙跃于渊": ["5%伤害", "4%伤害", "3%伤害"],
    "亢龙有悔": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心"],
}
