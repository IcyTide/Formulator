from typing import Dict, List

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "九溪弥烟": {
        "增加伤害5%": DamageAdditionRecipe(51, 1579, 1579),
        "增加伤害4%": DamageAdditionRecipe(41, 1579, 1579),
        "增加伤害3%": DamageAdditionRecipe(31, 1579, 1579),
        "增加会心3%": CriticalStrikeRecipe(300, 1579, 1579),
        "增加会心2%": CriticalStrikeRecipe(200, 1579, 1579),
    },
    "黄龙吐翠": {
        "增加伤害5%": DamageAdditionRecipe(51, 1581, 1581),
        "增加伤害4%": DamageAdditionRecipe(41, 1581, 1581),
        "增加伤害3%": DamageAdditionRecipe(31, 1581, 1581),
        "增加会心4%": CriticalStrikeRecipe(400, 1581, 1581),
        "增加会心3%": CriticalStrikeRecipe(300, 1581, 1581),
        "增加会心2%": CriticalStrikeRecipe(200, 1581, 1581),
    },
    "云飞玉皇": {
        "增加伤害4%": DamageAdditionRecipe(41, 1593, 1593),
        "增加伤害3%": DamageAdditionRecipe(31, 1593, 1593),
        "增加伤害2%": DamageAdditionRecipe(21, 1593, 1593),
        "增加会心3%": CriticalStrikeRecipe(300, 1593, 1593),
    },
    "夕照雷峰": {
        "增加伤害4%": DamageAdditionRecipe(41, 1600, 1600),
        "增加伤害3%": DamageAdditionRecipe(31, 1600, 1600),
        "增加伤害2%": DamageAdditionRecipe(21, 1600, 1600),
        "增加会心3%": CriticalStrikeRecipe(300, 1600, 1600),
    },
    "鹤归孤山": {
        "增加伤害5%": DamageAdditionRecipe(51, 18322, 1596),
        "增加伤害4%": DamageAdditionRecipe(41, 18322, 1596),
        "增加伤害3%": DamageAdditionRecipe(31, 18322, 1596),
        "增加会心2%": CriticalStrikeRecipe(200, 18322, 1596),
    },
    "风来吴山": {
        "增加伤害4%": Gains(gains=[DamageAdditionRecipe(41, skill_id, skill_id) for skill_id in (1645, 18333)]),
        "增加伤害3%": Gains(gains=[DamageAdditionRecipe(31, skill_id, skill_id) for skill_id in (1645, 18333)]),
        "增加伤害2%": Gains(gains=[DamageAdditionRecipe(21, skill_id, skill_id) for skill_id in (1645, 18333)]),
        "增加会心3%": Gains(gains=[CriticalStrikeRecipe(300, skill_id, skill_id) for skill_id in (1645, 18333)]),
        "增加会心2%": Gains(gains=[CriticalStrikeRecipe(200, skill_id, skill_id) for skill_id in (1645, 18333)]),
    },
    "听雷": {
        "增加伤害5%": DamageAdditionRecipe(51, 1646, 1646),
        "增加伤害4%": DamageAdditionRecipe(41, 1646, 1646),
        "增加伤害3%": DamageAdditionRecipe(31, 1646, 1646),
        "增加会心3%": CriticalStrikeRecipe(300, 1646, 1646),
        "增加会心2%": CriticalStrikeRecipe(200, 1646, 1646),
    },

}

RECIPES: Dict[str, List[str]] = {
    "九溪弥烟": ["增加伤害5%", "增加伤害4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "黄龙吐翠": ["增加伤害5%", "增加伤害4%", "增加会心4%", "增加伤害3%", "增加会心3%", "增加会心2%"],
    "云飞玉皇": ["增加伤害4%", "增加伤害3%", "增加会心3%", "增加伤害2%"],
    "夕照雷峰": ["增加伤害4%", "增加伤害3%", "增加会心3%", "增加伤害2%"],
    "鹤归孤山": ["增加伤害5%", "增加伤害4%", "增加伤害3%", "增加会心2%"],
    "风来吴山": ["增加伤害4%", "增加伤害3%", "增加会心3%", "增加伤害2%", "增加会心2%"],
    "听雷": ["增加伤害5%", "增加伤害4%", "增加伤害3%", "增加会心3%", "增加会心2%"]
}
