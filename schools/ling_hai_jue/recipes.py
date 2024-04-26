from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "击水三千": {
        "5%伤害": damage_addition_recipe([19766, 19767], 51),
        "4%伤害": damage_addition_recipe([19766, 19767], 41),
        "3%伤害": damage_addition_recipe([19766, 19767], 31),
        "4%会心": critical_strike_recipe([19766, 19767], 400),
        "3%会心": critical_strike_recipe([19766, 19767], 300),
        "2%会心": critical_strike_recipe([19766, 19767], 200),
    },
    "木落雁归": {
        "5%伤害": damage_addition_recipe([19819], 51),
        "4%伤害": damage_addition_recipe([19819], 41),
        "3%伤害": damage_addition_recipe([19819], 31),
        "4%会心": critical_strike_recipe([19819], 400),
        "3%会心": critical_strike_recipe([19819], 300),
        "2%会心": critical_strike_recipe([19819], 200),
    },
    "海运南冥": {
        "4%伤害": damage_addition_recipe([20684, 20685], 41),
        "3%伤害": damage_addition_recipe([20684, 20685], 31),
        "2%伤害": damage_addition_recipe([20684, 20685], 21),
        "4%会心": critical_strike_recipe([20684, 20685], 400),
        "3%会心": critical_strike_recipe([20684, 20685], 300),
        "2%会心": critical_strike_recipe([20684, 20685], 200),
    },
    "翼绝云天": {
        "5%伤害": damage_addition_recipe([20016], 51),
        "4%伤害": damage_addition_recipe([20016], 41),
        "3%伤害": damage_addition_recipe([20016], 31),
        "4%会心": critical_strike_recipe([20016], 400),
        "3%会心": critical_strike_recipe([20016], 300),
        "2%会心": critical_strike_recipe([20016], 200),
    },
    "振翅图南": {
        "5%伤害": damage_addition_recipe([31250], 51),
        "4%伤害": damage_addition_recipe([31250], 41),
        "3%伤害": damage_addition_recipe([31250], 31),
        "4%会心": critical_strike_recipe([31250], 400),
        "3%会心": critical_strike_recipe([31250], 300),
        "2%会心": critical_strike_recipe([31250], 200),
    },
    "浮游天地": {
        "4%会心": critical_strike_recipe([20052], 400),
        "3%会心": critical_strike_recipe([20052], 300),
        "2%会心": critical_strike_recipe([20052], 200),
    }
}

RECIPES: Dict[str, List[str]] = {
    "击水三千": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "木落雁归": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "海运南冥": ["4%伤害", "4%会心", "3%伤害", "3%会心", "2%伤害", "2%会心"],
    "翼绝云天": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "振翅图南": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "浮游天地": ["4%会心", "3%会心", "2%会心"]
}
