from typing import Dict

from base.skill import Skill, Damage, DotDamage, NpcDamage

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        35866: {}, 35894: {}, 35987: {}, 36157: {}, 36177: {}, 36453: {}, 36579: {}, 36580: {}},
    DotDamage: {26856: {}},
    NpcDamage: {
        36056: {}, 36057: {}, 36111: {}, 36112: {}, 36113: {}, 36114: {},
    },
    Skill: {
        35771: dict(bind_dot=26856),
        36165: dict(consume_dot=26856, consume_tick=3)
    }
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
