from typing import Dict

from base.skill import Skill, Damage, DotDamage

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        22126: dict(damage_addition=205),
        32822: {}, 22787: {}, 22170: {}, 22550: {}, 22551: {}, 22298: {}, 22621: {}, 22620: {}, 22610: {},
        22611: {}, 22612: {}, 22604: {}, 22605: {}, 22490: {}, 22554: {}, 25314: {}, 36267: {}, 36268: {}, 36265: {},
        36266: {}, 36269: {}, 36270: {}, 34981: {}, 29751: {}, 22761: {}, 25784: {}
    },
    DotDamage: {
        15568: {}, 19626: {}
    },
    Skill: {
        22330: dict(bind_dot=15568),
        26980: dict(bind_dot=19626)
    }
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
