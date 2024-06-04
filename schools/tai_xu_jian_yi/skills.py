from typing import Dict

from base.skill import Skill, Damage, DotDamage

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        18121: dict(damage_addition=205),
        589: {}, 4954: {}, 13853: {}, 21726: {}, 21979: {}, 25771: {}, 32814: {}, 34693: {}, 34694: {},
        **{skill_id: {} for skill_id in range(386, 394 + 1)},
        32408: dict(consume_dot=748, consume_tick=1)
    },
    DotDamage: {
        748: {}, 889: {}, 23170: {}
    },
    Skill: {
        600: dict(bind_dot=748),
        30944: dict(bind_dot=889),
        37453: dict(bind_dot=23170)
    },
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
