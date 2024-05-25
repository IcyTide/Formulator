from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, extra_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "烈日斩": {
        "10%伤害": extra_addition_recipe([3963], 51),
        "5%伤害": damage_addition_recipe([3963], 51),
        "4%伤害": damage_addition_recipe([3963], 41),
        "3%伤害": damage_addition_recipe([3963], 31),
        "4%会心": critical_strike_recipe([3963], 400),
        "3%会心": critical_strike_recipe([3963], 300)
    },
    "银月斩": {
        "5%会心": critical_strike_recipe([13468, 402], 500),
        "4%会心": critical_strike_recipe([13468, 402], 400),
        "3%会心": critical_strike_recipe([13468, 402], 300)
    },
    "生死劫": {
        "5%伤害": damage_addition_recipe([4036, 25726, 4035, 25725], 51),
        "4%伤害": damage_addition_recipe([4036, 25726, 4035, 25725], 41),
        "3%伤害": damage_addition_recipe([4036, 25726, 4035, 25725], 31),
    },
    "净世破魔击": {
        "5%伤害": damage_addition_recipe([4483 + i for i in range(8)] + [4476] + [26916], 51),
        "4%伤害": damage_addition_recipe([4483 + i for i in range(8)] + [4476] + [26916], 41),
        "3%伤害": damage_addition_recipe([4483 + i for i in range(8)] + [4476] + [26916], 31),
        "5%会心": critical_strike_recipe([4483 + i for i in range(8)] + [4476] + [26916], 500),
        "4%会心": critical_strike_recipe([4483 + i for i in range(8)] + [4476] + [26916], 400),
        "3%会心": critical_strike_recipe([4483 + i for i in range(8)] + [4476] + [26916], 300),
    },
    "驱夜断愁": {
        "5%伤害": damage_addition_recipe([4480, 4482], 51),
        "4%伤害": damage_addition_recipe([4480, 4482], 41),
        "3%伤害": damage_addition_recipe([4480, 4482], 31),
        "5%会心": critical_strike_recipe([4480, 4482], 500),
        "4%会心": critical_strike_recipe([4480, 4482], 400),
        "3%会心": critical_strike_recipe([4480, 4482], 300),
    },
}

RECIPES: Dict[str, List[str]] = {
    "烈日斩": ["10%伤害", "5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "银月斩": ["5%会心", "4%会心", "3%会心"],
    "生死劫": ["5%伤害", "4%伤害", "3%伤害"],
    "净世破魔击": ["5%伤害", "5%会心", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "驱夜断愁": ["5%伤害", "5%会心", "4%伤害", "4%会心", "3%伤害", "3%会心"]
}
