from typing import Dict

from base.skill import Skill
from general.skills import GENERAL_SKILLS


class 诛邪镇魔(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.buff_stacks[(25759, 1)]:
            parser.clear_buff(25759, 1)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_buff(25759, 1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        32816: {}, 4326: {}, 19055: {}, 13468: {}, 3963: {}, 4035: {}, 4036: {}, 4476: {}, 4480: {}, 4482: {},
        18280: {}, 18281: {}, 26708: {}, 26709: {}, 35056: {}, 35057: {}, 34985: {}, 34348: {}, 34349: {}, 34362: {},
        34363: {}, 34359: {}, 34361: {}, 37336: {}, 25777: {}, 35065: {},
        18631: dict(post_buffs={-12575: {1: 1}}),
        **{skill_id: {} for skill_id in range(4483, 4490 + 1)},
        13359: dict(bind_dot=4202),
        **{skill_id: dict(bind_dot=25725) for skill_id in (34373, 35038)},
        **{skill_id: dict(bind_dot=25726) for skill_id in (34374, 35039)}
    },
    诛邪镇魔: {26916: {}}
}
SKILLS: Dict[int, Skill] = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        skill.set_asset()
        SKILLS[skill_id] = skill
