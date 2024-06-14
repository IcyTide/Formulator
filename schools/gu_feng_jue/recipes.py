from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "行云式": {
        "5%伤害": DamageAdditionRecipe(51, 32132, 32132),
        "4%伤害": DamageAdditionRecipe(41, 32132, 32132),
        "3%伤害": DamageAdditionRecipe(31, 32132, 32132),
        "4%会心": CriticalStrikeRecipe(400, 32132, 32132),
        "3%会心": CriticalStrikeRecipe(300, 32132, 32132),
        "2%会心": CriticalStrikeRecipe(200, 32132, 32132),
    },
    "决云势": {
        "4%伤害": DamageAdditionRecipe(41, 32134, 32134),
        "3%伤害": DamageAdditionRecipe(31, 32134, 32134),
        "3%会心": CriticalStrikeRecipe(300, 32134, 32134),
        "2%会心": CriticalStrikeRecipe(200, 32134, 32134),
    },
    "断云势": {
        "5%伤害": DamageAdditionRecipe(51, 32135, 32135),
        "4%伤害": DamageAdditionRecipe(41, 32135, 32135),
        "4%会心": CriticalStrikeRecipe(400, 32135, 32135),
        "3%会心": CriticalStrikeRecipe(300, 32135, 32135),
    },
    "沧浪三叠": {
        "5%伤害": DamageAdditionRecipe(51, 32601, 32601),
        "4%伤害": DamageAdditionRecipe(41, 32601, 32601),
        "3%伤害": DamageAdditionRecipe(31, 32601, 32601),
        "4%会心": CriticalStrikeRecipe(400, 32601, 32601),
        "3%会心": CriticalStrikeRecipe(300, 32601, 32601),
        "2%会心": CriticalStrikeRecipe(200, 32601, 32601),
    },
    "横云断浪": {
        "5%伤害": DamageAdditionRecipe(51, 32144, 32144),
        "4%伤害": DamageAdditionRecipe(41, 32144, 32144),
        "4%会心": CriticalStrikeRecipe(400, 32144, 32144),
        "3%会心": CriticalStrikeRecipe(300, 32144, 32144),
    },
    "孤锋破浪": {
        "5%伤害": DamageAdditionRecipe(51, 32145, 32145),
        "4%伤害": DamageAdditionRecipe(41, 32145, 32145),
        "4%会心": CriticalStrikeRecipe(400, 32145, 32145),
        "3%会心": CriticalStrikeRecipe(300, 32145, 32145),
    },
    "留客雨": {
        "5%伤害": DamageAdditionRecipe(51, 32146, 32146),
        "4%伤害": DamageAdditionRecipe(41, 32146, 32146),
        "3%伤害": DamageAdditionRecipe(31, 32146, 32146),
        "4%会心": CriticalStrikeRecipe(400, 32146, 32146),
        "3%会心": CriticalStrikeRecipe(300, 32146, 32146),
        "2%会心": CriticalStrikeRecipe(200, 32146, 32146),
    },
    "触石雨": {
        "4%伤害": DamageAdditionRecipe(41, 32148, 32148),
        "3%伤害": DamageAdditionRecipe(31, 32148, 32148),
    },
}

RECIPES: Dict[str, List[str]] = {
    "行云式": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "决云势": ["4%伤害", "3%伤害", "3%会心", "2%会心"],
    "断云势": ["5%伤害", "4%伤害", "4%会心", "3%会心"],
    "沧浪三叠": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "横云断浪": ["5%伤害", "4%伤害", "4%会心", "3%会心"],
    "孤锋破浪": ["5%伤害", "4%伤害", "4%会心", "3%会心"],
    "留客雨": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "触石雨": ["4%伤害", "3%伤害"]
}
