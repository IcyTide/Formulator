from typing import Dict

from base.skill import Skill, PureSkill

SKILLS: Dict[type, Dict[int, dict]] = {
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
