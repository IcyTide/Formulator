from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "击水三千": {
        "5%伤害": DamageAdditionRecipe(51, 19737, 19737),
        "4%伤害": DamageAdditionRecipe(41, 19737, 19737),
        "3%伤害": DamageAdditionRecipe(31, 19737, 19737),
        "4%会心": CriticalStrikeRecipe(400, 19737, 19737),
        "3%会心": CriticalStrikeRecipe(300, 19737, 19737),
        "2%会心": CriticalStrikeRecipe(200, 19737, 19737),
    },
    "木落雁归": {
        "5%伤害": DamageAdditionRecipe(51, 19818, 19818),
        "4%伤害": DamageAdditionRecipe(41, 19818, 19818),
        "3%伤害": DamageAdditionRecipe(31, 19818, 19818),
        "4%会心": CriticalStrikeRecipe(400, 19818, 19818),
        "3%会心": CriticalStrikeRecipe(300, 19818, 19818),
        "2%会心": CriticalStrikeRecipe(200, 19818, 19818),
    },
    "海运南冥": {
        "4%伤害": DamageAdditionRecipe(41, 20082, 20082),
        "3%伤害": DamageAdditionRecipe(31, 20082, 20082),
        "2%伤害": DamageAdditionRecipe(21, 20082, 20082),
        "4%会心": CriticalStrikeRecipe(400, 20082, 20082),
        "3%会心": CriticalStrikeRecipe(300, 20082, 20082),
        "2%会心": CriticalStrikeRecipe(200, 20082, 20082),
    },
    "翼绝云天": {
        "5%伤害": DamageAdditionRecipe(51, 19827, 19827),
        "4%伤害": DamageAdditionRecipe(41, 19827, 19827),
        "3%伤害": DamageAdditionRecipe(31, 19827, 19827),
        "4%会心": CriticalStrikeRecipe(400, 19827, 19827),
        "3%会心": CriticalStrikeRecipe(300, 19827, 19827),
        "2%会心": CriticalStrikeRecipe(200, 19827, 19827),
    },
    "振翅图南": {
        "5%伤害": DamageAdditionRecipe(51, 20259, 20259),
        "4%伤害": DamageAdditionRecipe(41, 20259, 20259),
        "3%伤害": DamageAdditionRecipe(31, 20259, 20259),
        "4%会心": CriticalStrikeRecipe(400, 20259, 20259),
        "3%会心": CriticalStrikeRecipe(300, 20259, 20259),
        "2%会心": CriticalStrikeRecipe(200, 20259, 20259),
    },
    "浮游天地": {
        "4%会心": CriticalStrikeRecipe(400, 19828, 19828),
        "3%会心": CriticalStrikeRecipe(300, 19828, 19828),
        "2%会心": CriticalStrikeRecipe(200, 19828, 19828),
    }
}

RECIPES: Dict[str, List[str]] = {
    "击水三千": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "木落雁归": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "海运南冥": ["4%伤害", "4%会心", "3%伤害", "3%会心", "2%伤害", "2%会心"],
    "翼绝云天": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "振翅图南": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "浮游天地": ["4%会心", "3%会心", "2%会心"]
}
