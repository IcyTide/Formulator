from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "盾刀": {
        "5%伤害": damage_addition_recipe([13044], 51),
        "4%伤害": damage_addition_recipe([13044], 41),
        "3%伤害": damage_addition_recipe([13044], 31),
        "4%会心": critical_strike_recipe([13044], 400),
        "3%会心": critical_strike_recipe([13044], 300),
        "2%会心": critical_strike_recipe([13044], 200),
    },
    "盾压": {
        "5%伤害": damage_addition_recipe([19409], 51),
        "4%伤害": damage_addition_recipe([19409], 41),
        "4%会心": critical_strike_recipe([19409], 400),
        "3%会心": critical_strike_recipe([19409], 300),
    },
    "劫刀": {
        "5%伤害": damage_addition_recipe([28479], 51),
        "4%伤害": damage_addition_recipe([28479], 41),
        "3%伤害": damage_addition_recipe([28479], 31),
        "4%会心": critical_strike_recipe([28479], 400),
        "3%会心": critical_strike_recipe([28479], 300),
        "2%会心": critical_strike_recipe([28479], 200),
    },
    "斩刀": {
        "5%伤害": damage_addition_recipe([13092], 41),
        "4%伤害": damage_addition_recipe([13092], 31),
        "3%伤害": damage_addition_recipe([13092], 21),
        "4%会心": critical_strike_recipe([13092, 8249], 400),
        "3%会心": critical_strike_recipe([13092, 8249], 300),
        "2%会心": critical_strike_recipe([13092, 8249], 200),
    },
    "绝刀": {
        "5%伤害": damage_addition_recipe([13075], 51),
        "4%伤害": damage_addition_recipe([13075], 41),
        "4%会心": critical_strike_recipe([13075], 400),
        "3%会心": critical_strike_recipe([13075], 300),
    },
    "盾飞": {
        "4%伤害": damage_addition_recipe([13463], 41),
        "3%伤害": damage_addition_recipe([13463], 31),
        "3%会心": critical_strike_recipe([13463], 300),
        "2%会心": critical_strike_recipe([13463], 200),
    },
}

RECIPES: Dict[str, List[str]] = {
    "盾刀": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "盾压": ["5%伤害", "4%伤害", "4%会心", "3%会心"],
    "劫刀": ["4%伤害", "4%会心", "3%伤害", "3%会心", "2%伤害", "2%会心"],
    "斩刀": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "绝刀": ["5%伤害", "4%伤害", "4%会心", "3%会心"],
    "盾飞": ["4%伤害", "3%伤害", "3%会心", "2%会心"],
}
