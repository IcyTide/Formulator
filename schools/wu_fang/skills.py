from typing import Dict

from assets.setter import set_skill
from base.skill import Skill, Dot
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        27451: dict(damage_addition=205),
        32841: {}, 28081: {}, 27552: {}, 27555: {}, 27557: {}, 27579: {}, 27584: {}, 28409: {}, 28346: {}, 34699: {},
        27539: {}, 32922: {}, 27657: {}, 29674: {}, 28385: {}, 28434: {}, 36508: {}, 35367: {}, 29698: {}, 29695: {},
        **{
            skill_id: dict(consume_dot=20052, consume_tick=2) for skill_id in (29505, 29506, 34700, 34702, 30735)
        },
        27560: dict(bind_dot=20052)
    },
    Dot: {20052: {}}
}
SKILLS = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        set_skill(skill)
        SKILLS[skill_id] = skill
