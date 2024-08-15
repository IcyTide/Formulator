from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe, PveAdditionRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "劲风簇": {
        "增加伤害3%": DamageAdditionRecipe(31, 35659, 35659),
        "增加伤害2%": DamageAdditionRecipe(21, 35659, 35659),
        "增加会心4%": CriticalStrikeRecipe(400, 35659, 35659),
        "增加会心3%": CriticalStrikeRecipe(300, 35659, 35659),
    },
    "饮羽簇": {
        "增加伤害15%": PveAdditionRecipe(154, 35661, 35661),
        "增加伤害3%": DamageAdditionRecipe(31, 35661, 35661),
        "增加伤害2%": DamageAdditionRecipe(21, 35661, 35661),
        "增加会心4%": CriticalStrikeRecipe(400, 35661, 35661),
        "增加会心3%": CriticalStrikeRecipe(300, 35661, 35661),
    },
}

RECIPES: Dict[str, List[str]] = {
    "劲风簇": ["增加会心4%", "增加伤害3%", "增加会心3%", "增加伤害2%"],
    "饮羽簇": ["增加伤害15%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加伤害2%"],
}
