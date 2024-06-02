from typing import Dict

from base.skill import Damage, DotDamage, DotSkill, DotConsumeSkill

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        589: {}, 4954: {}, 13853: {}, 18121: {}, 21726: {}, 21979: {}, 25771: {}, 32814: {}, 34693: {}, 34694: {},
        **{skill_id: {} for skill_id in range(386, 394 + 1)}
    },
    type("", (Damage, DotConsumeSkill), {}): {
        32408: {
            "bind_skill": 748,
            "tick": 1,
        }
    },
    DotDamage: {
        748: {"bind_skill": 600},
        889: {"bind_skill": 30944},
        23170: {"bind_skill": 37453}
    },
    DotSkill: {
        600: {"bind_skill": 748},
        30944: {"bind_skill": 889},
        37453: {"bind_skill": 23170}
    },
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
