from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "普渡四方": {
        "5%伤害": DamageAdditionRecipe(51, 232, 232),
        "4%伤害": DamageAdditionRecipe(41, 232, 232),
        "3%伤害": DamageAdditionRecipe(31, 232, 232),
    },
    "横扫六合": {
        "50%伤害": DamageAdditionRecipe(512, 235, 235),
    },
    "韦陀献杵": {
        "5%伤害": DamageAdditionRecipe(51, 233, 233),
        "4%伤害": DamageAdditionRecipe(41, 233, 233),
        "3%伤害": DamageAdditionRecipe(31, 233, 233),
        "4%会心": CriticalStrikeRecipe(400, 233, 233),
        "3%会心": CriticalStrikeRecipe(300, 233, 233),
        "2%会心": CriticalStrikeRecipe(200, 233, 233),
    },
    "捕风式": {
        "15%伤害": DamageAdditionRecipe(150, 238, 238),
        "10%伤害": DamageAdditionRecipe(102, 238, 238),
    },
    "守缺式": {
        "5%伤害": DamageAdditionRecipe(51, 2572, 2572),
        "4%伤害": DamageAdditionRecipe(41, 2572, 2572),
        "3%伤害": DamageAdditionRecipe(31, 2572, 2572),
        "4%会心": CriticalStrikeRecipe(400, 2572, 2572),
        "3%会心": CriticalStrikeRecipe(300, 2572, 2572),
        "2%会心": CriticalStrikeRecipe(200, 2572, 2572),
    },
    "拿云式": {
        "5%伤害": DamageAdditionRecipe(51, 243, 243),
        "4%伤害": DamageAdditionRecipe(41, 243, 243),
        "3%伤害": DamageAdditionRecipe(31, 243, 243)
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
