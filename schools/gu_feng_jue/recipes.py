from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "行云式": {
        "增加伤害5%": DamageAdditionRecipe(51, 32132, 32132),
        "增加伤害4%": DamageAdditionRecipe(41, 32132, 32132),
        "增加伤害3%": DamageAdditionRecipe(31, 32132, 32132),
        "增加会心4%": CriticalStrikeRecipe(400, 32132, 32132),
        "增加会心3%": CriticalStrikeRecipe(300, 32132, 32132),
        "增加会心2%": CriticalStrikeRecipe(200, 32132, 32132),
    },
    "决云势": {
        "增加伤害4%": DamageAdditionRecipe(41, 32134, 32134),
        "增加伤害3%": DamageAdditionRecipe(31, 32134, 32134),
        "增加会心3%": CriticalStrikeRecipe(300, 32134, 32134),
        "增加会心2%": CriticalStrikeRecipe(200, 32134, 32134),
    },
    "断云势": {
        "增加伤害5%": DamageAdditionRecipe(51, 32135, 32135),
        "增加伤害4%": DamageAdditionRecipe(41, 32135, 32135),
        "增加会心4%": CriticalStrikeRecipe(400, 32135, 32135),
        "增加会心3%": CriticalStrikeRecipe(300, 32135, 32135),
    },
    "沧浪三叠": {
        "增加伤害5%": DamageAdditionRecipe(51, 32601, 32601),
        "增加伤害4%": DamageAdditionRecipe(41, 32601, 32601),
        "增加伤害3%": DamageAdditionRecipe(31, 32601, 32601),
        "增加会心4%": CriticalStrikeRecipe(400, 32601, 32601),
        "增加会心3%": CriticalStrikeRecipe(300, 32601, 32601),
        "增加会心2%": CriticalStrikeRecipe(200, 32601, 32601),
    },
    "横云断浪": {
        "增加伤害5%": DamageAdditionRecipe(51, 32144, 32144),
        "增加伤害4%": DamageAdditionRecipe(41, 32144, 32144),
        "增加会心4%": CriticalStrikeRecipe(400, 32144, 32144),
        "增加会心3%": CriticalStrikeRecipe(300, 32144, 32144),
    },
    "孤锋破浪": {
        "增加伤害5%": DamageAdditionRecipe(51, 32145, 32145),
        "增加伤害4%": DamageAdditionRecipe(41, 32145, 32145),
        "增加会心4%": CriticalStrikeRecipe(400, 32145, 32145),
        "增加会心3%": CriticalStrikeRecipe(300, 32145, 32145),
    },
    "留客雨": {
        "增加伤害5%": DamageAdditionRecipe(51, 32146, 32146),
        "增加伤害4%": DamageAdditionRecipe(41, 32146, 32146),
        "增加伤害3%": DamageAdditionRecipe(31, 32146, 32146),
        "增加会心4%": CriticalStrikeRecipe(400, 32146, 32146),
        "增加会心3%": CriticalStrikeRecipe(300, 32146, 32146),
        "增加会心2%": CriticalStrikeRecipe(200, 32146, 32146),
    },
    "触石雨": {
        "增加伤害4%": DamageAdditionRecipe(41, 32148, 32148),
        "增加伤害3%": DamageAdditionRecipe(31, 32148, 32148),
    },
}

RECIPES: Dict[str, List[str]] = {
    "行云式": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "决云势": ["增加伤害4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "断云势": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加会心3%"],
    "沧浪三叠": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "横云断浪": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加会心3%"],
    "孤锋破浪": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加会心3%"],
    "留客雨": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "触石雨": ["增加伤害4%", "增加伤害3%"]
}
