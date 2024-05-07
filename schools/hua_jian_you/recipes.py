from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "阳明指": {
        "4%伤害": damage_addition_recipe([14941], 41),
        "3%伤害": damage_addition_recipe([14941], 31),
        "3%会心": critical_strike_recipe([14941], 300),
        "2%会心": critical_strike_recipe([14941], 200),
    },
    "芙蓉并蒂": {
        "5%伤害": damage_addition_recipe([186], 51),
        "4%伤害": damage_addition_recipe([186], 41),
        "3%伤害": damage_addition_recipe([186], 31),
        "4%会心": critical_strike_recipe([186], 400),
        "3%会心": critical_strike_recipe([186], 300),
        "2%会心": critical_strike_recipe([186], 200),
    },
    "快雪时晴": {
        "5%伤害": damage_addition_recipe([33222], 51),
        "4%伤害": damage_addition_recipe([33222], 41),
        "3%伤害": damage_addition_recipe([33222], 31)
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
