from typing import Dict

from assets.setter import set_skill, set_dot
from base.skill import Skill
from base.dot import Dot
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        27451: dict(damage_addition=205),
        32841: {}, 28081: {}, 27552: {}, 27555: {}, 27557: {}, 27579: {}, 27584: {}, 28409: {}, 28346: {}, 34699: {},
        27539: {}, 32922: {}, 27657: {}, 29674: {}, 28385: {}, 28434: {}, 36508: {}, 29698: {}, 29695: {}, 36068: {},
        35367: dict(post_buffs={(24659, 1): 1}),
        **{
            skill_id: dict(consume_dot=20052, consume_tick=2) for skill_id in (29505, 29506, 34700, 34702, 30735)
        },
        27560: dict(bind_dot=20052)
    }
}
SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {20052: {}}
}


class 鬼门加成(Skill):
    talent_activate = False

    def record(self, actual_critical_strike, actual_damage, parser):
        if self.talent_activate and 0 in parser.current_dot_ticks:
            parser.refresh_target_buff(70188, 10)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 10, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 钩吻断肠秘章(鬼门加成):
    damage_addition_extra = 154

    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks.get((70529, 1)):
            parser.refresh_target_buff(70188, 15)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 15, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 苍棘缚地(鬼门加成):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks.get((71230, 1)):
            parser.refresh_target_buff(70188, 10)
        if parser.current_buff_stacks.get((71258, 1)):
            parser.refresh_target_buff(70188, 10)
        super().record(actual_critical_strike, actual_damage, parser)
        if parser.current_buff_stacks.get((71230, 1)):
            parser.refresh_target_buff(70188, 10, -1)
        if parser.current_buff_stacks.get((71258, 1)):
            parser.refresh_target_buff(70188, 10, -1)


MOBILE_SKILLS: Dict[type, Dict[int, dict]] = {
    鬼门加成: {
        102159: {}, 102157: {}, 102158: {}, 102164: {},
        101417: dict(bind_dot=71171),
        102163: dict(consume_dot=71171),
    },
    钩吻断肠秘章: {
        101357: {}, 101358: {},
    },
    苍棘缚地: {
        101425: {}
    }
}
MOBILE_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {
        71171: {}
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
