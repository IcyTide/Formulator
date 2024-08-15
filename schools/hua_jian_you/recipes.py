from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "阳明指": {
        "增加伤害4%": DamageAdditionRecipe(41, 179, 179),
        "增加伤害3%": DamageAdditionRecipe(31, 179, 179),
        "增加会心3%": CriticalStrikeRecipe(300, 179, 179),
        "增加会心2%": CriticalStrikeRecipe(200, 179, 179),
    },
    "芙蓉并蒂": {
        "增加伤害5%": DamageAdditionRecipe(51, 186, 0),
        "增加伤害4%": DamageAdditionRecipe(41, 186, 0),
        "增加伤害3%": DamageAdditionRecipe(31, 186, 0),
        "增加会心4%": CriticalStrikeRecipe(400, 186, 0),
        "增加会心3%": CriticalStrikeRecipe(300, 186, 0),
        "增加会心2%": CriticalStrikeRecipe(200, 186, 0),
    },
    "快雪时晴": {
        "增加伤害5%": DamageAdditionRecipe(51, 2636, 2636),
        "增加伤害4%": DamageAdditionRecipe(41, 2636, 2636),
        "增加伤害3%": DamageAdditionRecipe(31, 2636, 2636)
    },
}

RECIPES: Dict[str, List[str]] = {
    "阳明指": ["增加伤害4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "芙蓉并蒂": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "快雪时晴": ["增加伤害5%", "增加伤害4%", "增加伤害3%"],
}
