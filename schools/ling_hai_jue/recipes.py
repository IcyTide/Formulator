from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "击水三千": {
        "增加伤害5%": DamageAdditionRecipe(51, 19737, 19737),
        "增加伤害4%": DamageAdditionRecipe(41, 19737, 19737),
        "增加伤害3%": DamageAdditionRecipe(31, 19737, 19737),
        "增加会心4%": CriticalStrikeRecipe(400, 19737, 19737),
        "增加会心3%": CriticalStrikeRecipe(300, 19737, 19737),
        "增加会心2%": CriticalStrikeRecipe(200, 19737, 19737),
    },
    "木落雁归": {
        "增加伤害5%": DamageAdditionRecipe(51, 19818, 19818),
        "增加伤害4%": DamageAdditionRecipe(41, 19818, 19818),
        "增加伤害3%": DamageAdditionRecipe(31, 19818, 19818),
        "增加会心4%": CriticalStrikeRecipe(400, 19818, 19818),
        "增加会心3%": CriticalStrikeRecipe(300, 19818, 19818),
        "增加会心2%": CriticalStrikeRecipe(200, 19818, 19818),
    },
    "海运南冥": {
        "增加伤害4%": DamageAdditionRecipe(41, 20715, 20715),
        "增加伤害3%": DamageAdditionRecipe(31, 20715, 20715),
        "增加伤害2%": DamageAdditionRecipe(21, 20715, 20715),
        "增加会心4%": CriticalStrikeRecipe(400, 20715, 20715),
        "增加会心3%": CriticalStrikeRecipe(300, 20715, 20715),
        "增加会心2%": CriticalStrikeRecipe(200, 20715, 20715),
    },
    "翼绝云天": {
        "增加伤害5%": DamageAdditionRecipe(51, 19827, 19827),
        "增加伤害4%": DamageAdditionRecipe(41, 19827, 19827),
        "增加伤害3%": DamageAdditionRecipe(31, 19827, 19827),
        "增加会心4%": CriticalStrikeRecipe(400, 19827, 19827),
        "增加会心3%": CriticalStrikeRecipe(300, 19827, 19827),
        "增加会心2%": CriticalStrikeRecipe(200, 19827, 19827),
    },
    "振翅图南": {
        "增加伤害5%": DamageAdditionRecipe(51, 20259, 20259),
        "增加伤害4%": DamageAdditionRecipe(41, 20259, 20259),
        "增加伤害3%": DamageAdditionRecipe(31, 20259, 20259),
        "增加会心4%": CriticalStrikeRecipe(400, 20259, 20259),
        "增加会心3%": CriticalStrikeRecipe(300, 20259, 20259),
        "增加会心2%": CriticalStrikeRecipe(200, 20259, 20259),
    },
    "浮游天地": {
        "增加会心4%": CriticalStrikeRecipe(400, 19828, 19828),
        "增加会心3%": CriticalStrikeRecipe(300, 19828, 19828),
        "增加会心2%": CriticalStrikeRecipe(200, 19828, 19828),
    }
}

RECIPES: Dict[str, List[str]] = {
    "击水三千": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "木落雁归": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "海运南冥": ["增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加伤害2%", "增加会心2%"],
    "翼绝云天": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "振翅图南": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "浮游天地": ["增加会心4%", "增加会心3%", "增加会心2%"]
}
