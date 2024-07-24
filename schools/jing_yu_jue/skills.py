from typing import Dict

from assets.setter import set_skill, set_dot
from base.dot import Dot
from base.skill import Skill
from general.skills import GENERAL_SKILLS


class 逐一击破增伤(Skill):
    bind_buff = 1
    final_buff = -1

    def record(self, actual_critical_strike, actual_damage, parser):
        parser.refresh_buff(self.final_buff, 1)
        super().record(actual_critical_strike, actual_damage, parser)
        parser.clear_buff(self.final_buff, 1)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        3121: dict(damage_addition=205),
        3222: {}, 3227: {}, 22789: {}, 25775: {}, 32884: {}, 37616: {},
        3478: dict(bind_dot=19625)
    },
    逐一击破增伤: {
        3095: {}, 3187: {}, 6920: {}, 33870: {}, 37504: {},
        3125: dict(bind_dot=2237)
    }
}
SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {
        2237: dict(tick_extra=1),
        19625: {}
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
DOTS = {}
for dot_class, dots in SCHOOL_DOTS.items():
    for dot_id, attrs in dots.items():
        dot = dot_class(dot_id)
        for attr, value in attrs.items():
            setattr(dot, attr, value)
        set_dot(dot)
        DOTS[dot_id] = dot
