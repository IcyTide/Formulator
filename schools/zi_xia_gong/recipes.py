from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "两仪化形": {
        "5%伤害": DamageAdditionRecipe(51, 301, 301),
        "4%伤害": DamageAdditionRecipe(41, 301, 301),
        "3%伤害": DamageAdditionRecipe(31, 301, 301),
        "4%会心": CriticalStrikeRecipe(400, 301, 301),
        "3%会心": CriticalStrikeRecipe(300, 301, 301),
        "2%会心": CriticalStrikeRecipe(200, 301, 301),
    },
    "四象轮回": {
        "4%会心": CriticalStrikeRecipe(400, 367, 367),
        "3%会心": CriticalStrikeRecipe(300, 367, 367),
        "2%会心": CriticalStrikeRecipe(200, 367, 367),
    },
    "万世不竭": {
        "5%伤害": DamageAdditionRecipe(51, 18640, 18640),
        "4%伤害": DamageAdditionRecipe(41, 18640, 18640),
        "3%伤害": DamageAdditionRecipe(31, 18640, 18640),
    }
}

RECIPES: Dict[str, List[str]] = {
    "两仪化形": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "四象轮回": ["4%会心", "3%会心", "2%会心"],
    "万世不竭": ["5%伤害", "4%伤害", "3%伤害"]
}
