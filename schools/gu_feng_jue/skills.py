from typing import Dict

from base.skill import Damage, DotDamage, Skill


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        33146: {}, 32974: {}, 32975: {}, 32510: {}, 32246: {}, 32766: {}, 32149: {}, 32150: {}, 32151: {}, 32154: {},
        32167: {}, 32348: {}, 32602: {}, 32603: {}, 32604: {}, 32234: {}, 32235: {}, 32236: {}, 32237: {}, 32238: {},
        32239: {}, 32891: {}, 32892: {}, 32357: {}, 36118: {}, 33239: {}
    },
    DotDamage: {
        24443: {}, 27820: {}
    },
    Skill: {
        36851: dict(bind_dot=27820),
        **{skill_id: dict(bind_dot=24443) for skill_id in range(32869, 32874 + 1)}
    }
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
