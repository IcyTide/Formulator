from typing import Dict

from base.skill import Skill
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        1795: dict(channel_interval=32), 18383: dict(channel_interval=21), 1594: {}, 1595: {}, 1598: {}, 1706: {},
        1707: {}, 2896: {}, 13471: {}, 18299: {}, 18317: {}, 18685: {}, 18991: {}, 25776: {}, 26673: {}, 30861: {},
        32821: {}, 32967: {}, 34984: {}, 35051: {},
        1658: dict(post_buffs={-1: {1: 1}}),
        1659: dict(post_buffs={-1: {1: 0}})
    },
}
SKILLS: Dict[int, Skill] = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        SKILLS[skill_id] = skill = skill_class(skill_id)
        skill.set_asset(attrs)
