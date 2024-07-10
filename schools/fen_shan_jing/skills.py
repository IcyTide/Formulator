from typing import Dict

from assets.setter import set_skill, set_dot
from base.skill import Skill, Dot
from general.skills import GENERAL_SKILLS


class 盾压(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks.get((8474, 13)):
            self.post_buffs[(-1, 1)] = 15 * 2
        else:
            self.post_buffs[(-1, 1)] = 15

        super().record(actual_critical_strike, actual_damage, parser)


class 绝刀(Skill):
    final_buff = -9052
    bind_buff = -1

    def record(self, actual_critical_strike, actual_damage, parser):
        current_rage = parser.current_buff_stacks.get((-1, 1), 0)
        cost_rage = min(current_rage, 50)
        buff_level = cost_rage // 10 - 1
        if buff_level > 0:
            parser.refresh_buff(self.final_buff, buff_level)
        if parser.current_buff_stacks.get((8451, 1)):
            self.post_buffs[(-1, 1)] = 0
        elif parser.current_buff_stacks.get((8474, 13)):
            self.post_buffs[(-1, 1)] = 0
        else:
            self.post_buffs[(-1, 1)] = -cost_rage
        super().record(actual_critical_strike, actual_damage, parser)
        parser.clear_buff(self.final_buff, buff_level)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        32745: {}, 13039: {}, 36065: {}, 36482: {}, 37253: {}, 34673: {}, 34674: {}, 34714: {}, 37448: {}, 30925: {},
        30926: {}, 30857: {}, 30858: {}, 30859: {}, 23284: {}, 23285: {}, 23286: {}, 23287: {}, 23294: {}, 25780: {},
        **{skill_id: dict(post_buffs={(-1, 1): 10}) for skill_id in (13106, 13160, 13161)},
        13099: dict(post_buffs={(-1, 1): 15}),
        13044: dict(post_buffs={(-1, 1): 5}),
        13092: dict(post_buffs={(-1, 1): -15}),
        28479: dict(post_buffs={(-1, 1): -5}),
        13463: dict(post_target_buffs={(-8248, 1): 1}),
        13040: dict(post_buffs={(-1, 1): 10 + 15}),
        16727: dict(post_buffs={(-1, 1): 3}),
        29188: dict(bind_dot=8249, post_target_buffs={(-8248, 1): -1})
    },
    盾压: {19409: {}},
    绝刀: {13075: {}}
}
SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {8249: {}}
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
