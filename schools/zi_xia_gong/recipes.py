from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "两仪化形": {
        "增加伤害5%": DamageAdditionRecipe(51, 301, 301),
        "增加伤害4%": DamageAdditionRecipe(41, 301, 301),
        "增加伤害3%": DamageAdditionRecipe(31, 301, 301),
        "增加会心4%": CriticalStrikeRecipe(400, 301, 301),
        "增加会心3%": CriticalStrikeRecipe(300, 301, 301),
        "增加会心2%": CriticalStrikeRecipe(200, 301, 301),
    },
    "四象轮回": {
        "增加会心4%": CriticalStrikeRecipe(400, 367, 367),
        "增加会心3%": CriticalStrikeRecipe(300, 367, 367),
        "增加会心2%": CriticalStrikeRecipe(200, 367, 367),
    },
    "万世不竭": {
        "增加伤害5%": DamageAdditionRecipe(51, 18640, 18640),
        "增加伤害4%": DamageAdditionRecipe(41, 18640, 18640),
        "增加伤害3%": DamageAdditionRecipe(31, 18640, 18640),
    }
}

RECIPES: Dict[str, List[str]] = {
    "两仪化形": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "四象轮回": ["增加会心4%", "增加会心3%", "增加会心2%"],
    "万世不竭": ["增加伤害5%", "增加伤害4%", "增加伤害3%"]
}
