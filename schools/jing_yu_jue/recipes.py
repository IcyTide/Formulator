from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe, ChannelIntervalRecipe, PrepareFrameRecipe, \
    PhysicalShieldGainRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "暴雨梨花针": {
        "5%伤害": DamageAdditionRecipe(51, 3093, 3093),
        "4%伤害": DamageAdditionRecipe(41, 3093, 3093),
        "3%伤害": DamageAdditionRecipe(31, 3093, 3093),
        "4%会心": CriticalStrikeRecipe(400, 3093, 3093),
        "3%会心": CriticalStrikeRecipe(300, 3093, 3093),
    },
    "夺魄箭": {
        "-0.125运功": PrepareFrameRecipe(-2, 3095, 3095),
        "4%伤害": DamageAdditionRecipe(41, 3095, 3095),
        "3%伤害": DamageAdditionRecipe(31, 3095, 3095),
        "5%会心": CriticalStrikeRecipe(500, 3095, 3095),
        "4%会心": CriticalStrikeRecipe(400, 3095, 3095),
        "3%会心": CriticalStrikeRecipe(300, 3095, 3095),
    },
    "追命箭": {
        "20%无视防御": PhysicalShieldGainRecipe(-205, 3096, 3096),
        "5%伤害": DamageAdditionRecipe(51, 3096, 3096),
        "4%伤害": DamageAdditionRecipe(41, 3096, 3096),
        "3%伤害": DamageAdditionRecipe(31, 3096, 3096),
        "4%会心": CriticalStrikeRecipe(400, 3096, 3096),
        "3%会心": CriticalStrikeRecipe(300, 3096, 3096),
    },
    "逐星箭": {
        "5%伤害": DamageAdditionRecipe(51, 3101, 3101),
        "4%伤害": DamageAdditionRecipe(41, 3101, 3101),
        "3%伤害": DamageAdditionRecipe(31, 3101, 3101),
    },
    "穿心弩": {
        "10%伤害": ChannelIntervalRecipe(1.1, 3098, 3098),
        "5%伤害": ChannelIntervalRecipe(1.05, 3098, 3098)
    }
}

RECIPES: Dict[str, List[str]] = {
    "暴雨梨花针": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "夺魄箭": ["-0.125运功", "-0.125运功", "5%会心", "4%伤害", "4%会心", "3%伤害"],
    "追命箭": ["20%无视防御", "5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "逐星箭": ["5%伤害", "4%伤害", "3%伤害"],
    "穿心弩": ["10%伤害", "5%伤害"],
}
