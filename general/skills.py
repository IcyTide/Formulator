from typing import Dict

from base.skill import PhysicalDamage, MagicalDamage, Skill, PureSkill

GENERAL_SKILLS: Dict[int, Skill | dict] = {
    29535: {
        "skill_class": MagicalDamage,
        "skill_name": "逐云寒蕊",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": [90, 200 * 1.2],
        "skill_shield_gain": -1024
    },
    29536: {
        "skill_class": PhysicalDamage,
        "skill_name": "逐云寒蕊",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": [90, 200 * 1.2],
        "skill_shield_gain": -1024
    },
    22160: {
        "skill_class": PhysicalDamage,
        "skill_name": "昆吾·弦刃",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": 75
    },
    22164: {
        "skill_class": MagicalDamage,
        "skill_name": "昆吾·弦刃",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": 90
    },
    33257: {
        "skill_class": PhysicalDamage,
        "skill_name": "刃凌",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": [60, 100, 60, 100, 100]
    },
    33261: {
        "skill_class": MagicalDamage,
        "skill_name": "刃凌",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": [50, 100]
    },
    37562: {
        "skill_class": PureSkill,
        "skill_name": "昆吾·弦刃",
        "damage_base": 145300
    },
    37561: {
        "skill_class": PureSkill,
        "skill_name": "刃凌",
        "damage_base": 96900,
    },
}

for skill_id, detail in GENERAL_SKILLS.items():
    GENERAL_SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    GENERAL_SKILLS[skill_id].activate = False
    for attr, value in detail.items():
        setattr(GENERAL_SKILLS[skill_id], attr, value)
