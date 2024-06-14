from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "盾刀": {
        "5%伤害": DamageAdditionRecipe(51, 13044, 13044),
        "4%伤害": DamageAdditionRecipe(41, 13044, 13044),
        "3%伤害": DamageAdditionRecipe(31, 13044, 13044),
        "4%会心": CriticalStrikeRecipe(400, 13044, 13044),
        "3%会心": CriticalStrikeRecipe(300, 13044, 13044),
        "2%会心": CriticalStrikeRecipe(200, 13044, 13044),
    },
    "盾压": {
        "5%伤害": DamageAdditionRecipe(51, 13045, 13045),
        "4%伤害": DamageAdditionRecipe(41, 13045, 13045),
        "4%会心": CriticalStrikeRecipe(400, 13045, 13045),
        "3%会心": CriticalStrikeRecipe(300, 13045, 13045),
    },
    "劫刀": {
        "5%伤害": DamageAdditionRecipe(51, 13052, 13052),
        "4%伤害": DamageAdditionRecipe(41, 13052, 13052),
        "3%伤害": DamageAdditionRecipe(31, 13052, 13052),
        "4%会心": CriticalStrikeRecipe(400, 13052, 13052),
        "3%会心": CriticalStrikeRecipe(300, 13052, 13052),
        "2%会心": CriticalStrikeRecipe(200, 13052, 13052),
    },
    "斩刀": {
        "5%伤害": DamageAdditionRecipe(41, 13054, 13054),
        "4%伤害": DamageAdditionRecipe(31, 13054, 13054),
        "3%伤害": DamageAdditionRecipe(21, 13054, 13054),
        "4%会心": CriticalStrikeRecipe(400, 13054, 13054),
        "3%会心": CriticalStrikeRecipe(300, 13054, 13054),
        "2%会心": CriticalStrikeRecipe(200, 13054, 13054),
    },
    "绝刀": {
        "5%伤害": DamageAdditionRecipe(51, 13055, 13055),
        "4%伤害": DamageAdditionRecipe(41, 13055, 13055),
        "4%会心": CriticalStrikeRecipe(400, 13055, 13055),
        "3%会心": CriticalStrikeRecipe(300, 13055, 13055),
    },
    "盾飞": {
        "4%伤害": DamageAdditionRecipe(41, 13050, 13050),
        "3%伤害": DamageAdditionRecipe(31, 13050, 13050),
        "3%会心": CriticalStrikeRecipe(300, 13050, 13050),
        "2%会心": CriticalStrikeRecipe(200, 13050, 13050),
    },
}

RECIPES: Dict[str, List[str]] = {
    "盾刀": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "盾压": ["5%伤害", "4%伤害", "4%会心", "3%会心"],
    "劫刀": ["4%伤害", "4%会心", "3%伤害", "3%会心", "2%伤害", "2%会心"],
    "斩刀": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "绝刀": ["5%伤害", "4%伤害", "4%会心", "3%会心"],
    "盾飞": ["4%伤害", "3%伤害", "3%会心", "2%会心"],
}
