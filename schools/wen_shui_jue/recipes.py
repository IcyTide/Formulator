from typing import Dict, List

from base.gain import Gain, Gains
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "九溪弥烟": {
        "5%伤害": DamageAdditionRecipe(51, 1579, 1579),
        "4%伤害": DamageAdditionRecipe(41, 1579, 1579),
        "3%伤害": DamageAdditionRecipe(31, 1579, 1579),
        "3%会心": CriticalStrikeRecipe(300, 1579, 1579),
        "2%会心": CriticalStrikeRecipe(200, 1579, 1579),
    },
    "黄龙吐翠": {
        "5%伤害": DamageAdditionRecipe(51, 1581, 1581),
        "4%伤害": DamageAdditionRecipe(41, 1581, 1581),
        "3%伤害": DamageAdditionRecipe(31, 1581, 1581),
        "4%会心": CriticalStrikeRecipe(400, 1581, 1581),
        "3%会心": CriticalStrikeRecipe(300, 1581, 1581),
        "2%会心": CriticalStrikeRecipe(200, 1581, 1581),
    },
    "云飞玉皇": {
        "4%伤害": DamageAdditionRecipe(41, 1593, 1593),
        "3%伤害": DamageAdditionRecipe(31, 1593, 1593),
        "2%伤害": DamageAdditionRecipe(21, 1593, 1593),
        "3%会心": CriticalStrikeRecipe(300, 1593, 1593),
    },
    "夕照雷峰": {
        "4%伤害": DamageAdditionRecipe(41, 1600, 1600),
        "3%伤害": DamageAdditionRecipe(31, 1600, 1600),
        "2%伤害": DamageAdditionRecipe(21, 1600, 1600),
        "3%会心": CriticalStrikeRecipe(300, 1600, 1600),
    },
    "鹤归孤山": {
        "5%伤害": DamageAdditionRecipe(51, 18322, 1596),
        "4%伤害": DamageAdditionRecipe(41, 18322, 1596),
        "3%伤害": DamageAdditionRecipe(31, 18322, 1596),
        "2%会心": CriticalStrikeRecipe(200, 18322, 1596),
    },
    "风来吴山": {
        "4%伤害": Gains(gains=[DamageAdditionRecipe(41, skill_id, skill_id) for skill_id in (1645, 18333)]),
        "3%伤害": Gains(gains=[DamageAdditionRecipe(31, skill_id, skill_id) for skill_id in (1645, 18333)]),
        "2%伤害": Gains(gains=[DamageAdditionRecipe(21, skill_id, skill_id) for skill_id in (1645, 18333)]),
        "3%会心": Gains(gains=[CriticalStrikeRecipe(300, skill_id, skill_id) for skill_id in (1645, 18333)]),
        "2%会心": Gains(gains=[CriticalStrikeRecipe(200, skill_id, skill_id) for skill_id in (1645, 18333)]),
    },
    "听雷": {
        "5%伤害": DamageAdditionRecipe(51, 1646, 1646),
        "4%伤害": DamageAdditionRecipe(41, 1646, 1646),
        "3%伤害": DamageAdditionRecipe(31, 1646, 1646),
        "3%会心": CriticalStrikeRecipe(300, 1646, 1646),
        "2%会心": CriticalStrikeRecipe(200, 1646, 1646),
    },

}

RECIPES: Dict[str, List[str]] = {
    "九溪弥烟": ["5%伤害", "4%伤害", "3%伤害", "3%会心", "2%会心"],
    "黄龙吐翠": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "云飞玉皇": ["4%伤害", "3%伤害", "3%会心", "2%伤害"],
    "夕照雷峰": ["4%伤害", "3%伤害", "3%会心", "2%伤害"],
    "鹤归孤山": ["5%伤害", "4%伤害", "3%伤害", "2%会心"],
    "风来吴山": ["4%伤害", "3%伤害", "3%会心", "2%伤害", "2%会心"],
    "听雷": ["5%伤害", "4%伤害", "3%伤害", "3%会心", "2%会心"]
}
