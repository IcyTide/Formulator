from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "恶狗拦路": {
        "5%伤害": DamageAdditionRecipe(51, 5361, 5361),
        "4%伤害": DamageAdditionRecipe(41, 5361, 5361),
        "3%伤害": DamageAdditionRecipe(31, 5361, 5361),
    },
    "龙腾五岳": {
        "4%伤害": DamageAdditionRecipe(41, 5370, 5370),
        "3%伤害": DamageAdditionRecipe(31, 5370, 5370),
        "5%会心": CriticalStrikeRecipe(500, 5370, 5370),
        "4%会心": CriticalStrikeRecipe(400, 5370, 5370),
        "3%会心": CriticalStrikeRecipe(300, 5370, 5370),
    },
    "龙战于野": {
        "5%伤害": DamageAdditionRecipe(51, 5266, 5266),
        "4%伤害": DamageAdditionRecipe(41, 5266, 5266),
        "3%伤害": DamageAdditionRecipe(31, 5266, 5266),
        "3%会心": CriticalStrikeRecipe(300, 5266, 5266),
        "2%会心": CriticalStrikeRecipe(200, 5266, 5266),
    },
    "龙跃于渊": {
        "5%伤害": DamageAdditionRecipe(51, 5262, 5262),
        "4%伤害": DamageAdditionRecipe(41, 5262, 5262),
        "3%伤害": DamageAdditionRecipe(31, 5262, 5262),
    },
    "亢龙有悔": {
        "5%伤害": DamageAdditionRecipe(51, 5638, 5638),
        "4%伤害": DamageAdditionRecipe(41, 5638, 5638),
        "3%伤害": DamageAdditionRecipe(31, 5638, 5638),
        "4%会心": CriticalStrikeRecipe(400, 5638, 5638),
        "3%会心": CriticalStrikeRecipe(300, 5638, 5638),
    }
}

RECIPES: Dict[str, List[str]] = {
    "恶狗拦路": ["5%伤害", "4%伤害", "3%伤害"],
    "龙腾五岳": ["5%会心", "4%伤害", "4%会心", "3%伤害", "3%会心"],
    "龙战于野": ["5%伤害", "4%伤害", "3%伤害", "3%会心", "2%会心"],
    "龙跃于渊": ["5%伤害", "4%伤害", "3%伤害"],
    "亢龙有悔": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心"],
}
