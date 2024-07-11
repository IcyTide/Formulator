from typing import Dict

from assets.setter import set_skill, set_dot
from base.skill import Skill
from base.dot import Dot
from general.skills import GENERAL_SKILLS


class 明法判定(Skill):
    final_buff = 19635
    bind_buff_1 = 890
    bind_buff_2 = 12479

    def record(self, actual_critical_strike, actual_damage, parser):
        if buff_level := parser.current_target_buff_stacks.get((self.bind_buff_1, 1)):
            parser.refresh_target_buff(self.final_buff, buff_level)
        elif buff_level := parser.current_target_buff_stacks.get((self.bind_buff_2, 1)):
            parser.refresh_target_buff(self.final_buff, buff_level)


class 明法移除(Skill):
    final_buff = 19635

    def record(self, actual_critical_strike, actual_damage, parser):
        buff_levels = []
        for buff_id, buff_level in parser.current_target_buff_stacks:
            if buff_id == self.final_buff:
                buff_levels.append(buff_level)
        for buff_level in buff_levels:
            parser.clear_target_buff(self.final_buff, buff_level)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        11: dict(damage_addition=205),
        236: {}, 271: {}, 14951: {}, 17641: {}, 17642: {}, 19090: {}, 25766: {}, 28619: {}, 29516: {}, 32656: {},
        32659: {}, 32660: {}, 32887: {}, 3814: {}, 3816: {}, 3848: {}, 3849: {}, 3850: {}, 13685: {}, 28542: {},
        24883: {},
        **{skill_id: dict(bind_dot=743) for skill_id in (3808, 3810, 3830, 28539)},
        24026: dict(consume_dot=743, consume_tick=3)
    },
    明法判定: {26989: {}},
    明法移除: {26991: {}},
}
SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {743: dict(tick_extra=3)}
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
