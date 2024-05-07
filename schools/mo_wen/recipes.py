from typing import Dict, List

from base.gain import Gain
from base.recipe import attack_power_recipe, damage_addition_recipe, critical_strike_recipe


RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "宫": {
        "4%伤害": damage_addition_recipe([18860], 41),
        "3%伤害": damage_addition_recipe([18860], 31),
        "4%会心": critical_strike_recipe([18860], 400),
        "3%会心": critical_strike_recipe([18860], 300),
        "2%会心": critical_strike_recipe([18860], 200),
    },
    "商": {
        "5%伤害": attack_power_recipe([14311, 9357], 1.05),
        "4%伤害": attack_power_recipe([14311, 9357], 1.04),
        "3%伤害": attack_power_recipe([14311, 9357], 1.03),
        "4%会心": critical_strike_recipe([14311, 9357], 400),
        "3%会心": critical_strike_recipe([14311, 9357], 300),
        "2%会心": critical_strike_recipe([14311, 9357], 200),
    },
    "徵": {
        "4%伤害": damage_addition_recipe([14227, 18859], 41),
        "3%伤害": damage_addition_recipe([14227, 18859], 31),
        "4%会心": critical_strike_recipe([14227, 18859], 400),
        "3%会心": critical_strike_recipe([14227, 18859], 300),
        "2%会心": critical_strike_recipe([14227, 18859], 200),
    },
    "羽": {
        "4%伤害": damage_addition_recipe([14100], 41),
        "3%伤害": damage_addition_recipe([14100], 31),
        "4%会心": critical_strike_recipe([14100], 400),
        "3%会心": critical_strike_recipe([14100], 300),
    }
}

RECIPES: Dict[str, List[str]] = {
    "宫": ["4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "商": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "徵": ["4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "羽": ["4%伤害", "4%会心", "3%伤害", "3%会心"],
}
