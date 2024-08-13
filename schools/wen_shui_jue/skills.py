from typing import Dict

from base.skill import Skill
from general.skills import GENERAL_SKILLS


class 啸日(Skill):
    final_buff = -1

    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks.get((self.final_buff, 1)):
            parser.clear_buff(self.final_buff, 1)
        else:
            parser.refresh_buff(self.final_buff, 1)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        18381: dict(damage_addition=205),
        1795: dict(channel_interval_extra=2., damage_addition=205),
        1594: {}, 1595: {}, 1598: {}, 1706: {}, 1707: {}, 2896: {}, 13471: {}, 18299: {}, 18317: {}, 18685: {},
        18991: {}, 25776: {}, 26673: {}, 30861: {}, 32821: {}, 32967: {}, 34984: {}, 35051: {}
    },
    啸日: {1656: {}},
}
SKILLS = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        skill.set_asset()
        SKILLS[skill_id] = skill
DOTS = {}
