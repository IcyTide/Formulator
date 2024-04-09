from typing import Dict, List, Tuple

from base.buff import Buff
from base.recipe import damage_addition_recipe, critical_strike_recipe

RECIPES: Dict[str, List[Tuple[str, dict]]] = {
    "雷走风切": [
        ("5%伤害", damage_addition_recipe([16631, 16599], 51)),
        ("4%伤害", damage_addition_recipe([16631, 16599], 41)),
        ("4%会心", critical_strike_recipe([16631, 16599], 400)),
        ("3%伤害", damage_addition_recipe([16631, 16599], 31)),
        ("3%会心", critical_strike_recipe([16631, 16599], 300)),
        ("2%会心", critical_strike_recipe([16631, 16599], 200)),
    ]
    ,

    "项王击鼎": [
        ("5%伤害", damage_addition_recipe([16760, 16382], 51)),
        ("4%伤害", damage_addition_recipe([16760, 16382], 41)),
        ("4%会心", critical_strike_recipe([16760, 16382], 400)),
        ("3%伤害", damage_addition_recipe([16760, 16382], 31)),
        ("3%会心", critical_strike_recipe([16760, 16382], 300)),
        ("2%会心", critical_strike_recipe([16760, 16382], 200)),
    ]
    ,

    "破釜沉舟": [
        ("5%伤害", damage_addition_recipe([20991], 51)),
        ("4%伤害", damage_addition_recipe([20991], 41)),
        ("4%会心", critical_strike_recipe([20991], 400)),
        ("3%伤害", damage_addition_recipe([20991], 31)),
        ("3%会心", critical_strike_recipe([20991], 300)),
        ("2%会心", critical_strike_recipe([20991], 200)),
    ]
    ,

    "上将军印": [
        ("4%伤害", damage_addition_recipe([16803, 16802, 16801, 16800, 17043, 19423, 19424, 32859], 41)),
        ("4%会心", critical_strike_recipe([16803, 16802, 16801, 16800, 17043, 19423, 19424], 400)),
        ("3%伤害", damage_addition_recipe([16803, 16802, 16801, 16800, 17043, 19423, 19424, 32859], 31)),
        ("3%会心", critical_strike_recipe([16803, 16802, 16801, 16800, 17043, 19423, 19424], 300)),
        ("2%伤害", damage_addition_recipe([16803, 16802, 16801, 16800, 17043, 19423, 19424, 32859], 21)),
        ("2%会心", critical_strike_recipe([16803, 16802, 16801, 16800, 17043, 19423, 19424], 200)),
    ]
    ,

    "擒龙六斩": [
        ("5%伤害", damage_addition_recipe([16933, 16934, 16935, 16936, 16937, 16938], 51)),
        ("4%伤害", damage_addition_recipe([16933, 16934, 16935, 16936, 16937, 16938], 41)),
        ("4%会心", critical_strike_recipe([16933, 16934, 16935, 16936, 16937, 16938], 400)),
        ("3%伤害", damage_addition_recipe([16933, 16934, 16935, 16936, 16937, 16938], 31)),
        ("3%会心", critical_strike_recipe([16933, 16934, 16935, 16936, 16937, 16938], 300)),
        ("2%会心", critical_strike_recipe([16933, 16934, 16935, 16936, 16937, 16938], 200)),
    ],
    "刀啸风吟": [
        ("5%伤害", damage_addition_recipe([16610], 51)),
        ("4%伤害", damage_addition_recipe([16610], 41)),
        ("4%会心", critical_strike_recipe([16610], 400)),
        ("3%会心", critical_strike_recipe([16610], 300)),
        ("2%会心", critical_strike_recipe([16610], 200)),
    ]

}

for skill_name, recipes in RECIPES.items():
    for skill_name, detail in recipe.items():
        if not detail:
            continue
        talent[talent_id] = Buff(talent_id, detail.pop("buff_name"))
        for attr, value in detail.items():
            setattr(talent[talent_id], attr, value)
