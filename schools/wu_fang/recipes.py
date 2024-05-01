from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "商陆缀寒": {
        "3%伤害": damage_addition_recipe([27552], 31),
        "2%伤害": damage_addition_recipe([27552], 21),
        "4%会心": critical_strike_recipe([27552], 400),
        "3%会心": critical_strike_recipe([27552], 300),
    },
    "钩吻断肠": {
        "3%伤害": damage_addition_recipe([27555], 41),
        "2%伤害": damage_addition_recipe([27555], 31),
        "4%会心": critical_strike_recipe([27555], 400),
        "3%会心": critical_strike_recipe([27555], 300),
        "2%会心": critical_strike_recipe([27555], 200),
    },
    "川乌射罔": {
        "3%伤害": damage_addition_recipe([27557], 31),
        "2%伤害": damage_addition_recipe([27557], 21),
        "4%会心": critical_strike_recipe([27557], 400),
        "3%会心": critical_strike_recipe([27557], 300),
    },
    "且待时休": {
        "3%伤害": damage_addition_recipe([27584], 31),
        "2%伤害": damage_addition_recipe([27584], 21),
    },
    "银光照雪": {
        "3%伤害": damage_addition_recipe([28346, 34699], 31),
        "2%伤害": damage_addition_recipe([28346, 34699], 21),
        "5%会心": critical_strike_recipe([28346, 34699], 500),
        "4%会心": critical_strike_recipe([28346, 34699], 400),
    },
}

RECIPES: Dict[str, List[str]] = {
    "商陆缀寒": ["4%会心", "3%伤害", "3%会心", "2%伤害"],
    "钩吻断肠": ["4%会心", "3%伤害", "3%会心", "2%伤害", "2%会心"],
    "川乌射罔": ["4%会心", "3%伤害", "3%会心", "2%伤害"],
    "且待时休": ["3%伤害", "2%伤害"],
    "银光照雪": ["5%会心", "4%会心", "3%伤害", "2%伤害"],
}
