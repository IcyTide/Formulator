from typing import Dict

from base.skill import Skill
from general.skills import GENERAL_SKILLS


class 折花吞噬(Skill):
    consume_dots = {
        **{i + 9: skill_id for i, skill_id in enumerate([714, 666, 711, 24158])}
    }

    def record(self, actual_critical_strike, actual_damage, parser):
        self.consume_dot = self.consume_dots[self.skill_level]
        super().record(actual_critical_strike, actual_damage, parser)


class 清流判定(Skill):
    bind_buff = 711
    final_buff = -12588

    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_dot_ticks.get(self.bind_buff):
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
        2645: dict(post_buffs={(14636, 1): 1}),
        182: dict(post_buffs={(-24599, i + 1): 0 for i in range(3)}),
        **{skill_id: dict(bind_dot=711) for skill_id in (18730, 13848, 6136)},
        **{skill_id: dict(bind_dot=714) for skill_id in (285, 3086, 13847, 6135)},
        **{skill_id: dict(bind_dot=666) for skill_id in (180, 13849, 6134)},
        **{skill_id: dict(bind_dot=24158) for skill_id in (32481, 32409)},
        6129: dict(consume_dot=711),
        6126: dict(consume_dot=714),
        6128: dict(consume_dot=666),
        32410: dict(consume_dot=24158)
    },
    快雪时晴: {33222: {}},
    折花吞噬: {601: {}},
    清流判定: {18722: {}}
}


class 快雪时晴秘章(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_dot_ticks.get(70041):
            parser.refresh_target_buff(70188, 35)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 35, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


MOBILE_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        101939: {}, 100047: {}, 100041: {},
        101593: dict(bind_dot=70041),
        100043: dict(consume_dot=70041)
    },
    快雪时晴秘章: {
        100458: {}, 101583: {}
    }
}
SKILLS: Dict[int, Skill] = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        skill.set_asset()
        SKILLS[skill_id] = skill
for skill_class, skills in MOBILE_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        skill.set_asset()
        SKILLS[skill_id] = skill
