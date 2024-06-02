from typing import Dict

from base.skill import Damage, DotDamage, DotSkill, DotConsumeSkill


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        32841: {}, 27451: {}, 28081: {}, 27552: {}, 27555: {}, 27557: {}, 27579: {}, 27584: {}, 28409: {}, 28346: {},
        34699: {}, 27539: {}, 32922: {}, 27657: {}, 29674: {}, 28385: {}, 28434: {}, 36508: {}, 35367: {}, 29698: {},
        29695: {}
    },
    type("", (Damage, DotConsumeSkill), {}): {
        skill_id: {"bind_skill": 20052, "tick": 2} for skill_id in (29505, 29506, 34700, 34702, 30735)
    },
    DotDamage: {20052: {'bind_skill': 27560}},
    DotSkill: {27560: {'bind_skill': 20052}}
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
