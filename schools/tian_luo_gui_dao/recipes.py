from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe, PrepareFrameRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "暴雨梨花针": {
        "增加伤害5%": DamageAdditionRecipe(51, 3093, 3093),
        "增加伤害4%": DamageAdditionRecipe(41, 3093, 3093),
        "增加伤害3%": DamageAdditionRecipe(31, 3093, 3093),
        "增加会心4%": CriticalStrikeRecipe(400, 3093, 3093),
        "增加会心3%": CriticalStrikeRecipe(300, 3093, 3093),
    },
    "蚀肌弹": {
        "-0.125运功": PrepareFrameRecipe(-2, 3105, 3105),
        "增加伤害5%": DamageAdditionRecipe(51, 3105, 3105),
        "增加伤害4%": DamageAdditionRecipe(41, 3105, 3105),
        "增加伤害3%": DamageAdditionRecipe(31, 3105, 3105),
        "增加会心4%": CriticalStrikeRecipe(400, 3105, 3105),
        "增加会心3%": CriticalStrikeRecipe(300, 3105, 3105),
    },
    "天绝地灭": {
        "增加伤害5%": DamageAdditionRecipe(51, 3108, 3108),
        "增加伤害4%": DamageAdditionRecipe(41, 3108, 3108),
        "增加伤害3%": DamageAdditionRecipe(31, 3108, 3108),
    },
    "暗藏杀机": {
        "增加伤害5%": DamageAdditionRecipe(51, 3111, 3111),
        "增加伤害4%": DamageAdditionRecipe(41, 3111, 3111),
        "增加伤害3%": DamageAdditionRecipe(31, 3111, 3111),
        "增加会心2%": CriticalStrikeRecipe(200, 3111, 3111),
    },
}

RECIPES: Dict[str, List[str]] = {
    "暴雨梨花针": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%"],
    "蚀肌弹": ["-0.125运功", "-0.125运功", "增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%"],
    "天绝地灭": ["增加伤害5%", "增加伤害4%", "增加伤害3%"],
    "暗藏杀机": ["增加伤害5%", "增加伤害4%", "增加伤害3%", "增加会心2%"],
}
