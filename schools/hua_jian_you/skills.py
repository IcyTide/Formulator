from typing import Dict

from assets.setter import set_skill
from base.skill import Skill, Dot
from general.skills import GENERAL_SKILLS


class 吞噬(Skill):
    bind_buff_levels: dict
    bind_buff = -1

    def record(self, actual_critical_strike, actual_damage, parser):
        if buff_level := self.bind_buff_levels.get(self.skill_level):
            parser.refresh_buff(self.bind_buff, buff_level)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.clear_buff(self.bind_buff, buff_level)


class 折花吞噬(吞噬):
    consume_dots = {
        **{i + 9: skill_id for i, skill_id in enumerate([714, 666, 711, 24158])}
    }
    bind_buff_levels = {
        **{i + 9: 1 for i in range(4)}
    }

    def record(self, actual_critical_strike, actual_damage, parser):
        self.consume_dot = self.consume_dots[self.skill_level]
        super().record(actual_critical_strike, actual_damage, parser)


class 清流判定(Skill):
    bind_buff = 711
    final_buff = -12588

    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_dot_stacks.get(self.bind_buff):
            parser.refresh_buff(self.final_buff, 1)
        else:
            parser.clear_buff(self.final_buff, 1)


class 快雪时晴(Skill):
    final_buff = -24599
    max_level = 3

    def record(self, actual_critical_strike, actual_damage, parser):
        if not parser.current_buff_stacks.get((self.final_buff, self.max_level)):
            for buff_level in range(1, self.max_level):
                if buff_stack := parser.current_buff_stacks.get((self.final_buff, buff_level)):
                    parser.clear_buff(self.final_buff, buff_level)
                    parser.refresh_buff(self.final_buff, buff_level + 1, buff_stack + 1)
                    break
            else:
                parser.refresh_buff(self.final_buff, 1, 1)
        super().record(actual_critical_strike, actual_damage, parser)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        16: dict(damage_addition=205),
        186: {}, 6693: {}, 14941: {}, 25768: {}, 32467: {}, 32501: {}, 37270: {},
        37525: dict(pre_buffs={(28116, 1): 1}),
        2645: dict(post_buffs={(-14636, 1): 1}),
        182: dict(post_buffs={(-14636, 1): -1, **{(-24599, i + 1): -i - 1 for i in range(3)}}),
        **{skill_id: dict(bind_dot=711) for skill_id in (18730, 13848, 6136)},
        **{skill_id: dict(bind_dot=714) for skill_id in (285, 3086, 13847, 6135)},
        **{skill_id: dict(bind_dot=666) for skill_id in (180, 13849, 6134)},
        **{skill_id: dict(bind_dot=24158) for skill_id in (32481, 32409)},
    },
    Dot: {
        711: dict(tick_extra=1),
        714: dict(tick_extra=1),
        666: dict(tick_extra=1),
        24158: {}
    },
    快雪时晴: {33222: {}},
    吞噬: {
        6129: dict(consume_dot=711, bind_buff_levels={5: 2, 6: 1}),
        6126: dict(consume_dot=714, bind_buff_levels={5: 2, 6: 1}),
        6128: dict(consume_dot=666, bind_buff_levels={5: 2, 6: 1}),
        32410: dict(consume_dot=24158, bind_buff_levels={2: 2, 3: 1})
    },
    折花吞噬: {601: {}},
    清流判定: {18722: {}}
}
SKILLS = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        set_skill(skill)
        SKILLS[skill_id] = skill
