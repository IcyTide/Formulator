from typing import Dict

from assets.setter import set_skill, set_dot
from base.dot import Dot
from base.skill import Skill
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        15: dict(damage_addition=205),
        2716: {}, 6234: {}, 6554: {}, 23936: {}, 24999: {}, 25769: {}, 30524: {}, 30532: {}, 32889: {}, 6559: {},
        32957: {}, 33140: {}, 34611: {}, 34612: {}, 34642: {}, 34704: {}, 35058: {}, 37317: {}, 37318: {}, 37319: {},
        37320: {}, 506: {}, 36554: {},
        **{skill_id: dict(bind_dot=2920) for skill_id in (6207, 18716)},
        25757: dict(bind_dot=18512),
        3889: dict(consume_dot=2920)
    }
}
SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {2920: {}}
}
SKILLS = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        set_skill(skill)
        SKILLS[skill_id] = skill
DOTS = {}
for dot_class, dots in SCHOOL_DOTS.items():
    for dot_id, attrs in dots.items():
        dot = dot_class(dot_id)
        for attr, value in attrs.items():
            setattr(dot, attr, value)
        set_dot(dot)
        DOTS[dot_id] = dot
