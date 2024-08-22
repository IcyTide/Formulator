from typing import Dict

from base.skill import Skill

GENERAL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        28947: {}
    }
}

SKILLS = {}
for skill_class, skills in GENERAL_SKILLS.items():
    for skill_id, attrs in skills.items():
        SKILLS[skill_id] = skill = skill_class(skill_id)
        skill.activate = False
        skill.set_asset(attrs)
