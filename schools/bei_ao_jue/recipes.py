from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "雷走风切": {
        "5%伤害": DamageAdditionRecipe(51, 16598, 16598),
        "4%伤害": DamageAdditionRecipe(41, 16598, 16598),
        "3%伤害": DamageAdditionRecipe(31, 16598, 16598),
        "4%会心": CriticalStrikeRecipe(400, 16598, 16598),
        "3%会心": CriticalStrikeRecipe(300, 16598, 16598),
        "2%会心": CriticalStrikeRecipe(200, 16598, 16598),
    },
    "项王击鼎": {
        "5%伤害": DamageAdditionRecipe(51, 16601, 16601),
        "4%伤害": DamageAdditionRecipe(41, 16601, 16601),
        "3%伤害": DamageAdditionRecipe(31, 16601, 16601),
        "4%会心": CriticalStrikeRecipe(400, 16601, 16601),
        "3%会心": CriticalStrikeRecipe(300, 16601, 16601),
        "2%会心": CriticalStrikeRecipe(200, 16601, 16601),
    },
    "破釜沉舟": {
        "5%伤害": DamageAdditionRecipe(51, 16602, 16602),
        "4%伤害": DamageAdditionRecipe(41, 16602, 16602),
        "3%伤害": DamageAdditionRecipe(31, 16602, 16602),
        "4%会心": CriticalStrikeRecipe(400, 16602, 16602),
        "3%会心": CriticalStrikeRecipe(300, 16602, 16602),
        "2%会心": CriticalStrikeRecipe(200, 16602, 16602),
    },
    "上将军印": {
        "4%伤害": DamageAdditionRecipe(41, 16627, 16627),
        "3%伤害": DamageAdditionRecipe(31, 16627, 16627),
        "2%伤害": DamageAdditionRecipe(21, 16627, 16627),
        "4%会心": CriticalStrikeRecipe(400, 16627, 16627),
        "3%会心": CriticalStrikeRecipe(300, 16627, 16627),
        "2%会心": CriticalStrikeRecipe(200, 16627, 16627),
    },
    "擒龙六斩": {
        "5%伤害": DamageAdditionRecipe(51, 16870, 16870),
        "4%伤害": DamageAdditionRecipe(41, 16870, 16870),
        "3%伤害": DamageAdditionRecipe(31, 16870, 16870),
        "4%会心": CriticalStrikeRecipe(400, 16870, 16870),
        "3%会心": CriticalStrikeRecipe(300, 16870, 16870),
        "2%会心": CriticalStrikeRecipe(200, 16870, 16870),
    },
    "刀啸风吟": {
        "5%伤害": DamageAdditionRecipe(51, 16027, 16027),
        "4%伤害": DamageAdditionRecipe(41, 16027, 16027),
        "4%会心": CriticalStrikeRecipe(400, 16027, 16027),
        "3%会心": CriticalStrikeRecipe(300, 16027, 16027),
        "2%会心": CriticalStrikeRecipe(200, 16027, 16027),
    }
}

RECIPES: Dict[str, List[str]] = {
    "雷走风切": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "项王击鼎": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "破釜沉舟": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "上将军印": ["4%伤害", "4%会心", "3%伤害", "3%会心", "2%伤害", "2%会心"],
    "擒龙六斩": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "刀啸风吟": ["5%伤害", "4%伤害", "4%会心", "3%会心", "2%会心"]
}
