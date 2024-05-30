from typing import Tuple, List, Dict, Union


def agility(value):
    return {"agility_base": value}


def strength(value):
    return {"strength_base": value}


def spirit(value):
    return {"spirit_base": value}


def spunk(value):
    return {"spunk_base": value}


def physical_attack_power(value):
    return {"physical_attack_power_base": value}


def magical_attack_power(value):
    return {"magical_attack_power_base": value}


def weapon_damage(value):
    return {"weapon_damage_base": value}


def surplus(value):
    return {"surplus_base": value}


def strain(value):
    return {"strain_base": value}


def strain_rate(value):
    return {"strain_rate": value}


def haste(value):
    return {"haste_base": value}


def overcome(value):
    return {"physical_overcome_base": value, "magical_overcome_base": value}


def critical_strike(value):
    return {"all_critical_strike_base": value}


def critical_strike_rate(value):
    return {"all_critical_strike_gain": value}


def physical_spread(values):
    return {"physical_attack_power_base": values[0],
            "all_critical_strike_base": values[1],
            "surplus_base": values[1]}


def magical_spread(values):
    return {"magical_attack_power_base": values[0],
            "all_critical_strike_base": values[1],
            "surplus_base": values[1]}


def guild_spread(value):
    return {"surplus_base": value, "strain_base": value}


def boiled_fish(value):
    return {"surplus_base": value, "strain_base": value}


class CONSUMABLES_NUMBER:
    major_food_max: int = 382
    major_food_min: int = 191

    physical_food_max: int = 768
    physical_food_min: int = 384
    magical_food_max: int = 917
    magical_food_min: int = 458

    minor_food_max: int = 1705
    minor_food_min: int = 853

    major_potion_max: int = 492
    major_potion_min: int = 246

    physical_potion_max: int = 988
    physical_potion_min: int = 494
    magical_potion_max: int = 1179
    magical_potion_min: int = 589

    minor_potion_max: int = 2192
    minor_potion_min: int = 1096

    physical_enchant_max: int = 658
    physical_enchant_min: int = 439
    magical_enchant_max: int = 786
    magical_enchant_min: int = 524

    minor_snack_max: int = 1934
    minor_snack_min: int = 1074
    physical_snack_max: int = 866
    physical_snack_min: int = 480
    magical_snack_max: int = 1038
    magical_snack_min: int = 576

    major_wine: int = 256
    haste_wine: int = 1144

    guild_spread: int = 258
    guild_food: int = 517

    major_spread: int = 437
    physical_spread: Tuple[int, int] = (439, 975)
    magical_spread: Tuple[int, int] = (524, 975)

    physical_zongzi: int = 907
    magical_zongzi: int = 1082
    weapon_zongzi: int = 1360
    critical_zongzi: int = 600
    strain_zongzi: int = 61

    physical_candy: int = 972
    magical_candy: int = 1160

    boiled_fish_max: int = 400
    boiled_fish_min: int = 100


