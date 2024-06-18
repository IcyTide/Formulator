from typing import Dict

from assets.setter import set_skill
from base.skill import Skill, Dot
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        32887: {}, 4326: {}, 19055: {}, 13468: {}, 3963: {}, 4035: {}, 4036: {}, 4476: {}, 4480: {}, 4482: {},
        18280: {}, 18281: {}, 26708: {}, 26709: {}, 26916: {}, 35056: {}, 35057: {}, 34985: {}, 34348: {}, 34349: {},
        34362: {}, 34363: {}, 34359: {}, 34361: {}, 37336: {}, 25777: {},
        **{skill_id: {} for skill_id in range(4483, 4490 + 1)},
        13359: dict(bind_dot=4202),
        **{skill_id: dict(bind_dot=25725) for skill_id in (34373, 35038)},
        **{skill_id: dict(bind_dot=25726) for skill_id in (34374, 35039)}
    },
    Dot: {4202: {}, 25725: {}, 25726: {}}
}
SKILLS = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        set_skill(skill)
        SKILLS[skill_id] = skill
