from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "阳明指": {
        "4%伤害": DamageAdditionRecipe(41, 179, 179),
        "3%伤害": DamageAdditionRecipe(31, 179, 179),
        "3%会心": CriticalStrikeRecipe(300, 179, 179),
        "2%会心": CriticalStrikeRecipe(200, 179, 179),
    },
    "芙蓉并蒂": {
        "5%伤害": DamageAdditionRecipe(51, 186, 0),
        "4%伤害": DamageAdditionRecipe(41, 186, 0),
        "3%伤害": DamageAdditionRecipe(31, 186, 0),
        "4%会心": CriticalStrikeRecipe(400, 186, 0),
        "3%会心": CriticalStrikeRecipe(300, 186, 0),
        "2%会心": CriticalStrikeRecipe(200, 186, 0),
    },
    "快雪时晴": {
        "5%伤害": DamageAdditionRecipe(51, 2636, 2636),
        "4%伤害": DamageAdditionRecipe(41, 2636, 2636),
        "3%伤害": DamageAdditionRecipe(31, 2636, 2636)
    },
}

RECIPES: Dict[str, List[str]] = {
    "阳明指": ["4%伤害", "3%伤害", "3%会心", "2%会心"],
    "芙蓉并蒂": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "快雪时晴": ["5%伤害", "4%伤害", "3%伤害"],
}
