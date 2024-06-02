from typing import Dict

from base.skill import Damage, DotDamage, DotSkill

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        3095: {}, 3121: {}, 3187: {}, 3222: {}, 3227: {}, 6920: {}, 22789: {}, 25775: {}, 32884: {}, 33870: {},
        37504: {}, 37616: {}
    },
    DotDamage: {
        2237: {"bind_skill": 3125},
        19625: {"bind_skill": 3478}
    },
    DotSkill: {
        3125: {"bind_skill": 2237},
        3478: {"bind_skill": 19625}
    }
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
