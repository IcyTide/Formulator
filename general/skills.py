from typing import Dict

from base.skill import PhysicalDamage, Skill

GENERAL_SKILLS: Dict[int, Skill | dict] = {
    22160: {
        "skill_class": PhysicalDamage,
        "skill_name": "昆吾·弦刃",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": 75
    },
    33257: {
        "skill_class": PhysicalDamage,
        "skill_name": "刃凌",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": [60, 100, 60, 100, 100]
    },
}

for skill_id, detail in GENERAL_SKILLS.items():
    GENERAL_SKILLS[skill_id] = detail.pop('skill_class')(skill_id, detail.pop('skill_name'))
    for attr, value in detail.items():
        setattr(GENERAL_SKILLS[skill_id], attr, value)
