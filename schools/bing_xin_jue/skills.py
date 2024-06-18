from typing import Dict

from assets.setter import set_skill
from base.skill import Skill, Dot
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        15: dict(damage_addition=205),
        2716: {}, 6234: {}, 6554: {}, 23936: {}, 24999: {}, 25769: {}, 30524: {}, 30532: {}, 32889: {}, 6559: {},
        32957: {}, 33140: {}, 34611: {}, 34612: {}, 34642: {}, 34704: {}, 35058: {}, 37317: {}, 37318: {}, 37319: {},
        37320: {},
        **{skill_id: dict(bind_dot=2920) for skill_id in (6207, 18716)},
        25757: dict(bind_dot=18512),
        3889: dict(consume_dot=2920)
    },
    Dot: {
        2920: {}
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
