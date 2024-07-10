from typing import Dict

from assets.setter import set_skill, set_dot
from base.skill import Skill, Dot
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        32908: {}, 13520: {}, 34916: {}, 6337: {}, 26703: {}, 32898: {}, 14927: {}, 14928: {}, 36570: {}, 28819: {},
        25779: {}, 34998: {}, 28952: {},
        **{skill_id: {} for skill_id in range(6355, 6374 + 1)},
        **{skill_id: {} for skill_id in range(13523, 13530 + 1)},
        **{skill_id: dict(bind_dot=6367) for skill_id in (6853, 14930)},
        **{skill_id: dict(bind_dot=6401) for skill_id in (6867, 14931)}
    }
}
SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {
        6367: {}, 6401: {}
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
