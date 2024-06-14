from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe, PrepareFrameRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "暴雨梨花针": {
        "5%伤害": DamageAdditionRecipe(51, 3093, 3093),
        "4%伤害": DamageAdditionRecipe(41, 3093, 3093),
        "3%伤害": DamageAdditionRecipe(31, 3093, 3093),
        "4%会心": CriticalStrikeRecipe(400, 3093, 3093),
        "3%会心": CriticalStrikeRecipe(300, 3093, 3093),
    },
    "蚀肌弹": {
        "-0.125运功": PrepareFrameRecipe(-2, 3105, 3105),
        "5%伤害": DamageAdditionRecipe(51, 3105, 3105),
        "4%伤害": DamageAdditionRecipe(41, 3105, 3105),
        "3%伤害": DamageAdditionRecipe(31, 3105, 3105),
        "4%会心": CriticalStrikeRecipe(400, 3105, 3105),
        "3%会心": CriticalStrikeRecipe(300, 3105, 3105),
    },
    "天绝地灭": {
        "5%伤害": DamageAdditionRecipe(51, 3108, 3108),
        "4%伤害": DamageAdditionRecipe(41, 3108, 3108),
        "3%伤害": DamageAdditionRecipe(31, 3108, 3108),
    },
    "暗藏杀机": {
        "5%伤害": DamageAdditionRecipe(51, 3111, 3111),
        "4%伤害": DamageAdditionRecipe(41, 3111, 3111),
        "3%伤害": DamageAdditionRecipe(31, 3111, 3111),
        "2%会心": CriticalStrikeRecipe(200, 3111, 3111),
    },
}

RECIPES: Dict[str, List[str]] = {
    "暴雨梨花针": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "蚀肌弹": ["-0.125运功", "-0.125运功", "5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "天绝地灭": ["5%伤害", "4%伤害", "3%伤害"],
    "暗藏杀机": ["5%伤害", "4%伤害", "3%伤害", "2%会心"],
}
