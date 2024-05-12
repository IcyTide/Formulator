from typing import Dict, List

from base.gain import Gain
from base.recipe import double_addition_recipe, attack_power_recipe, damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "蝎心": {
        "4%伤害": double_addition_recipe([6218], [], 1.04, 41),
        "3%伤害": double_addition_recipe([6218], [], 1.03, 31),
        "3%会心": critical_strike_recipe([6218], 300),
        "2%会心": critical_strike_recipe([6218], 200),
    },
    "蛇影": {
        "5%伤害": attack_power_recipe([25917], 1.05),
        "4%伤害": attack_power_recipe([25917], 1.04),
        "4%会心": critical_strike_recipe([25917], 300),
        "3%会心": critical_strike_recipe([25917], 300),
        "2%会心": critical_strike_recipe([25917], 200),
    },
    "百足": {
        "10%伤害": attack_power_recipe([13472, 2509], 1.1),
        "5%伤害": attack_power_recipe([13472, 2509], 1.05),
    },
    "灵蛊": {
        "10%伤害": damage_addition_recipe([18590], 102),
    },
}

RECIPES: Dict[str, List[str]] = {
    "蝎心": ["4%伤害", "3%伤害", "3%会心", "2%会心"],
    "百足": ["10%伤害", "10%伤害", "5%伤害"],
    "灵蛊": ["10%伤害", "10%伤害", "10%伤害"],
}
