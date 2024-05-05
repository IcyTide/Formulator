from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "玳弦急曲": {
        "5%伤害": damage_addition_recipe([6234, 6554], 51),
        "4%伤害": damage_addition_recipe([6234, 6554], 41),
        "3%伤害": damage_addition_recipe([6234, 6554], 31),
    },
    "剑气长江": {
        "6%伤害": damage_addition_recipe([30524], 61),
        "4%伤害": damage_addition_recipe([30524], 41),
        "3%会心": critical_strike_recipe([30524], 300),
        "2%会心": critical_strike_recipe([30524], 200),
    },
    "江海凝光": {
        "15%伤害": damage_addition_recipe([6559], 154),
        "3%会心": critical_strike_recipe([6559], 300),
        "2%会心": critical_strike_recipe([6559], 200),
    },
}

RECIPES: Dict[str, List[str]] = {
    "玳弦急曲": ["5%伤害", "4%伤害", "3%伤害"],
    "剑气长江": ["6%伤害", "4%伤害", "3%会心", "2%会心"],
    "江海凝光": ["15%伤害", "15%伤害", "3%会心", "2%会心"],
}
