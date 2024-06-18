from typing import Dict

from assets.setter import set_skill
from base.skill import Skill

GENERAL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        **{skill_id: {} for skill_id in range(29532, 29537 + 1)},
        29548: {}
    }
}

SKILLS = {}
for skill_class, skills in GENERAL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        skill.activate = False
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        set_skill(skill)
        SKILLS[skill_id] = skill
