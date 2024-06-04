from typing import Dict

from base.skill import Skill, Damage, DotDamage

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        32823: {}, 16419: {}, 16820: {}, 16822: {}, 16599: {}, 16631: {}, 16787: {}, 16794: {}, 16610: {}, 16760: {},
        16382: {}, 20991: {}, 19424: {}, 36486: {}, 30645: {}, 34585: {}, 32859: {}, 37458: {}, 25782: {},
        **{skill_id: {} for skill_id in range(16933, 16944 + 1)},
        **{skill_id: {} for skill_id in (16803, 16802, 16801, 16800, 17043, 19423)},
    },
    DotDamage: {11447: {}, 19555: {}},
    Skill: {
        **{skill_id: dict(bind_dot=11447) for skill_id in (17058, 17060)},
        26934: dict(bind_dot=19555)
    }
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
