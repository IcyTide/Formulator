from typing import Dict

from base.skill import Skill
from general.skills import GENERAL_SKILLS


class 百节判定(Skill):
    final_buff = 15926

    def record(self, actual_critical_strike, actual_damage, parser):
        if stack := parser.current_buff_stacks[self.final_buff].get(1, 0):
            parser.refresh_buff(self.final_buff + stack, 1)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.clear_buff(self.final_buff + stack, 1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)
        parser.refresh_buff(self.final_buff + min(stack + 1, 3), 1)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        22126: {}, 32822: {}, 22170: {}, 22550: {}, 22551: {}, 22298: {}, 22621: {}, 22620: {}, 22610: {}, 22611: {},
        22612: {}, 22604: {}, 22605: {}, 22490: {}, 22554: {}, 25314: {}, 34981: {}, 29751: {}, 22761: {}, 25784: {},
        22359: {},
        **{skill_id: {} for skill_id in range(36265, 36270 + 1)},
        22330: dict(bind_dot=15568),
        26980: dict(bind_dot=19626),
        22787: dict(pre_buffs={15932: {1: 1}}),
    },
    百节判定: {skill_id: {} for skill_id in (36267, 22604, 22328)}
}
SKILLS: Dict[int, Skill] = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        SKILLS[skill_id] = skill = skill_class(skill_id)
        skill.set_asset(attrs)
