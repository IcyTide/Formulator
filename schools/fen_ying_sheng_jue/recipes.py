from typing import Dict, List

from base.gain import Gain
from base.recipe import MoveStateDamageAdditionRecipe, DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "烈日斩": {
        "10%伤害": MoveStateDamageAdditionRecipe(51, 3963, 0),
        "5%伤害": DamageAdditionRecipe(51, 3963, 0),
        "4%伤害": DamageAdditionRecipe(41, 3963, 0),
        "3%伤害": DamageAdditionRecipe(31, 3963, 0),
        "4%会心": CriticalStrikeRecipe(400, 3963, 0),
        "3%会心": CriticalStrikeRecipe(300, 3963, 0)
    },
    "银月斩": {
        "5%会心": CriticalStrikeRecipe(500, 3960, 3960),
        "4%会心": CriticalStrikeRecipe(400, 3960, 3960),
        "3%会心": CriticalStrikeRecipe(300, 3960, 3960)
    },
    "生死劫": {
        "5%伤害": DamageAdditionRecipe(51, 3966, 3966),
        "4%伤害": DamageAdditionRecipe(41, 3966, 3966),
        "3%伤害": DamageAdditionRecipe(31, 3966, 3966),
    },
    "净世破魔击": {
        "5%伤害": DamageAdditionRecipe(51, 3967, 3967),
        "4%伤害": DamageAdditionRecipe(41, 3967, 3967),
        "3%伤害": DamageAdditionRecipe(31, 3967, 3967),
        "5%会心": CriticalStrikeRecipe(500, 3967, 3967),
        "4%会心": CriticalStrikeRecipe(400, 3967, 3967),
        "3%会心": CriticalStrikeRecipe(300, 3967, 3967),
    },
    "驱夜断愁": {
        "5%伤害": DamageAdditionRecipe(51, 3979, 3979),
        "4%伤害": DamageAdditionRecipe(41, 3979, 3979),
        "3%伤害": DamageAdditionRecipe(31, 3979, 3979),
        "5%会心": CriticalStrikeRecipe(500, 3979, 3979),
        "4%会心": CriticalStrikeRecipe(400, 3979, 3979),
        "3%会心": CriticalStrikeRecipe(300, 3979, 3979),
    },
}

RECIPES: Dict[str, List[str]] = {
    "烈日斩": ["10%伤害", "5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "银月斩": ["5%会心", "4%会心", "3%会心"],
    "生死劫": ["5%伤害", "4%伤害", "3%伤害"],
    "净世破魔击": ["5%伤害", "5%会心", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "驱夜断愁": ["5%伤害", "5%会心", "4%伤害", "4%会心", "3%伤害", "3%会心"]
}