FUNCTION_MAP = {
    "身法": agility,
    "力道": strength,
    "根骨": spirit,
    "元气": spunk,
    "外攻": physical_attack_power,
    "内攻": magical_attack_power,
    "武器伤害": weapon_damage,
    "破招": surplus,
    "无双": strain,
    "无双百分比": strain_rate,
    "加速": haste,
    "破防": overcome,
    "会心": critical_strike,
    "会心百分比": critical_strike_rate,
    ("外攻", "会心/破招"): physical_spread,
    ("内攻", "会心/破招"): magical_spread,
    "破招/无双": boiled_fish
}
NAME_MAP = {
    "身法": "身法",
    "力道": "力道",
    "根骨": "根骨",
    "元气": "元气",
    "外攻": "外功",
    "内攻": "内功",
    "武器伤害": "",
    "破招": "",
    "无双": "",
    "无双百分比": "",
    "加速": "",
    "破防": "",
    "会心": "",
    "会心百分比": "",
    ("外攻", "会心/破招"): "外功",
    ("内攻", "会心/破招"): "内功",
    "破招/无双": ""
}
FOODS: Dict[str, Union[dict, list]] = {
    "身法": {
        CONSUMABLES_NUMBER.major_food_max: "杂锦鱼球粥",
        CONSUMABLES_NUMBER.major_food_min: "杂碎汤"
    },
    "力道": {
        CONSUMABLES_NUMBER.major_food_max: "三鲜粥",
        CONSUMABLES_NUMBER.major_food_min: "三鲜汤"
    },
    "根骨": {
        CONSUMABLES_NUMBER.major_food_max: "咸骨粥",
        CONSUMABLES_NUMBER.major_food_min: "老火骨汤"
    },
    "元气": {
        CONSUMABLES_NUMBER.major_food_max: "鱼片砂锅粥",
        CONSUMABLES_NUMBER.major_food_min: "鱼头豆腐汤"
    },
    "外攻": {
        CONSUMABLES_NUMBER.physical_food_max: "太后饼",
        CONSUMABLES_NUMBER.physical_food_min: "煎饼果子"
    },
    "内攻": {
        CONSUMABLES_NUMBER.magical_food_max: "灌汤包",
        CONSUMABLES_NUMBER.magical_food_min: "鲜肉包子"
    },
    "破招": {
        CONSUMABLES_NUMBER.minor_food_max: "白肉血肠",
        CONSUMABLES_NUMBER.minor_food_min: "毛血旺"
    },
    "加速": {
        CONSUMABLES_NUMBER.minor_food_max: "红烧扣肉",
        CONSUMABLES_NUMBER.minor_food_min: "栗子烧肉"
    },
    "破防": {
        CONSUMABLES_NUMBER.minor_food_max: "红烧排骨",
        CONSUMABLES_NUMBER.minor_food_min: "水煮肉片"
    },
    "会心": {
        CONSUMABLES_NUMBER.minor_food_max: "酸菜鱼",
        CONSUMABLES_NUMBER.minor_food_min: "鱼香肉丝"
    }
}
POTIONS: Dict[str, Union[dict, list]] = {
    "身法": {
        CONSUMABLES_NUMBER.major_potion_max: "上品轻身丹",
        CONSUMABLES_NUMBER.major_potion_min: "中品轻身丹"
    },
    "力道": {
        CONSUMABLES_NUMBER.major_potion_max: "上品大力丸",
        CONSUMABLES_NUMBER.major_potion_min: "中品大力丸"
    },
    "根骨": {
        CONSUMABLES_NUMBER.major_potion_max: "上品静心丸",
        CONSUMABLES_NUMBER.major_potion_min: "中品静心丸"
    },
    "元气": {
        CONSUMABLES_NUMBER.major_potion_max: "上品聚魂丹",
        CONSUMABLES_NUMBER.major_potion_min: "中品聚魂丹"
    },
    "外攻": {
        CONSUMABLES_NUMBER.physical_potion_max: "上品亢龙散",
        CONSUMABLES_NUMBER.physical_potion_min: "中品亢龙散"
    },
    "内攻": {
        CONSUMABLES_NUMBER.magical_potion_max: "上品展凤散",
        CONSUMABLES_NUMBER.magical_potion_min: "中品展凤散"
    },
    "破招": {
        CONSUMABLES_NUMBER.minor_potion_max: "上品凝神散",
        CONSUMABLES_NUMBER.minor_potion_min: "中品凝神散"
    },
    "加速": {
        CONSUMABLES_NUMBER.minor_potion_max: "上品活气散",
        CONSUMABLES_NUMBER.minor_potion_min: "中品活气散"
    },
    "破防": {
        CONSUMABLES_NUMBER.minor_potion_max: "上品破秽散",
        CONSUMABLES_NUMBER.minor_potion_min: "中品破秽散"
    },
    "会心": {
        CONSUMABLES_NUMBER.minor_potion_max: "上品玉璃散",
        CONSUMABLES_NUMBER.minor_potion_min: "中品玉璃散"
    }
}
WEAPON_ENCHANTS: Dict[str, Union[dict, list]] = {
    "外攻": {
        CONSUMABLES_NUMBER.physical_enchant_max: "瀑沙熔锭",
        CONSUMABLES_NUMBER.physical_enchant_min: "瀑沙磨石"
    },
    "内攻": {
        CONSUMABLES_NUMBER.magical_enchant_max: "坠宵熔锭",
        CONSUMABLES_NUMBER.magical_enchant_min: "坠宵磨石"
    }
}
SNACKS: Dict[str, Union[dict, list]] = {
    "外攻": {
        CONSUMABLES_NUMBER.physical_snack_max: "创意料理",
        CONSUMABLES_NUMBER.physical_snack_min: "葫芦叫花鸡"
    },
    "内攻": {
        CONSUMABLES_NUMBER.magical_snack_max: "创意料理",
        CONSUMABLES_NUMBER.magical_snack_min: "小炒青菜"
    },
    "无双": {
        CONSUMABLES_NUMBER.minor_snack_max: "创意料理",
        CONSUMABLES_NUMBER.minor_snack_min: "炖豆腐"
    },
    "破招": {CONSUMABLES_NUMBER.minor_snack_min: "煎豆腐"},
    "破防": {
        CONSUMABLES_NUMBER.minor_snack_max: "创意料理",
        CONSUMABLES_NUMBER.minor_snack_min: "炸鱼干"
    },
    "会心": {
        CONSUMABLES_NUMBER.minor_snack_max: "创意料理",
        CONSUMABLES_NUMBER.minor_snack_min: "清蒸鲈鱼"
    }
}
WINES: Dict[str, Union[dict, list]] = {
    "身法": {CONSUMABLES_NUMBER.major_wine: "关外白酒·旬又三"},
    "力道": {CONSUMABLES_NUMBER.major_wine: "汾酒·旬又三"},
    "根骨": {CONSUMABLES_NUMBER.major_wine: "高粱酒·旬又三"},
    "元气": {CONSUMABLES_NUMBER.major_wine: "状元红·旬又三"},
    "加速": {CONSUMABLES_NUMBER.haste_wine: "女儿红·旬又三"}
}
SPREADS: Dict[str, Union[dict, list]] = {
    "身法": {CONSUMABLES_NUMBER.major_spread: "水晶芙蓉宴"},
    "力道": {CONSUMABLES_NUMBER.major_spread: "水晶芙蓉宴"},
    "根骨": {CONSUMABLES_NUMBER.major_spread: "水晶芙蓉宴"},
    "元气": {CONSUMABLES_NUMBER.major_spread: "水晶芙蓉宴"},
    ("外攻", "会心/破招"): {CONSUMABLES_NUMBER.physical_spread: "玉笛谁家听落梅"},
    ("内攻", "会心/破招"): {CONSUMABLES_NUMBER.magical_spread: "二十四桥明月夜"},
}

