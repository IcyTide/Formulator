from typing import Dict

from assets.setter import set_skill, set_dot
from base.skill import Skill, Dot
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        25512: dict(damage_addition=205),
        24454: {}, 24558: {}, 24870: {}, 25174: {}, 25837: {}, 30847: {}, 32886: {}, 33236: {}, 34683: {}, 37311: {},
        37599: {},
        **{skill_id: {} for skill_id in range(24675, 24677 + 1)},
        **{skill_id: {} for skill_id in range(24811, 24814 + 1)},
        **{skill_id: {} for skill_id in range(24821, 24824 + 1)},
        33588: dict(bind_dot=24846)
    }
}
SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {24846: {}}
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
