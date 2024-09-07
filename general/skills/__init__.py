from typing import Dict

from base.skill import Skill
from general.skills import equipment, formation, team

SKILLS = [
    equipment.SKILLS,
    formation.SKILLS,
    team.SKILLS
]
GENERAL_SKILLS: Dict[int, Skill] = {}
for skills in SKILLS:
    for skill_class, items in skills.items():
        for skill_id, attrs in items.items():
            GENERAL_SKILLS[skill_id] = skill = skill_class(skill_id)
            skill.activate = False
            skill.set_asset(attrs)
