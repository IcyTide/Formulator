from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "普渡四方": {
        "增加伤害5%": DamageAdditionRecipe(51, 232, 232),
        "增加伤害4%": DamageAdditionRecipe(41, 232, 232),
        "增加伤害3%": DamageAdditionRecipe(31, 232, 232),
    },
    "横扫六合": {
        "增加伤害50%": DamageAdditionRecipe(512, 235, 235),
    },
    "韦陀献杵": {
        "增加伤害5%": DamageAdditionRecipe(51, 233, 233),
        "增加伤害4%": DamageAdditionRecipe(41, 233, 233),
        "增加伤害3%": DamageAdditionRecipe(31, 233, 233),
        "增加会心4%": CriticalStrikeRecipe(400, 233, 233),
        "增加会心3%": CriticalStrikeRecipe(300, 233, 233),
        "增加会心2%": CriticalStrikeRecipe(200, 233, 233),
    },
    "捕风式": {
        "增加伤害15%": DamageAdditionRecipe(150, 238, 238),
        "增加伤害10%": DamageAdditionRecipe(102, 238, 238),
    },
    "守缺式": {
        "增加伤害5%": DamageAdditionRecipe(51, 2572, 2572),
        "增加伤害4%": DamageAdditionRecipe(41, 2572, 2572),
        "增加伤害3%": DamageAdditionRecipe(31, 2572, 2572),
        "增加会心4%": CriticalStrikeRecipe(400, 2572, 2572),
        "增加会心3%": CriticalStrikeRecipe(300, 2572, 2572),
        "增加会心2%": CriticalStrikeRecipe(200, 2572, 2572),
    },
    "拿云式": {
        "增加伤害5%": DamageAdditionRecipe(51, 243, 243),
        "增加伤害4%": DamageAdditionRecipe(41, 243, 243),
        "增加伤害3%": DamageAdditionRecipe(31, 243, 243)
    },
}

RECIPES: Dict[str, List[str]] = {
    "普渡四方": ["增加伤害5%", "增加伤害4%", "增加伤害3%"],
    "横扫六合": ["增加伤害50%"],
    "韦陀献杵": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "捕风式": ["增加伤害15%", "增加伤害10%", "增加伤害10%"],
    "守缺式": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "拿云式": ["增加伤害5%", "增加伤害4%", "增加伤害3%"],
}
