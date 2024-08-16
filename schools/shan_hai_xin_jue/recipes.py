from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe, PveAdditionRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "劲风簇": {
        "3%伤害": DamageAdditionRecipe(31, 35659, 35659),
        "2%伤害": DamageAdditionRecipe(20, 35659, 35659),
        "4%会心": CriticalStrikeRecipe(400, 35659, 35659),
        "3%会心": CriticalStrikeRecipe(300, 35659, 35659),
    },
    "饮羽簇": {
        "15%伤害": PveAdditionRecipe(154, 35661, 35661),
        "3%伤害": DamageAdditionRecipe(31, 35661, 35661),
        "2%伤害": DamageAdditionRecipe(20, 35661, 35661),
        "4%会心": CriticalStrikeRecipe(400, 35661, 35661),
        "3%会心": CriticalStrikeRecipe(300, 35661, 35661),
    },
}

RECIPES: Dict[str, List[str]] = {
    "劲风簇": ["4%会心", "3%伤害", "3%会心", "2%伤害"],
    "饮羽簇": ["15%伤害", "4%会心", "3%伤害", "3%会心", "2%伤害"],
}
