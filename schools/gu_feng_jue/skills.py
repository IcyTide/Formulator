from typing import Dict

from assets.setter import set_skill
from base.skill import Skill, Dot
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        33146: {}, 32974: {}, 32975: {}, 32510: {}, 32246: {}, 32766: {}, 32149: {}, 32150: {}, 32151: {}, 32154: {},
        32167: {}, 32348: {}, 32602: {}, 32603: {}, 32604: {}, 32891: {}, 32892: {}, 32357: {}, 36118: {}, 33239: {},
        34695: {}, 32591: {},
        **{skill_id: {} for skill_id in range(32234, 32239 + 1)},
        36851: dict(bind_dot=27820),
        33133: dict(bind_dot=24650),
        **{skill_id: dict(bind_dot=24132, bind_stack=i + 1) for i, skill_id in enumerate(range(32372, 32369 - 1, -1))},
        **{skill_id: dict(bind_dot=24443, bind_stack=i + 1) for i, skill_id in enumerate(range(32874, 32869 - 1, -1))}
    },
    Dot: {
        24132: {}, 24443: {}, 24650: {}, 27820: {}
    },
}
SKILLS = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        set_skill(skill)
        SKILLS[skill_id] = skill
