from typing import Dict, Union

from base.skill import PhysicalDamage, MagicalDamage, Skill

GENERAL_SKILLS: Dict[int, Union[Skill, dict]] = {
    13778: {
        "skill_class": Skill,
        "skill_name": "乘龙箭",
        "post_target_buffs": {(3465, 1): 1},
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
