from typing import Dict

from assets.setter import set_skill, set_dot
from base.skill import Skill, Dot
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        32823: {}, 16419: {}, 16820: {}, 16822: {}, 16599: {}, 16631: {}, 16787: {}, 16794: {}, 16610: {}, 16760: {},
        16382: {}, 20991: {}, 19424: {}, 36486: {}, 30645: {}, 34585: {}, 32859: {}, 37458: {}, 37984: {}, 25782: {},
        **{skill_id: {} for skill_id in range(16933, 16944 + 1)},
        **{skill_id: {} for skill_id in (16803, 16802, 16801, 16800, 17043, 19423)},
        **{skill_id: dict(bind_dot=11447) for skill_id in (17058, 17060)},
        26934: dict(bind_dot=19555)
    }
}
SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {11447: {}, 19555: {}}
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
