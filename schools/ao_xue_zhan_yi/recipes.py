from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "穿云": {
        "4%伤害": DamageAdditionRecipe(41, 400, 400),
        "3%伤害": DamageAdditionRecipe(31, 400, 400),
        "3%会心": CriticalStrikeRecipe(300, 400, 400),
        "2%会心": CriticalStrikeRecipe(200, 400, 400),
    },
    "龙吟": {
        "5%伤害": DamageAdditionRecipe(51, 403, 403),
        "4%伤害": DamageAdditionRecipe(41, 403, 403),
        "3%伤害": DamageAdditionRecipe(31, 403, 403),
    },
    "龙牙": {
        "5%伤害": DamageAdditionRecipe(51, 415, 415),
        "4%伤害": DamageAdditionRecipe(41, 415, 415),
        "3%伤害": DamageAdditionRecipe(31, 415, 415),
        "4%会心": CriticalStrikeRecipe(400, 415, 415),
        "3%会心": CriticalStrikeRecipe(300, 415, 415),
        "2%会心": CriticalStrikeRecipe(200, 415, 415),
    },
    "灭": {
        "4%伤害": DamageAdditionRecipe(41, 423, 423),
        "3%伤害": DamageAdditionRecipe(31, 423, 423),
        "3%会心": CriticalStrikeRecipe(300, 423, 423),
        "2%会心": CriticalStrikeRecipe(200, 423, 423),
    },
    "突": {
        "4%伤害": DamageAdditionRecipe(41, 418, 418),
        "3%伤害": DamageAdditionRecipe(31, 418, 418),
    },
    "断魂刺": {
        "4%伤害": DamageAdditionRecipe(41, 428, 428),
        "3%伤害": DamageAdditionRecipe(31, 428, 428),
    }
}

RECIPES: Dict[str, List[str]] = {
    "穿云": ["4%伤害", "3%伤害", "3%会心", "2%会心"],
    "龙吟": ["5%伤害", "4%伤害", "3%伤害"],
    "龙牙": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "灭": ["4%伤害", "3%伤害", "3%会心", "2%会心"],
    "突": ["4%伤害", "3%伤害"],
    "断魂刺": ["4%伤害", "3%伤害"]
}
