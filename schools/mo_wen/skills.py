from typing import Dict

from base.skill import Damage, DotDamage, NpcDamage, DotSkill


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        14063: {}, 14100: {}, 14227: {}, 14311: {}, 14312: {}, 14494: {}, 18859: {}, 18860: {}, 25781: {},
        30799: {}, 31008: {}, 31138: {}, 32624: {}, 32738: {},
        34676: {"global_damage_factor": 1048576 * (0.25 * 0.5 * 1.3 * 1.2 * 0.5 * 1.11 * 0.9 - 1)}
    },
    DotDamage: {
        9357: {},
        9361: {},
        23187: {"bind_skill": 31005}
    },
    NpcDamage: {15076: {}},
    DotSkill: {
        **{skill_id: {"bind_skill": 9357} for skill_id in (14287, 17788)},
        **{skill_id: {"bind_skill": 9361} for skill_id in (14291, 17792)},
        31005: {"bind_skill": 23187}
    }
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
