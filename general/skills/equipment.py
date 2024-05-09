from typing import Dict

from base.skill import PhysicalDamage, MagicalDamage, Skill, PureDamage

GENERAL_SKILLS: Dict[int, Skill | dict] = {
    22160: {
        "skill_class": PhysicalDamage,
        "skill_name": "昆吾·弦刃",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": 75
    },
    22161: {
        "skill_class": MagicalDamage,
        "skill_name": "昆吾·弦刃",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": 90
    },
    22162: {
        "skill_class": MagicalDamage,
        "skill_name": "昆吾·弦刃",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": 90
    },
    22163: {
        "skill_class": MagicalDamage,
        "skill_name": "昆吾·弦刃",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": 90
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
    33258: {
        "skill_class": MagicalDamage,
        "skill_name": "刃凌",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": [50, 100]
    },
    33259: {
        "skill_class": MagicalDamage,
        "skill_name": "刃凌",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": [50, 100]
    },
    33260: {
        "skill_class": MagicalDamage,
        "skill_name": "刃凌",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": [50, 100]
    },
    33261: {
        "skill_class": MagicalDamage,
        "skill_name": "刃凌",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": [50, 100]
    },
    37562: {
        "skill_class": PureDamage,
        "skill_name": "昆吾·弦刃",
        "damage_base": 145300
    },
    37561: {
        "skill_class": PureDamage,
        "skill_name": "刃凌",
        "damage_base": 96900,
    },
}

for skill_id, detail in GENERAL_SKILLS.items():
    GENERAL_SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    GENERAL_SKILLS[skill_id].activate = False
    for attr, value in detail.items():
        setattr(GENERAL_SKILLS[skill_id], attr, value)
