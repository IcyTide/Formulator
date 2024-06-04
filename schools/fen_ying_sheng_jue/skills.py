from typing import Dict

from base.skill import Skill, Damage, DotDamage

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        32887: {}, 4326: {}, 19055: {}, 13468: {}, 3963: {}, 4035: {}, 4036: {}, 4476: {}, 4483: {}, 4484: {},
        4485: {}, 4486: {}, 4487: {}, 4488: {}, 4489: {}, 4490: {}, 4480: {}, 4482: {}, 18280: {}, 18281: {},
        26708: {}, 26709: {}, 26916: {}, 35056: {}, 35057: {}, 34985: {}, 34348: {}, 34349: {}, 34362: {},
        34363: {}, 34359: {}, 34361: {}, 37336: {}, 25777: {}
    },
    DotDamage: {4202: {}, 25725: {}, 25726: {}},
    Skill: {
        13359: dict(bind_dot=4202),
        **{skill_id: dict(bind_dot=25725) for skill_id in (34373, 35038)},
        **{skill_id: dict(bind_dot=25726) for skill_id in (34374, 35039)}
    }
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
