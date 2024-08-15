from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "三星临": {
        "增加伤害5%": DamageAdditionRecipe(51, 24369, 24369),
        "增加伤害4%": DamageAdditionRecipe(41, 24369, 24369),
        "增加伤害3%": DamageAdditionRecipe(31, 24369, 24369),
        "增加会心4%": CriticalStrikeRecipe(400, 24369, 24369),
        "增加会心3%": CriticalStrikeRecipe(300, 24369, 24369),
        "增加会心2%": CriticalStrikeRecipe(200, 24369, 24369),
    },
    "兵主逆": {
        "增加伤害5%": DamageAdditionRecipe(51, 24371, 24371),
        "增加伤害4%": DamageAdditionRecipe(41, 24371, 24371),
        "增加伤害3%": DamageAdditionRecipe(31, 24371, 24371),
        "增加会心4%": CriticalStrikeRecipe(400, 24371, 24371),
        "增加会心3%": CriticalStrikeRecipe(300, 24371, 24371),
    },
    "天斗旋": {
        "增加伤害5%": DamageAdditionRecipe(51, 24372, 24372),
        "增加伤害4%": DamageAdditionRecipe(41, 24372, 24372),
        "增加伤害3%": DamageAdditionRecipe(31, 24372, 24372),
        "增加会心4%": CriticalStrikeRecipe(400, 24372, 24372),
        "增加会心3%": CriticalStrikeRecipe(300, 24372, 24372),
        "增加会心2%": CriticalStrikeRecipe(200, 24372, 24372),
    },
    "鬼星开穴": {
        "增加伤害5%": DamageAdditionRecipe(51, 24379, 24379),
        "增加伤害4%": DamageAdditionRecipe(41, 24379, 24379),
        "增加会心4%": CriticalStrikeRecipe(400, 24379, 24379),
        "增加会心3%": CriticalStrikeRecipe(300, 24379, 24379),
    },
}

RECIPES: Dict[str, List[str]] = {
    "三星临": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "兵主逆": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%"],
    "天斗旋": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "鬼星开穴": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加会心3%"]
}
