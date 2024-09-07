from typing import Dict

from base.skill import Skill, PureSkill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        22151: {}
    },
    PureSkill: {
        37562: dict(damage_base=145300),
        37561: dict(damage_base=96900)
    }
}
