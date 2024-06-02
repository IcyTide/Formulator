from typing import Dict

from base.skill import Damage, DotDamage, DotSkill

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        32813: {}, 18121: {}, 303: {}, 327: {}, 328: {}, 329: {}, 330: {}, 331: {}, 461: {}, 462: {}, 463: {}, 464: {},
        465: {}, 896: {}, 3439: {}, 3440: {}, 3441: {}, 3442: {}, 3443: {}, 3444: {}, 3445: {}, 3446: {}, 3447: {},
        3448: {}, 6091: {}, 6092: {}, 6093: {}, 6094: {}, 6095: {}, 6096: {}, 6097: {}, 6098: {}, 6099: {}, 6100: {},
        18649: {}, 18650: {}, 18651: {}, 18652: {}, 18653: {}, 18670: {}, 22014: {}, 36439: {}, 25770: {}
    },
    DotDamage: {6424: {'bind_skill': 33592}},
    DotSkill: {33592: {'bind_skill': 6424}}
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
