from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "三环套月": {
        "5%伤害": DamageAdditionRecipe(51, 364, 364),
        "4%伤害": DamageAdditionRecipe(41, 364, 364),
        "3%伤害": DamageAdditionRecipe(31, 364, 364),
        "4%会心": CriticalStrikeRecipe(400, 364, 364),
        "3%会心": CriticalStrikeRecipe(300, 364, 364),
        "2%会心": CriticalStrikeRecipe(200, 364, 364),
    },
    "无我无剑": {
        "5%伤害": DamageAdditionRecipe(51, 365, 365),
        "4%伤害": DamageAdditionRecipe(41, 365, 365),
        "3%伤害": DamageAdditionRecipe(31, 365, 365),
        "4%会心": CriticalStrikeRecipe(400, 365, 365),
        "3%会心": CriticalStrikeRecipe(300, 365, 365),
        "2%会心": CriticalStrikeRecipe(200, 365, 365),
    },
    "八荒归元": {
        "5%伤害": DamageAdditionRecipe(51, 2699, 2699),
        "4%伤害": DamageAdditionRecipe(41, 2699, 2699),
        "3%伤害": DamageAdditionRecipe(31, 2699, 2699),
    },
    "人剑合一": {
        "60%伤害": DamageAdditionRecipe(614, 588, 588),
        "40%伤害": DamageAdditionRecipe(410, 588, 588),
    }
}

RECIPES: Dict[str, List[str]] = {
    "三环套月": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "无我无剑": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "八荒归元": ["5%伤害", "4%伤害", "3%伤害"],
    "人剑合一": ["60%伤害", "40%伤害"]
}
