from typing import Dict

from assets.setter import set_skill, set_dot
from base.skill import Skill, NpcSkill
from base.dot import Dot
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        35866: {}, 35894: {}, 35987: {}, 36157: {}, 36177: {}, 36453: {}, 36579: {}, 36580: {},
        35771: dict(bind_dot=26856),
        36165: dict(consume_dot=26856, consume_tick=3),
        35695: dict(pet_buffs={(26857, 1): 1}),
        35696: dict(pet_count=3, pet_buffs={(26857, 1): 1})
    },
    NpcSkill: {
        36056: {}, 36057: {}, 36111: {}, 36112: {}, 36113: {}, 36114: {},
    }
}
SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {26856: {}},
}


class 射日加成(Skill):
    talent_activate = False

    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_target_buff_stacks.get((71182, 1)):
            parser.refresh_target_buff(70188, 20)
        if self.talent_activate:
            parser.refresh_target_buff(70188, 25)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 25, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)
        if parser.current_target_buff_stacks.get((71182, 1)):
            parser.refresh_target_buff(70188, 20, -1)


class 白泽加成(NpcSkill):
    talent_activate_1 = False
    talent_activate_2 = False

    def record(self, actual_critical_strike, actual_damage, parser):
        if self.talent_activate_1:
            parser.refresh_target_buff(70188, 30)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 30, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)
        if self.talent_activate_2:
            parser.refresh_target_buff(71182, 1)


MOBILE_SKILLS: Dict[type, Dict[int, dict]] = {
    射日加成: {
        102019: {}, 102018: {}, 102037: {}, 102027: {}, 101998: {}, 102035: {},
        102211: dict(bind_dot=71175),
    },
    白泽加成: {
        102028: {}, 102029: {}, 102030: {}, 102031: {}, 102032: {}, 102033: {},
    }
}
MOBILE_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {
        71175: {}
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
