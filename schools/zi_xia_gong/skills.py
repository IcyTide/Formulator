from typing import Dict

from base.skill import Skill, Damage, DotDamage

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        18121: dict(damage_addition=205),
        32813: {}, 303: {}, 896: {}, 18670: {}, 22014: {}, 36439: {}, 25770: {},
        **{skill_id: {} for skill_id in range(327, 331 + 1)},
        **{skill_id: {} for skill_id in range(461, 465 + 1)},
        **{skill_id: {} for skill_id in range(3439, 3448 + 1)},
        **{skill_id: {} for skill_id in range(6091, 6100 + 1)},
        **{skill_id: {} for skill_id in range(18649, 18653 + 1)},
    },
    DotDamage: {6424: {}},
    Skill: {33592: dict(bind_dot=6424)}
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
