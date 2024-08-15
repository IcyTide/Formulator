from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "三环套月": {
        "增加伤害5%": DamageAdditionRecipe(51, 364, 364),
        "增加伤害4%": DamageAdditionRecipe(41, 364, 364),
        "增加伤害3%": DamageAdditionRecipe(31, 364, 364),
        "增加会心4%": CriticalStrikeRecipe(400, 364, 364),
        "增加会心3%": CriticalStrikeRecipe(300, 364, 364),
        "增加会心2%": CriticalStrikeRecipe(200, 364, 364),
    },
    "无我无剑": {
        "增加伤害5%": DamageAdditionRecipe(51, 365, 365),
        "增加伤害4%": DamageAdditionRecipe(41, 365, 365),
        "增加伤害3%": DamageAdditionRecipe(31, 365, 365),
        "增加会心4%": CriticalStrikeRecipe(400, 365, 365),
        "增加会心3%": CriticalStrikeRecipe(300, 365, 365),
        "增加会心2%": CriticalStrikeRecipe(200, 365, 365),
    },
    "八荒归元": {
        "增加伤害5%": DamageAdditionRecipe(51, 2699, 2699),
        "增加伤害4%": DamageAdditionRecipe(41, 2699, 2699),
        "增加伤害3%": DamageAdditionRecipe(31, 2699, 2699),
    },
    "人剑合一": {
        "增加伤害60%": DamageAdditionRecipe(614, 588, 588),
        "增加伤害40%": DamageAdditionRecipe(410, 588, 588),
    }
}

RECIPES: Dict[str, List[str]] = {
    "三环套月": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "无我无剑": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "八荒归元": ["增加伤害5%", "增加伤害4%", "增加伤害3%"],
    "人剑合一": ["增加伤害60%", "增加伤害40%"]
}
