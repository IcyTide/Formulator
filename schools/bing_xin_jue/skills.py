from typing import Dict

from base.skill import Damage, DotDamage, DotSkill, DotConsumeSkill

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        15: {}, 2716: {}, 6234: {}, 6554: {}, 6559: {}, 23936: {}, 24999: {}, 25769: {}, 30524: {}, 30532: {},
        32889: {}, 32957: {}, 33140: {}, 34611: {}, 34612: {}, 34642: {}, 34704: {}, 35058: {}, 37317: {}, 37318: {},
        37319: {}, 37320: {}
    },
    type("", (Damage, DotConsumeSkill), {}): {
        6559: {
            "bind_skill": 2920,
            "tick": 99,
            "last_dot": False
        }
    },
    DotDamage: {
        2920: {"bind_skill": 6207},
        18512: {"bind_skill": 25757}
    },
    DotSkill: {
        **{skill_id: {"bind_skill": 2920} for skill_id in (6207, 18716)},
        25757: {"bind_skill": 18512}
    }
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
