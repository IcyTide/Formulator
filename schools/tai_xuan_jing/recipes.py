from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "三星临": {
        "5%伤害": DamageAdditionRecipe(51, 24369, 24369),
        "4%伤害": DamageAdditionRecipe(41, 24369, 24369),
        "3%伤害": DamageAdditionRecipe(31, 24369, 24369),
        "4%会心": CriticalStrikeRecipe(400, 24369, 24369),
        "3%会心": CriticalStrikeRecipe(300, 24369, 24369),
        "2%会心": CriticalStrikeRecipe(200, 24369, 24369),
    },
    "兵主逆": {
        "5%伤害": DamageAdditionRecipe(51, 24371, 24371),
        "4%伤害": DamageAdditionRecipe(41, 24371, 24371),
        "3%伤害": DamageAdditionRecipe(31, 24371, 24371),
        "4%会心": CriticalStrikeRecipe(400, 24371, 24371),
        "3%会心": CriticalStrikeRecipe(300, 24371, 24371),
    },
    "天斗旋": {
        "5%伤害": DamageAdditionRecipe(51, 24372, 24372),
        "4%伤害": DamageAdditionRecipe(41, 24372, 24372),
        "3%伤害": DamageAdditionRecipe(31, 24372, 24372),
        "4%会心": CriticalStrikeRecipe(400, 24372, 24372),
        "3%会心": CriticalStrikeRecipe(300, 24372, 24372),
        "2%会心": CriticalStrikeRecipe(200, 24372, 24372),
    },
    "鬼星开穴": {
        "5%伤害": DamageAdditionRecipe(51, 24379, 24379),
        "4%伤害": DamageAdditionRecipe(41, 24379, 24379),
        "4%会心": CriticalStrikeRecipe(400, 24379, 24379),
        "3%会心": CriticalStrikeRecipe(300, 24379, 24379),
    },
}

RECIPES: Dict[str, List[str]] = {
    "三星临": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "兵主逆": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "天斗旋": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "鬼星开穴": ["5%伤害", "4%伤害", "4%会心", "3%会心"]
}
