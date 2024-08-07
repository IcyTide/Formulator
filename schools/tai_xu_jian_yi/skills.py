from typing import Dict

from assets.setter import set_skill, set_dot
from base.dot import Dot
from base.skill import Skill
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        18121: dict(damage_addition=205),
        589: {}, 4954: {}, 13853: {}, 21726: {}, 21979: {}, 25771: {}, 32814: {}, 34693: {}, 34694: {},
        2681: dict(post_buffs={(2757, 1): 1}),
        **{skill_id: {} for skill_id in range(386, 394 + 1)},
        **{skill_id: {} for skill_id in range(6076, 6085 + 1)},
        32408: dict(consume_dot=748, consume_tick=1),
        600: dict(bind_dot=748),
        37453: dict(bind_dot=889),
        30944: dict(bind_dot=23170)
    }
}
SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {
        748: {}, 889: {}, 23170: {}
    }
}
MOBILE_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        100010: {}, 100011: {}, 101658: {}, 100374: {}, 100019: {}, 100012: {}, 100017: {}, 100003: {}, 100008: {},
        101633: {},
        101581: dict(bind_dot=70624),
        100021: dict(consume_dot=70624),
        101634: dict(consume_dot=70624),
    }
}
MOBILE_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {
        70624: {}
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
for skill_class, skills in MOBILE_SKILLS.items():
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
for dot_class, dots in MOBILE_DOTS.items():
    for dot_id, attrs in dots.items():
        dot = dot_class(dot_id)
        for attr, value in attrs.items():
            setattr(dot, attr, value)
        set_dot(dot)
        DOTS[dot_id] = dot
