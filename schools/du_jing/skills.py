from typing import Dict

from assets.setter import set_skill, set_dot
from base.skill import Skill, PetSkill, Dot
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        2183: dict(damage_addition=205),
        3067: {}, 13472: {}, 18590: {}, 25044: {}, 25773: {}, 29573: {}, 30918: {}, 32818: {}, 34389: {}, 6648: {},
        37959: {},
        13476: dict(bind_dot=6218),
        34643: dict(bind_dot=25917),
        6238: dict(bind_dot=2509),
        6237: dict(bind_dot=2296),
        6236: dict(bind_dot=2295),
        26226: dict(bind_dot=18882),
        2223: dict(pet_buffs={(16543, 1): 1})
    },
    PetSkill: {2472: {}, 22997: {}, 36292: {}, 25019: {}},
}
SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {
        6218: {}, 2509: {}, 2295: {}, 18882: {}, 2296: {},
        25917: dict(tick_extra=1),
    }
}
SKILLS = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        set_skill(skill)
        SKILLS[skill_id] = skill
DOTS = {}
for dot_class, dots in SCHOOL_DOTS.items():
    for dot_id, attrs in dots.items():
        dot = dot_class(dot_id)
        for attr, value in attrs.items():
            setattr(dot, attr, value)
        set_dot(dot)
        DOTS[dot_id] = dot
