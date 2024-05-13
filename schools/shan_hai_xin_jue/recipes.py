from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe, pve_addition_recipe


RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "劲风簇": {
        "4%会心": critical_strike_recipe([35866], 400),
        "3%伤害": damage_addition_recipe([35866, 36453], 31),
        "3%会心": critical_strike_recipe([35866], 300),
        "2%伤害": damage_addition_recipe([35866, 36453], 21)
    },
    "饮羽簇": {
        "15%伤害": pve_addition_recipe([35987], 154),
        "4%会心": critical_strike_recipe([35987], 400),
        "3%伤害": damage_addition_recipe([35987], 31),
        "3%会心": critical_strike_recipe([35987], 300),
        "2%伤害": damage_addition_recipe([35987], 21)
    },
}

RECIPES: Dict[str, List[str]] = {
    "劲风簇": ["4%会心", "3%伤害", "3%会心", "2%伤害"],
    "饮羽簇": ["15%伤害", "4%会心", "3%伤害", "3%会心", "2%伤害"],
}
