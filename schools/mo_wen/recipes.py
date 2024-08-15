from typing import Dict, List

from base.gain import Gain
from base.recipe import ChannelIntervalRecipe, DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "宫": {
        "增加伤害4%": DamageAdditionRecipe(41, 14064, 14064),
        "增加伤害3%": DamageAdditionRecipe(31, 14064, 14064),
        "增加会心4%": CriticalStrikeRecipe(400, 14064, 14064),
        "增加会心3%": CriticalStrikeRecipe(300, 14064, 14064),
        "增加会心2%": CriticalStrikeRecipe(200, 14064, 14064),
    },
    "商": {
        "增加伤害5%": ChannelIntervalRecipe(1.05, 14065, 14065),
        "增加伤害4%": ChannelIntervalRecipe(1.04, 14065, 14065),
        "增加伤害3%": ChannelIntervalRecipe(1.03, 14065, 14065),
        "增加会心4%": CriticalStrikeRecipe(400, 14065, 14065),
        "增加会心3%": CriticalStrikeRecipe(300, 14065, 14065),
        "增加会心2%": CriticalStrikeRecipe(200, 14065, 14065),
    },
    "徵": {
        "增加伤害4%": DamageAdditionRecipe(41, 14067, 14067),
        "增加伤害3%": DamageAdditionRecipe(31, 14067, 14067),
        "增加会心4%": CriticalStrikeRecipe(400, 14067, 14067),
        "增加会心3%": CriticalStrikeRecipe(300, 14067, 14067),
        "增加会心2%": CriticalStrikeRecipe(200, 14067, 14067),
    },
    "羽": {
        "增加伤害4%": DamageAdditionRecipe(41, 14068, 14068),
        "增加伤害3%": DamageAdditionRecipe(31, 14068, 14068),
        "增加会心4%": CriticalStrikeRecipe(400, 14068, 14068),
        "增加会心3%": CriticalStrikeRecipe(300, 14068, 14068),
    }
}

RECIPES: Dict[str, List[str]] = {
    "宫": ["增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "商": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "徵": ["增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "羽": ["增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%"],
}
