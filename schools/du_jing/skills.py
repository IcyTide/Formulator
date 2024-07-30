from typing import Dict

from assets.setter import set_skill, set_dot
from base.dot import Dot
from base.skill import Skill, PetSkill
from general.skills import GENERAL_SKILLS


class 曲致判定(PetSkill):
    final_buff = -17988

    def record(self, actual_critical_strike, actual_damage, parser):
        if 2296 in parser.current_dot_stacks or 25917 in parser.current_dot_stacks:
            parser.refresh_buff(self.final_buff, 1)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.clear_buff(self.final_buff, 1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 连缘蛊判定(Skill):
    final_buff = -19513

    def record(self, actual_critical_strike, actual_damage, parser):
        buff_level = 0
        if 6218 in parser.current_dot_stacks:
            buff_level += 1
        if 2296 in parser.current_dot_stacks or 25917 in parser.current_dot_stacks:
            buff_level += 1
        if 2509 in parser.current_dot_stacks or 12557 in parser.current_dot_stacks:
            buff_level += 1
        if 2295 in parser.current_dot_stacks:
            buff_level += 1
        if buff_level:
            for i in range(4):
                parser.clear_buff(self.final_buff, i + 1)
            parser.refresh_buff(self.final_buff, buff_level)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        2183: dict(damage_addition=205),
        3067: {}, 13472: {}, 18590: {}, 25044: {}, 25773: {}, 29573: {}, 30918: {}, 32818: {}, 34389: {}, 6648: {},
        37959: {},
        13476: dict(bind_dot=6218),
        34643: dict(bind_dot=25917),
        6238: dict(bind_dot=2509),
        18700: dict(bind_dot=12557),
        6237: dict(bind_dot=2296),
        6236: dict(bind_dot=2295),
        26226: dict(bind_dot=18882),
        2226: dict(post_buffs={(2543, 1): 1}),
        2223: dict(pet_buffs={(16543, 1): 1})
    },
    连缘蛊判定: {26914: {}},
    曲致判定: {
        2472: {}, 22997: {}, 36292: {}, 25019: {}
    },
}
SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {
        6218: {}, 2509: {}, 12557: {}, 2295: {}, 18882: {},
        2296: dict(tick_extra=1),
        25917: dict(tick_extra=1),
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
