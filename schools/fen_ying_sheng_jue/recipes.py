from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "普渡四方": {
        "5%伤害": damage_addition_recipe([17641], 51),
        "4%伤害": damage_addition_recipe([17641], 41),
        "3%伤害": damage_addition_recipe([17641], 31),
    },
    "横扫六合": {
        "50%伤害": damage_addition_recipe([3810], 512),
    },
    "韦陀献杵": {
        "5%伤害": damage_addition_recipe([3848, 3849, 3850, 271], 51),
        "4%伤害": damage_addition_recipe([3848, 3849, 3850, 271], 41),
        "3%伤害": damage_addition_recipe([3848, 3849, 3850, 271], 31),
        "4%会心": critical_strike_recipe([3848, 3849, 3850], 400),
        "3%会心": critical_strike_recipe([3848, 3849, 3850], 300),
        "2%会心": critical_strike_recipe([3848, 3849, 3850], 200),
    },
    "捕风式": {
        "15%伤害": damage_addition_recipe([14951], 150),
        "10%伤害": damage_addition_recipe([14951], 102),
    },
    "守缺式": {
        "5%伤害": damage_addition_recipe([3814, 3816], 51),
        "4%伤害": damage_addition_recipe([3814, 3816], 41),
        "3%伤害": damage_addition_recipe([3814, 3816], 31),
        "4%会心": critical_strike_recipe([3814, 3816], 400),
        "3%会心": critical_strike_recipe([3814, 3816], 300),
        "2%会心": critical_strike_recipe([3814, 3816], 200),
    },
    "拿云式": {
        "5%伤害": damage_addition_recipe([13685], 51),
        "4%伤害": damage_addition_recipe([13685], 41),
        "3%伤害": damage_addition_recipe([13685], 31)
    },
}

RECIPES: Dict[str, List[str]] = {
    "普渡四方": ["5%伤害", "4%伤害", "3%伤害"],
    "横扫六合": ["50%伤害"],
    "韦陀献杵": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "捕风式": ["15%伤害", "10%伤害", "10%伤害"],
    "守缺式": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "拿云式": ["5%伤害", "4%伤害", "3%伤害"],
}
