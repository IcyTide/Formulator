from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "星垂平野": {
        "增加伤害5%": DamageAdditionRecipe(51, 22143, 22143),
        "增加伤害4%": DamageAdditionRecipe(41, 22143, 22143),
        "增加伤害3%": DamageAdditionRecipe(31, 22143, 22143),
        "增加会心4%": CriticalStrikeRecipe(400, 22143, 22143),
        "增加会心3%": CriticalStrikeRecipe(300, 22143, 22143),
        "增加会心2%": CriticalStrikeRecipe(200, 22143, 22143),
    },
    "金戈回澜": {
        "增加伤害5%": DamageAdditionRecipe(51, 22144, 22144),
        "增加伤害4%": DamageAdditionRecipe(41, 22144, 22144),
        "增加会心4%": CriticalStrikeRecipe(400, 22144, 22144),
        "增加会心3%": CriticalStrikeRecipe(300, 22144, 22144),
    },
    "寂洪荒": {
        "增加伤害5%": DamageAdditionRecipe(51, 22327, 22327),
        "增加伤害4%": DamageAdditionRecipe(41, 22327, 22327),
        "增加伤害3%": DamageAdditionRecipe(31, 22327, 22327),
    },
    "乱天狼": {
        "增加伤害5%": DamageAdditionRecipe(51, 22320, 22320),
        "增加伤害4%": DamageAdditionRecipe(41, 22320, 22320),
        "增加伤害3%": DamageAdditionRecipe(31, 22320, 22320),
        "增加会心4%": CriticalStrikeRecipe(400, 22320, 22320),
        "增加会心3%": CriticalStrikeRecipe(300, 22320, 22320),
        "增加会心2%": CriticalStrikeRecipe(200, 22320, 22320),
    },
    "隐风雷": {
        "增加伤害5%": DamageAdditionRecipe(51, 22321, 22321),
        "增加伤害4%": DamageAdditionRecipe(41, 22321, 22321),
        "增加伤害3%": DamageAdditionRecipe(31, 22321, 22321),
        "增加会心4%": CriticalStrikeRecipe(400, 22321, 22321),
        "增加会心3%": CriticalStrikeRecipe(300, 22321, 22321),
        "增加会心2%": CriticalStrikeRecipe(200, 22321, 22321),
    },
    "斩无常": {
        "增加伤害5%": DamageAdditionRecipe(51, 22358, 22358),
        "增加伤害4%": DamageAdditionRecipe(41, 22358, 22358),
        "增加会心4%": CriticalStrikeRecipe(400, 22358, 22358),
        "增加会心3%": CriticalStrikeRecipe(300, 22358, 22358),
    },
    "幽冥窥月": {
        "增加伤害5%": DamageAdditionRecipe(51, 22361, 22361),
        "增加会心3%": CriticalStrikeRecipe(300, 22361, 22361),
        "增加会心2%": CriticalStrikeRecipe(200, 22361, 22361),
    }
}

RECIPES: Dict[str, List[str]] = {
    "星垂平野": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "金戈回澜": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加会心3%"],
    "寂洪荒": ["增加伤害5%", "增加伤害4%", "增加伤害3%"],
    "乱天狼": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "隐风雷": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "斩无常": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加会心3%"],
    "幽冥窥月": ["增加伤害5%", "增加伤害5%", "增加会心3%", "增加会心2%"],
}
