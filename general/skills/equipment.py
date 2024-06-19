from typing import Dict

from assets.setter import set_skill
from base.skill import Skill, PureSkill

GENERAL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        **{skill_id: {} for skill_id in range(22160, 22164 + 1)},
        **{skill_id: {} for skill_id in range(33257, 33261 + 1)},
        22151: {}
    },
    PureSkill: {
        37562: dict(damage_base=145300),
        37561: dict(damage_base=96900)
    }
}

SKILLS: Dict[int, Skill] = {}
for skill_class, skills in GENERAL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        skill.activate = False
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        set_skill(skill)
        SKILLS[skill_id] = skill
