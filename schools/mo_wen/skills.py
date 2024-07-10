from typing import Dict

from assets.setter import set_skill, set_dot
from base.constant import GLOBAL_DAMAGE_COF
from base.skill import Skill, Dot, NpcSkill
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        14063: {}, 14100: {}, 14227: {}, 14311: {}, 14312: {}, 14494: {}, 18859: {}, 18860: {}, 25781: {}, 31008: {},
        31138: {}, 32624: {}, 32738: {}, 34514: {}, 38015: {},
        14082: dict(post_buffs={(12576, 1): 1}),
        30799: dict(magical_shield_gain=-922),  # BUFF-23167
        34676: dict(
            global_damage_cof_extra=GLOBAL_DAMAGE_COF(1048576 * (0.25 * 0.5 * 1.3 * 1.2 * 0.5 * 1.11 * 0.9 - 1))
        ),
        **{skill_id: dict(bind_dot=9357) for skill_id in (14287, 17788)},
        **{skill_id: dict(bind_dot=9361) for skill_id in (14291, 17792)},
        31005: dict(bind_dot=23187)
    },
    NpcSkill: {15076: {}}
}
SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {9357: {}, 9361: {}, 23187: {}}
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
