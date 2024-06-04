from typing import Dict

from base.skill import Skill, Damage, DotDamage

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        3121: dict(damage_addition=205),
        3095: {}, 3187: {}, 3222: {}, 3227: {}, 6920: {}, 22789: {}, 25775: {}, 32884: {}, 33870: {}, 37504: {},
        37616: {}
    },
    DotDamage: {
        2237: dict(extra_tick=1),
        19625: {}
    },
    Skill: {
        3125: dict(bind_dot=2237),
        3478: dict(bind_dot=19625)
    }
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
