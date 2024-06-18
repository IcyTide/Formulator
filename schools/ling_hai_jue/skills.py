from typing import Dict

from assets.setter import set_skill
from base.skill import Skill, Dot
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        19712: dict(damage_addition=205),
        19766: {}, 19767: {}, 20014: {}, 19819: {}, 20016: {}, 20052: {}, 20054: {}, 20322: {}, 20323: {}, 20684: {},
        20685: {}, 20734: {}, 25273: {}, 25783: {}, 31250: {}, 32478: {}, 32815: {}, 36282: {},
        25640: dict(bind_dot=18386),
        26935: dict(bind_dot=19557)
    },
    Dot: {18386: {}, 19557: {}}
}
SKILLS = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        set_skill(skill)
        SKILLS[skill_id] = skill
