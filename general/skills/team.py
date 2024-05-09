from typing import Dict

from base.skill import PhysicalDamage, MagicalDamage, Skill, PureDamage, BuffSkill

GENERAL_SKILLS: Dict[int, Skill | dict] = {
    13778: {
        "skill_class": BuffSkill,
        "skill_name": "乘龙箭",
        "bind_buff": 3465,
        "duration": 128
    },
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
    }
}

for skill_id, detail in GENERAL_SKILLS.items():
    GENERAL_SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    GENERAL_SKILLS[skill_id].activate = False
    for attr, value in detail.items():
        setattr(GENERAL_SKILLS[skill_id], attr, value)