GUILD_FOOD = f"{CONSUMABLES_NUMBER.guild_food}无双"
GUILD_SPREAD = f"{CONSUMABLES_NUMBER.guild_spread}破招/无双"

BOILED_FISH: Dict[str, Union[dict, list]] = {
    "破招/无双": {
        CONSUMABLES_NUMBER.boiled_fish_max: "百炼水煮鱼",
        CONSUMABLES_NUMBER.boiled_fish_min: "炼狱水煮鱼"
    }
}

CANDY = {
    "外攻": {CONSUMABLES_NUMBER.physical_candy: "云片糕"},
    "内攻": {CONSUMABLES_NUMBER.magical_candy: "芝麻杆"},
}
ZONGZI = {
    "外攻": {CONSUMABLES_NUMBER.physical_zongzi: "芦兜粽"},
    "内攻": {CONSUMABLES_NUMBER.magical_zongzi: "蛋黄粽"},
    "武器伤害": {CONSUMABLES_NUMBER.weapon_zongzi: "瑰栗粽"},
    "无双百分比": {CONSUMABLES_NUMBER.strain_zongzi: "瓜仁粽"},
    "会心百分比": {CONSUMABLES_NUMBER.critical_zongzi: "瘦肉粽"}
}
CONSUMABLES = {}
for consumables in [FOODS, POTIONS, WEAPON_ENCHANTS, SNACKS, WINES, SPREADS, CANDY, ZONGZI, BOILED_FISH]:
    for attr, params in consumables.copy().items():
        consumables.pop(attr)
        if NAME_MAP[attr] not in consumables:
            consumables[NAME_MAP[attr]] = []
        for param, name in params.items():
            if isinstance(attr, tuple) and isinstance(param, tuple):
                name = f"{name}({''.join(f'{p}{a}' for p, a in zip(param, attr))})"
            else:
                name = f"{name}({param}{attr})"
            consumables[NAME_MAP[attr]].append(name)
            CONSUMABLES[name] = FUNCTION_MAP[attr](param)

CONSUMABLES["guild_food"] = strain(CONSUMABLES_NUMBER.guild_food)
CONSUMABLES["guild_spread"] = guild_spread(CONSUMABLES_NUMBER.guild_spread)
