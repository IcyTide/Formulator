from typing import Dict

from base.skill import Damage, DotDamage, DotSkill

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        32908: {}, 13520: {}, 13523: {}, 13526: {}, 13527: {}, 6362: {}, 6363: {}, 13528: {}, 13529: {}, 34916: {},
        6355: {}, 6356: {}, 6357: {}, 6358: {}, 6359: {}, 6337: {}, 26703: {}, 32898: {}, 14927: {}, 14928: {},
        36570: {}, 28819: {}, 25779: {},
        **{skill_id: {} for skill_id in range(6366, 6374 + 1)},
    },
    DotDamage: {6401: {'bind_skill': 6867}},
    DotSkill: {skill_id: {'bind_skill': 6401} for skill_id in (6867, 14931)}
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
