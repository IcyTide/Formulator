from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "星垂平野": {
        "5%伤害": damage_addition_recipe([22170, 22550, 22551, 22298], 51),
        "4%伤害": damage_addition_recipe([22170, 22550, 22551, 22298], 41),
        "3%伤害": damage_addition_recipe([22170, 22550, 22551, 22298], 31),
        "4%会心": critical_strike_recipe([22170, 22550, 22551, 22298], 400),
        "3%会心": critical_strike_recipe([22170, 22550, 22551, 22298], 300),
        "2%会心": critical_strike_recipe([22170, 22550, 22551, 22298], 200),
    },
    "金戈回澜": {
        "5%伤害": damage_addition_recipe([22621, 22620], 51),
        "4%伤害": damage_addition_recipe([22621, 22620], 41),
        "4%会心": critical_strike_recipe([22621, 22620], 400),
        "3%会心": critical_strike_recipe([22621, 22620], 300),
    },
    "寂洪荒": {
        "5%伤害": damage_addition_recipe([22604, 22605, 36267, 36268], 51),
        "4%伤害": damage_addition_recipe([22604, 22605, 36267, 36268], 41),
        "3%伤害": damage_addition_recipe([22604, 22605, 36267, 36268], 31),
    },
    "乱天狼": {
        "5%伤害": damage_addition_recipe([22490, 22554, 36265, 36266], 51),
        "4%伤害": damage_addition_recipe([22490, 22554, 36265, 36266], 41),
        "3%伤害": damage_addition_recipe([22490, 22554, 36265, 36266], 31),
        "4%会心": critical_strike_recipe([22490, 22554, 36265, 36266], 400),
        "3%会心": critical_strike_recipe([22490, 22554, 36265, 36266], 300),
        "2%会心": critical_strike_recipe([22490, 22554, 36265, 36266], 200),
    },
    "隐风雷": {
        "5%伤害": damage_addition_recipe([22610, 22611, 22612, 36269, 36270], 51),
        "4%伤害": damage_addition_recipe([22610, 22611, 22612, 36269, 36270], 41),
        "3%伤害": damage_addition_recipe([22610, 22611, 22612, 36269, 36270], 31),
        "4%会心": critical_strike_recipe([22610, 22611, 22612, 36269, 36270], 400),
        "3%会心": critical_strike_recipe([22610, 22611, 22612, 36269, 36270], 300),
        "2%会心": critical_strike_recipe([22610, 22611, 22612, 36269, 36270], 200),
    },
    "斩无常": {
        "5%伤害": damage_addition_recipe([], 51),
        "4%伤害": damage_addition_recipe([], 41),
        "4%会心": critical_strike_recipe([], 400),
        "3%会心": critical_strike_recipe([], 300),
    },
    "幽冥窥月": {
        "5%伤害": damage_addition_recipe([22787], 51),
        "3%会心": critical_strike_recipe([22787], 300),
        "2%会心": critical_strike_recipe([22787], 200),
    }
}

RECIPES: Dict[str, List[str]] = {
    "星垂平野": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "金戈回澜": ["5%伤害", "4%伤害", "4%会心", "3%会心"],
    "寂洪荒": ["5%伤害", "4%伤害", "3%伤害"],
    "乱天狼": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "隐风雷": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "斩无常": ["5%伤害", "4%伤害", "4%会心", "3%会心"],
    "幽冥窥月": ["5%伤害", "5%伤害", "3%会心", "2%会心"],
}
