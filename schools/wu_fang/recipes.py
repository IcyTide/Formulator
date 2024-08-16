from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "商陆缀寒": {
        "3%伤害": DamageAdditionRecipe(31, 27551, 27551),
        "2%伤害": DamageAdditionRecipe(20, 27551, 27551),
        "4%会心": CriticalStrikeRecipe(400, 27551, 27551),
        "3%会心": CriticalStrikeRecipe(300, 27551, 27551),
    },
    "钩吻断肠": {
        "3%伤害": DamageAdditionRecipe(41, 27554, 27554),
        "2%伤害": DamageAdditionRecipe(31, 27554, 27554),
        "4%会心": CriticalStrikeRecipe(400, 27554, 27554),
        "3%会心": CriticalStrikeRecipe(300, 27554, 27554),
        "2%会心": CriticalStrikeRecipe(200, 27554, 27554),
    },
    "川乌射罔": {
        "3%伤害": DamageAdditionRecipe(31, 27556, 27556),
        "2%伤害": DamageAdditionRecipe(20, 27556, 27556),
        "4%会心": CriticalStrikeRecipe(400, 27556, 27556),
        "3%会心": CriticalStrikeRecipe(300, 27556, 27556),
    },
    "且待时休": {
        "3%伤害": DamageAdditionRecipe(31, 27582, 27582),
        "2%伤害": DamageAdditionRecipe(20, 27582, 27582),
    },
    "银光照雪": {
        "3%伤害": DamageAdditionRecipe(31, 28345, 28345),
        "2%伤害": DamageAdditionRecipe(20, 28345, 28345),
        "5%会心": CriticalStrikeRecipe(500, 28345, 28345),
        "4%会心": CriticalStrikeRecipe(400, 28345, 28345),
    },
}

RECIPES: Dict[str, List[str]] = {
    "商陆缀寒": ["4%会心", "3%伤害", "3%会心", "2%伤害"],
    "钩吻断肠": ["4%会心", "3%伤害", "3%会心", "2%伤害", "2%会心"],
    "川乌射罔": ["4%会心", "3%伤害", "3%会心", "2%伤害"],
    "且待时休": ["3%伤害", "2%伤害"],
    "银光照雪": ["5%会心", "4%会心", "3%伤害", "2%伤害"],
}
