from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "恶狗拦路": {
        "增加伤害5%": DamageAdditionRecipe(51, 5361, 5361),
        "增加伤害4%": DamageAdditionRecipe(41, 5361, 5361),
        "增加伤害3%": DamageAdditionRecipe(31, 5361, 5361),
    },
    "龙腾五岳": {
        "增加伤害4%": DamageAdditionRecipe(41, 5370, 5370),
        "增加伤害3%": DamageAdditionRecipe(31, 5370, 5370),
        "增加会心5%": CriticalStrikeRecipe(500, 5370, 5370),
        "增加会心4%": CriticalStrikeRecipe(400, 5370, 5370),
        "增加会心3%": CriticalStrikeRecipe(300, 5370, 5370),
    },
    "龙战于野": {
        "增加伤害5%": DamageAdditionRecipe(51, 5266, 5266),
        "增加伤害4%": DamageAdditionRecipe(41, 5266, 5266),
        "增加伤害3%": DamageAdditionRecipe(31, 5266, 5266),
        "增加会心3%": CriticalStrikeRecipe(300, 5266, 5266),
        "增加会心2%": CriticalStrikeRecipe(200, 5266, 5266),
    },
    "龙跃于渊": {
        "增加伤害5%": DamageAdditionRecipe(51, 5262, 5262),
        "增加伤害4%": DamageAdditionRecipe(41, 5262, 5262),
        "增加伤害3%": DamageAdditionRecipe(31, 5262, 5262),
    },
    "亢龙有悔": {
        "增加伤害5%": DamageAdditionRecipe(51, 5638, 5638),
        "增加伤害4%": DamageAdditionRecipe(41, 5638, 5638),
        "增加伤害3%": DamageAdditionRecipe(31, 5638, 5638),
        "增加会心4%": CriticalStrikeRecipe(400, 5638, 5638),
        "增加会心3%": CriticalStrikeRecipe(300, 5638, 5638),
    }
}

RECIPES: Dict[str, List[str]] = {
    "恶狗拦路": ["增加伤害5%", "增加伤害4%", "增加伤害3%"],
    "龙腾五岳": ["增加会心5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%"],
    "龙战于野": ["增加伤害5%", "增加伤害4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "龙跃于渊": ["增加伤害5%", "增加伤害4%", "增加伤害3%"],
    "亢龙有悔": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%"],
}
