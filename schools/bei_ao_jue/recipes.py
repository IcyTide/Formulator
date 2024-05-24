from typing import Dict, List

from base.gain import Gain
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "雷走风切": {
        "5%伤害": damage_addition_recipe([16631, 16599], 51),
        "4%伤害": damage_addition_recipe([16631, 16599], 41),
        "4%会心": critical_strike_recipe([16631, 16599], 400),
        "3%伤害": damage_addition_recipe([16631, 16599], 31),
        "3%会心": critical_strike_recipe([16631, 16599], 300),
        "2%会心": critical_strike_recipe([16631, 16599], 200),
    },
    "项王击鼎": {
        "5%伤害": damage_addition_recipe([16760, 16382], 51),
        "4%伤害": damage_addition_recipe([16760, 16382], 41),
        "4%会心": critical_strike_recipe([16760, 16382], 400),
        "3%伤害": damage_addition_recipe([16760, 16382], 31),
        "3%会心": critical_strike_recipe([16760, 16382], 300),
        "2%会心": critical_strike_recipe([16760, 16382], 200),
    },
    "破釜沉舟": {
        "5%伤害": damage_addition_recipe([20991], 51),
        "4%伤害": damage_addition_recipe([20991], 41),
        "4%会心": critical_strike_recipe([20991], 400),
        "3%伤害": damage_addition_recipe([20991], 31),
        "3%会心": critical_strike_recipe([20991], 300),
        "2%会心": critical_strike_recipe([20991], 200),
    },
    "上将军印": {
        "4%伤害": damage_addition_recipe([16803, 16802, 16801, 16800, 17043, 19423, 19424, 32859], 41),
        "4%会心": critical_strike_recipe([16803, 16802, 16801, 16800, 17043, 19423, 19424], 400),
        "3%伤害": damage_addition_recipe([16803, 16802, 16801, 16800, 17043, 19423, 19424, 32859], 31),
        "3%会心": critical_strike_recipe([16803, 16802, 16801, 16800, 17043, 19423, 19424], 300),
        "2%伤害": damage_addition_recipe([16803, 16802, 16801, 16800, 17043, 19423, 19424, 32859], 21),
        "2%会心": critical_strike_recipe([16803, 16802, 16801, 16800, 17043, 19423, 19424], 200),
    },
    "擒龙六斩": {
        "5%伤害": damage_addition_recipe([16933, 16934, 16935, 16936, 16937, 16938, 16939, 16940, 16941, 16942], 51),
        "4%伤害": damage_addition_recipe([16933, 16934, 16935, 16936, 16937, 16938, 16939, 16940, 16941, 16942], 41),
        "4%会心": critical_strike_recipe([16933, 16934, 16935, 16936, 16937, 16938, 16939, 16940, 16941, 16942], 400),
        "3%伤害": damage_addition_recipe([16933, 16934, 16935, 16936, 16937, 16938, 16939, 16940, 16941, 16942], 31),
        "3%会心": critical_strike_recipe([16933, 16934, 16935, 16936, 16937, 16938, 16939, 16940, 16941, 16942], 300),
        "2%会心": critical_strike_recipe([16933, 16934, 16935, 16936, 16937, 16938, 16939, 16940, 16941, 16942], 200),
    },
    "刀啸风吟": {
        "5%伤害": damage_addition_recipe([16610], 51),
        "4%伤害": damage_addition_recipe([16610], 41),
        "4%会心": critical_strike_recipe([16610], 400),
        "3%会心": critical_strike_recipe([16610], 300),
        "2%会心": critical_strike_recipe([16610], 200),
    }
}

RECIPES: Dict[str, List[str]] = {
    "雷走风切": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "项王击鼎": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "破釜沉舟": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "上将军印": ["4%伤害", "4%会心", "3%伤害", "3%会心", "2%伤害", "2%会心"],
    "擒龙六斩": ["5%伤害", "4%伤害", "4%会心", "3%伤害", "3%会心", "2%会心"],
    "刀啸风吟": ["5%伤害", "4%伤害", "4%会心", "3%会心", "2%会心"]
}
