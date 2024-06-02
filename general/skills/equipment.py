from typing import Dict

from base.skill import Damage, PureDamage

GENERAL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        **{skill_id: {} for skill_id in range(22160, 22164 + 1)},
        **{skill_id: {} for skill_id in range(33257, 33261 + 1)}
    },
    PureDamage: {
        37561: {"damage_base": 96900},
        37562: {"damage_base": 145300}
    }
}

SKILLS = {}
for skill_class, skills in GENERAL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
