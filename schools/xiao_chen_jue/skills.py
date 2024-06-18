from typing import Dict

from assets.setter import set_skill
from base.skill import Skill, Dot
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        32908: {}, 13520: {}, 13523: {}, 13526: {}, 13527: {}, 6362: {}, 6363: {}, 13528: {}, 13529: {}, 34916: {},
        6355: {}, 6356: {}, 6357: {}, 6358: {}, 6359: {}, 6337: {}, 26703: {}, 32898: {}, 14927: {}, 14928: {},
        36570: {}, 28819: {}, 25779: {},
        **{skill_id: {} for skill_id in range(6366, 6374 + 1)},
        **{skill_id: dict(bind_dot=6401) for skill_id in (6867, 14931)}
    },
    Dot: {6401: {}}
}
SKILLS = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        set_skill(skill)
        SKILLS[skill_id] = skill
