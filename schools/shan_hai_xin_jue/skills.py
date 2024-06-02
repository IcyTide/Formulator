from typing import Dict

from base.skill import Damage, DotDamage, NpcDamage, DotSkill, DotConsumeSkill

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        35866: {}, 35894: {}, 35987: {}, 36157: {}, 36177: {}, 36453: {}, 36579: {}, 36580: {}},
    DotDamage: {
        26856: {"bind_skill": 35771}
    },
    NpcDamage: {
        36056: {}, 36057: {}, 36111: {}, 36112: {}, 36113: {}, 36114: {},
    },
    DotSkill: {
        35771: {"bind_skill": 26856}
    },
    DotConsumeSkill: {
        36165: {"bind_skill": 26856, "tick": 3}
    }
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
