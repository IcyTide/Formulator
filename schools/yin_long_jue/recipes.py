from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "星垂平野": {
        "5%伤害": DamageAdditionRecipe(51, 22143, 22143),
        "4%伤害": DamageAdditionRecipe(41, 22143, 22143),
        "3%伤害": DamageAdditionRecipe(31, 22143, 22143),
        "4%会心": CriticalStrikeRecipe(400, 22143, 22143),
        "3%会心": CriticalStrikeRecipe(300, 22143, 22143),
        "2%会心": CriticalStrikeRecipe(200, 22143, 22143),
    },
    "金戈回澜": {
        "5%伤害": DamageAdditionRecipe(51, 22144, 22144),
        "4%伤害": DamageAdditionRecipe(41, 22144, 22144),
        "4%会心": CriticalStrikeRecipe(400, 22144, 22144),
        "3%会心": CriticalStrikeRecipe(300, 22144, 22144),
    },
    "寂洪荒": {
        "5%伤害": DamageAdditionRecipe(51, 22327, 22327),
        "4%伤害": DamageAdditionRecipe(41, 22327, 22327),
        "3%伤害": DamageAdditionRecipe(31, 22327, 22327),
    },
    "乱天狼": {
        "5%伤害": DamageAdditionRecipe(51, 22320, 22320),
        "4%伤害": DamageAdditionRecipe(41, 22320, 22320),
        "3%伤害": DamageAdditionRecipe(31, 22320, 22320),
        "4%会心": CriticalStrikeRecipe(400, 22320, 22320),
        "3%会心": CriticalStrikeRecipe(300, 22320, 22320),
        "2%会心": CriticalStrikeRecipe(200, 22320, 22320),
    },
    "隐风雷": {
        "5%伤害": DamageAdditionRecipe(51, 22321, 22321),
        "4%伤害": DamageAdditionRecipe(41, 22321, 22321),
        "3%伤害": DamageAdditionRecipe(31, 22321, 22321),
        "4%会心": CriticalStrikeRecipe(400, 22321, 22321),
        "3%会心": CriticalStrikeRecipe(300, 22321, 22321),
        "2%会心": CriticalStrikeRecipe(200, 22321, 22321),
    },
    "斩无常": {
        "5%伤害": DamageAdditionRecipe(51, 22358, 22358),
        "4%伤害": DamageAdditionRecipe(41, 22358, 22358),
        "4%会心": CriticalStrikeRecipe(400, 22358, 22358),
        "3%会心": CriticalStrikeRecipe(300, 22358, 22358),
    },
    "幽冥窥月": {
        "5%伤害": DamageAdditionRecipe(51, 22361, 22361),
        "3%会心": CriticalStrikeRecipe(300, 22361, 22361),
        "2%会心": CriticalStrikeRecipe(200, 22361, 22361),
    }
}

RECIPES: Dict[str, List[str]] = {
    "星垂平野": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "金戈回澜": ["5%伤害", "4%伤害", "4%会心", "3%会心"],
    "寂洪荒": ["5%伤害", "4%伤害", "3%伤害"],
    "乱天狼": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "隐风雷": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "斩无常": ["5%伤害", "4%伤害", "4%会心", "3%会心"],
    "幽冥窥月": ["5%伤害", "5%伤害", "3%会心", "2%会心"],
}
