from typing import Dict

from base.skill import Damage

GENERAL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        **{skill_id: {} for skill_id in range(29532, 29537 + 1)},
    }
}

SKILLS = {}
for skill_class, skills in GENERAL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
