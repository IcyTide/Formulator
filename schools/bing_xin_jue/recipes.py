from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "玳弦急曲": {
        "5%伤害": DamageAdditionRecipe(51, 2707, 2707),
        "4%伤害": DamageAdditionRecipe(41, 2707, 2707),
        "3%伤害": DamageAdditionRecipe(31, 2707, 2707),
    },
    "剑气长江": {
        "6%伤害": DamageAdditionRecipe(61, 561, 561),
        "4%伤害": DamageAdditionRecipe(41, 561, 561),
        "3%会心": CriticalStrikeRecipe(300, 561, 561),
        "2%会心": CriticalStrikeRecipe(200, 561, 561),
    },
    "江海凝光": {
        "15%伤害": DamageAdditionRecipe(154, 553, 553),
        "3%会心": CriticalStrikeRecipe(300, 553, 553),
        "2%会心": CriticalStrikeRecipe(200, 553, 553),
    },
}

RECIPES: Dict[str, List[str]] = {
    "玳弦急曲": ["5%伤害", "4%伤害", "3%伤害"],
    "剑气长江": ["6%伤害", "4%伤害", "3%会心", "2%会心"],
    "江海凝光": ["15%伤害", "15%伤害", "3%会心", "2%会心"],
}
