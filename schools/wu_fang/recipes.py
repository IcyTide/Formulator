from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "商陆缀寒": {
        "增加伤害3%": DamageAdditionRecipe(31, 27551, 27551),
        "增加伤害2%": DamageAdditionRecipe(21, 27551, 27551),
        "增加会心4%": CriticalStrikeRecipe(400, 27551, 27551),
        "增加会心3%": CriticalStrikeRecipe(300, 27551, 27551),
    },
    "钩吻断肠": {
        "增加伤害3%": DamageAdditionRecipe(41, 27554, 27554),
        "增加伤害2%": DamageAdditionRecipe(31, 27554, 27554),
        "增加会心4%": CriticalStrikeRecipe(400, 27554, 27554),
        "增加会心3%": CriticalStrikeRecipe(300, 27554, 27554),
        "增加会心2%": CriticalStrikeRecipe(200, 27554, 27554),
    },
    "川乌射罔": {
        "增加伤害3%": DamageAdditionRecipe(31, 27556, 27556),
        "增加伤害2%": DamageAdditionRecipe(21, 27556, 27556),
        "增加会心4%": CriticalStrikeRecipe(400, 27556, 27556),
        "增加会心3%": CriticalStrikeRecipe(300, 27556, 27556),
    },
    "且待时休": {
        "增加伤害3%": DamageAdditionRecipe(31, 27582, 27582),
        "增加伤害2%": DamageAdditionRecipe(21, 27582, 27582),
    },
    "银光照雪": {
        "增加伤害3%": DamageAdditionRecipe(31, 28345, 28345),
        "增加伤害2%": DamageAdditionRecipe(21, 28345, 28345),
        "增加会心5%": CriticalStrikeRecipe(500, 28345, 28345),
        "增加会心4%": CriticalStrikeRecipe(400, 28345, 28345),
    },
}

RECIPES: Dict[str, List[str]] = {
    "商陆缀寒": ["增加会心4%", "增加伤害3%", "增加会心3%", "增加伤害2%"],
    "钩吻断肠": ["增加会心4%", "增加伤害3%", "增加会心3%", "增加伤害2%", "增加会心2%"],
    "川乌射罔": ["增加会心4%", "增加伤害3%", "增加会心3%", "增加伤害2%"],
    "且待时休": ["增加伤害3%", "增加伤害2%"],
    "银光照雪": ["增加会心5%", "增加会心4%", "增加伤害3%", "增加伤害2%"],
}
