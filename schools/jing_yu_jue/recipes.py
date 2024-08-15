from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe, ChannelIntervalRecipe, PrepareFrameRecipe, \
    PhysicalShieldGainRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "暴雨梨花针": {
        "增加伤害5%": DamageAdditionRecipe(51, 3093, 3093),
        "增加伤害4%": DamageAdditionRecipe(41, 3093, 3093),
        "增加伤害3%": DamageAdditionRecipe(31, 3093, 3093),
        "增加会心4%": CriticalStrikeRecipe(400, 3093, 3093),
        "增加会心3%": CriticalStrikeRecipe(300, 3093, 3093),
    },
    "夺魄箭": {
        "-0.125运功": PrepareFrameRecipe(-2, 3095, 3095),
        "增加伤害4%": DamageAdditionRecipe(41, 3095, 3095),
        "增加伤害3%": DamageAdditionRecipe(31, 3095, 3095),
        "增加会心5%": CriticalStrikeRecipe(500, 3095, 3095),
        "增加会心4%": CriticalStrikeRecipe(400, 3095, 3095),
        "增加会心3%": CriticalStrikeRecipe(300, 3095, 3095),
    },
    "追命箭": {
        "20%无视防御": PhysicalShieldGainRecipe(-205, 3096, 3096),
        "增加伤害5%": DamageAdditionRecipe(51, 3096, 3096),
        "增加伤害4%": DamageAdditionRecipe(41, 3096, 3096),
        "增加伤害3%": DamageAdditionRecipe(31, 3096, 3096),
        "增加会心4%": CriticalStrikeRecipe(400, 3096, 3096),
        "增加会心3%": CriticalStrikeRecipe(300, 3096, 3096),
    },
    "逐星箭": {
        "增加伤害5%": DamageAdditionRecipe(51, 3101, 3101),
        "增加伤害4%": DamageAdditionRecipe(41, 3101, 3101),
        "增加伤害3%": DamageAdditionRecipe(31, 3101, 3101),
    },
    "穿心弩": {
        "增加伤害10%": ChannelIntervalRecipe(1.1, 3098, 3098),
        "增加伤害5%": ChannelIntervalRecipe(1.05, 3098, 3098)
    }
}

RECIPES: Dict[str, List[str]] = {
    "暴雨梨花针": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%"],
    "夺魄箭": ["-0.125运功", "-0.125运功", "增加会心5%", "增加伤害4%", "增加会心4%", "增加伤害3%"],
    "追命箭": ["20%无视防御", "增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%"],
    "逐星箭": ["增加伤害5%", "增加伤害4%", "增加伤害3%"],
    "穿心弩": ["增加伤害10%", "增加伤害5%"],
}
