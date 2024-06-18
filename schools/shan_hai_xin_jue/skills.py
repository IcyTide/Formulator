from typing import Dict

from assets.setter import set_skill
from base.skill import Skill, Dot, NpcSkill
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        35866: {}, 35894: {}, 35987: {}, 36157: {}, 36177: {}, 36453: {}, 36579: {}, 36580: {},
        35771: dict(bind_dot=26856),
        36165: dict(consume_dot=26856, consume_tick=3),
        35695: dict(pet_buffs={(26857, 1): 1}),
        35696: dict(pet_count=3, pet_buffs={(26857, 1): 1})
    },
    Dot: {26856: {}},
    NpcSkill: {
        36056: {}, 36057: {}, 36111: {}, 36112: {}, 36113: {}, 36114: {},
    }
}
SKILLS = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        set_skill(skill)
        SKILLS[skill_id] = skill
