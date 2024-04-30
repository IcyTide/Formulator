from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "行云式": {
        "5%伤害": damage_addition_recipe([32149, 32150, 32151], 51),
        "4%伤害": damage_addition_recipe([32149, 32150, 32151], 41),
        "3%伤害": damage_addition_recipe([32149, 32150, 32151], 31),
        "4%会心": critical_strike_recipe([32149, 32150, 32151], 400),
        "3%会心": critical_strike_recipe([32149, 32150, 32151], 300),
        "2%会心": critical_strike_recipe([32149, 32150, 32151], 200),
    },
    "决云势": {
        "4%伤害": damage_addition_recipe([32154], 41),
        "3%伤害": damage_addition_recipe([32154], 31),
        "3%会心": critical_strike_recipe([32154], 300),
        "2%会心": critical_strike_recipe([32154], 200),
    },
    "断云势": {
        "5%伤害": damage_addition_recipe([32167, 32348], 51),
        "4%伤害": damage_addition_recipe([32167, 32348], 41),
        "4%会心": critical_strike_recipe([32167, 32348], 400),
        "3%会心": critical_strike_recipe([32167, 32348], 300),
    },
    "沧浪三叠": {
        "5%伤害": damage_addition_recipe([32602, 32603, 32604], 51),
        "4%伤害": damage_addition_recipe([32602, 32603, 32604], 41),
        "3%伤害": damage_addition_recipe([32602, 32603, 32604], 31),
        "4%会心": critical_strike_recipe([32602, 32603, 32604], 400),
        "3%会心": critical_strike_recipe([32602, 32603, 32604], 300),
        "2%会心": critical_strike_recipe([32602, 32603, 32604], 200),
    },
    "横云断浪": {
        "5%伤害": damage_addition_recipe([32234], 51),
        "4%伤害": damage_addition_recipe([32234], 41),
        "4%会心": critical_strike_recipe([32234], 400),
        "3%会心": critical_strike_recipe([32234], 300),
    },
    "孤锋破浪": {
        "5%伤害": damage_addition_recipe([32235, 32236, 32237, 32238, 32239, 32891, 32892], 51),
        "4%伤害": damage_addition_recipe([32235, 32236, 32237, 32238, 32239, 32891, 32892], 41),
        "4%会心": critical_strike_recipe([32235, 32236, 32237, 32238, 32239, 32891, 32892], 400),
        "3%会心": critical_strike_recipe([32235, 32236, 32237, 32238, 32239, 32891, 32892], 300),
    },
    "留客雨": {
        "5%伤害": damage_addition_recipe([32246], 51),
        "4%伤害": damage_addition_recipe([32246], 41),
        "3%伤害": damage_addition_recipe([32246], 31),
        "4%会心": critical_strike_recipe([32246], 400),
        "3%会心": critical_strike_recipe([32246], 300),
        "2%会心": critical_strike_recipe([32246], 200),
    },
    "触石雨": {
        "4%伤害": damage_addition_recipe([32766], 41),
        "3%伤害": damage_addition_recipe([32766], 31),
    },
}

RECIPES: Dict[str, List[str]] = {
    "行云式": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "决云势": ["4%伤害", "3%伤害", "3%会心", "2%会心"],
    "断云势": ["5%伤害", "4%伤害", "4%会心", "3%会心"],
    "沧浪三叠": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "横云断浪": ["5%伤害", "4%伤害", "4%会心", "3%会心"],
    "孤锋破浪": ["5%伤害", "4%伤害", "4%会心", "3%会心"],
    "留客雨": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "触石雨": ["4%伤害", "3%伤害"]
}
