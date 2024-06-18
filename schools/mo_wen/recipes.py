from typing import Dict, List

from base.gain import Gain
from base.recipe import ChannelIntervalRecipe, DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "宫": {
        "4%伤害": DamageAdditionRecipe(41, 14064, 14064),
        "3%伤害": DamageAdditionRecipe(31, 14064, 14064),
        "4%会心": CriticalStrikeRecipe(400, 14064, 14064),
        "3%会心": CriticalStrikeRecipe(300, 14064, 14064),
        "2%会心": CriticalStrikeRecipe(200, 14064, 14064),
    },
    "商": {
        "5%伤害": ChannelIntervalRecipe(1.05, 14065, 14065),
        "4%伤害": ChannelIntervalRecipe(1.04, 14065, 14065),
        "3%伤害": ChannelIntervalRecipe(1.03, 14065, 14065),
        "4%会心": CriticalStrikeRecipe(400, 14065, 14065),
        "3%会心": CriticalStrikeRecipe(300, 14065, 14065),
        "2%会心": CriticalStrikeRecipe(200, 14065, 14065),
    },
    "徵": {
        "4%伤害": DamageAdditionRecipe(41, 14067, 14067),
        "3%伤害": DamageAdditionRecipe(31, 14067, 14067),
        "4%会心": CriticalStrikeRecipe(400, 14067, 14067),
        "3%会心": CriticalStrikeRecipe(300, 14067, 14067),
        "2%会心": CriticalStrikeRecipe(200, 14067, 14067),
    },
    "羽": {
        "4%伤害": DamageAdditionRecipe(41, 14068, 14068),
        "3%伤害": DamageAdditionRecipe(31, 14068, 14068),
        "4%会心": CriticalStrikeRecipe(400, 14068, 14068),
        "3%会心": CriticalStrikeRecipe(300, 14068, 14068),
    }
}

RECIPES: Dict[str, List[str]] = {
    "宫": ["4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "商": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "徵": ["4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "羽": ["4%伤害", "4%会心", "3%伤害", "3%会心"],
}
