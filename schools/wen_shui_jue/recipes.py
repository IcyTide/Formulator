from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "九溪弥烟": {
        "5%伤害": damage_addition_recipe([26673, 18685], 51),
        "4%伤害": damage_addition_recipe([26673, 18685], 41),
        "3%伤害": damage_addition_recipe([26673, 18685], 31),
        "3%会心": critical_strike_recipe([26673, 18685], 300),
        "2%会心": critical_strike_recipe([26673, 18685], 200),
    },
    "黄龙吐翠": {
        "5%伤害": damage_addition_recipe([13471], 51),
        "4%伤害": damage_addition_recipe([13471], 41),
        "3%伤害": damage_addition_recipe([13471], 31),
        "4%会心": critical_strike_recipe([13471], 400),
        "3%会心": critical_strike_recipe([13471], 300),
        "2%会心": critical_strike_recipe([13471], 200),
    },
    "云飞玉皇": {
        "4%伤害": damage_addition_recipe([1594, 1595, 18317], 41),
        "3%伤害": damage_addition_recipe([1594, 1595, 18317], 31),
        "2%伤害": damage_addition_recipe([1594, 1595, 18317], 21),
        "3%会心": critical_strike_recipe([1594, 1595, 18317], 300),
    },
    "夕照雷峰": {
        "4%伤害": damage_addition_recipe([2896], 41),
        "3%伤害": damage_addition_recipe([2896], 31),
        "2%伤害": damage_addition_recipe([2896], 21),
        "3%会心": critical_strike_recipe([2896], 300),
    },
    "鹤归孤山": {
        "5%伤害": damage_addition_recipe([1598], 51),
        "4%伤害": damage_addition_recipe([1598], 41),
        "3%伤害": damage_addition_recipe([1598], 31),
        "2%会心": critical_strike_recipe([1598], 200),
    },
    "风来吴山": {
        "4%伤害": damage_addition_recipe([18991], 41),
        "3%伤害": damage_addition_recipe([18991], 31),
        "2%伤害": damage_addition_recipe([18991], 21),
        "3%会心": critical_strike_recipe([18991], 300),
        "2%会心": critical_strike_recipe([18991], 200),
    },
    "听雷": {
        "5%伤害": damage_addition_recipe([1706, 1707], 51),
        "4%伤害": damage_addition_recipe([1706, 1707], 41),
        "3%伤害": damage_addition_recipe([1706, 1707], 31),
        "3%会心": critical_strike_recipe([1706, 1707], 300),
        "2%会心": critical_strike_recipe([1706, 1707], 200),
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
