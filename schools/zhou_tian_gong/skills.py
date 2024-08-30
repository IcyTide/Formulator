from typing import Dict

from base.skill import Skill
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        37804: {}, 37816: {}, 38016: {}, 38075: {}, 38076: {}, 38077: {}, 38084: {}, 38085: {}, 38090: {}, 38093: {},
        38438: {}, 38447: {}, 38452: {}, 38453: {}, 38083: {}, 38531: {}, 38554: {}, 38556: {}, 38557: {},
    }
}
SKILLS: Dict[int, Skill] = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        SKILLS[skill_id] = skill = skill_class(skill_id)
        skill.set_asset(attrs)
