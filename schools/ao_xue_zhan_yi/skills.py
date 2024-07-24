from typing import Dict

from assets.setter import set_skill, set_dot
from base.dot import Dot
from base.skill import Skill
from general.skills import GENERAL_SKILLS


class 战意判定(Skill):
    final_buff = -12608
    bind_buff = -1

    def record(self, actual_critical_strike, actual_damage, parser):
        if buff_level := parser.current_buff_stacks.get((self.bind_buff, 1)):
            parser.refresh_buff(self.final_buff, buff_level)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        12: dict(damage_additon=205, channel_interval_extra=1.7),
        431: {}, 701: {}, 702: {}, 6525: {}, 6526: {}, 423: {}, 14882: {}, 15002: {}, 24898: {}, 25772: {}, 32820: {},
        37618: {}, 36568: {}, 18207: {}, 18208: {},
        400: dict(post_buffs={(-1, 1): 1}),
        18603: dict(post_buffs={(-1, 1): 2}),
        409: dict(post_buffs={(-1, 1): 3}),
        18773: dict(post_buffs={(-1, 1): -3}),
        401: dict(bind_dot=12461),
        18591: dict(bind_dot=3442),
        31031: dict(post_buffs={(-1, 1): 5})
    },
    战意判定: {18740: {}}
}
SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {
        3442: {},
        12461: dict(tick_extra=3)
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
