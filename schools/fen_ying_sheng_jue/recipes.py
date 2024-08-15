from typing import Dict, List

from base.gain import Gain
from base.recipe import MoveStateDamageAdditionRecipe, DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "烈日斩": {
        "增加伤害10%": MoveStateDamageAdditionRecipe(51, 3963, 0),
        "增加伤害5%": DamageAdditionRecipe(51, 3963, 0),
        "增加伤害4%": DamageAdditionRecipe(41, 3963, 0),
        "增加伤害3%": DamageAdditionRecipe(31, 3963, 0),
        "增加会心4%": CriticalStrikeRecipe(400, 3963, 0),
        "增加会心3%": CriticalStrikeRecipe(300, 3963, 0)
    },
    "银月斩": {
        "增加会心5%": CriticalStrikeRecipe(500, 3960, 3960),
        "增加会心4%": CriticalStrikeRecipe(400, 3960, 3960),
        "增加会心3%": CriticalStrikeRecipe(300, 3960, 3960)
    },
    "生死劫": {
        "增加伤害5%": DamageAdditionRecipe(51, 3966, 3966),
        "增加伤害4%": DamageAdditionRecipe(41, 3966, 3966),
        "增加伤害3%": DamageAdditionRecipe(31, 3966, 3966),
    },
    "净世破魔击": {
        "增加伤害5%": DamageAdditionRecipe(51, 3967, 3967),
        "增加伤害4%": DamageAdditionRecipe(41, 3967, 3967),
        "增加伤害3%": DamageAdditionRecipe(31, 3967, 3967),
        "增加会心5%": CriticalStrikeRecipe(500, 3967, 3967),
        "增加会心4%": CriticalStrikeRecipe(400, 3967, 3967),
        "增加会心3%": CriticalStrikeRecipe(300, 3967, 3967),
    },
    "驱夜断愁": {
        "增加伤害5%": DamageAdditionRecipe(51, 3979, 3979),
        "增加伤害4%": DamageAdditionRecipe(41, 3979, 3979),
        "增加伤害3%": DamageAdditionRecipe(31, 3979, 3979),
        "增加会心5%": CriticalStrikeRecipe(500, 3979, 3979),
        "增加会心4%": CriticalStrikeRecipe(400, 3979, 3979),
        "增加会心3%": CriticalStrikeRecipe(300, 3979, 3979),
    },
}

RECIPES: Dict[str, List[str]] = {
    "烈日斩": ["增加伤害10%", "增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%"],
    "银月斩": ["增加会心5%", "增加会心4%", "增加会心3%"],
    "生死劫": ["增加伤害5%", "增加伤害4%", "增加伤害3%"],
    "净世破魔击": ["增加伤害5%", "增加会心5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%"],
    "驱夜断愁": ["增加伤害5%", "增加会心5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%"]
}
