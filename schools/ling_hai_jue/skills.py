from typing import Dict

from base.skill import Damage, DotDamage, DotSkill

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        19712: {}, 19766: {}, 19767: {}, 19768: {}, 19819: {}, 20016: {}, 20052: {}, 20054: {}, 20322: {}, 20323: {},
        20684: {}, 20685: {}, 20734: {}, 25273: {}, 25783: {}, 31250: {}, 32478: {}, 32815: {}, 36282: {}
    },
    DotDamage: {
        18386: {"bind_skill": 25640},
        19557: {"bind_skill": 26935}
    },
    DotSkill: {
        25640: {"bind_skill": 18386},
        26935: {"bind_skill": 19557}
    }
}
SKILLS = {}

for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
