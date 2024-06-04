from typing import Dict

from base.skill import Skill, Damage, DotDamage

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        15: dict(damage_addition=205),
        2716: {}, 6234: {}, 6554: {}, 23936: {}, 24999: {}, 25769: {}, 30524: {}, 30532: {}, 32889: {}, 6559: {},
        32957: {}, 33140: {}, 34611: {}, 34612: {}, 34642: {}, 34704: {}, 35058: {}, 37317: {}, 37318: {}, 37319: {},
        37320: {},
    },
    DotDamage: {
        2920: {}, 18716: {}
    },
    Skill: {
        **{skill_id: dict(bind_dot=2920) for skill_id in (6207, 18716)},
        25757: dict(bind_dot=18512),
        3889: dict(consume_dot=2920)
    }
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
