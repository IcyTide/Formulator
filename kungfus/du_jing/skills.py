from typing import Dict

from base.skill import Skill, PetSkill


class 曲致判定(PetSkill):
    final_buff = -17988

    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_dot_ticks.get(2296) or parser.current_dot_ticks.get(25917):
            parser.refresh_buff(self.final_buff, 1)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.clear_buff(self.final_buff)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 连缘蛊判定(Skill):
    final_buff = -19513

    def record(self, actual_critical_strike, actual_damage, parser):
        buff_level = 0
        if parser.current_dot_ticks.get(6218):
            buff_level += 1
        if parser.current_dot_ticks.get(2296) or parser.current_dot_ticks.get(25917):
            buff_level += 1
        if parser.current_dot_ticks.get(2509) or parser.current_dot_ticks.get(12557):
            buff_level += 1
        if parser.current_dot_ticks.get(2295):
            buff_level += 1
        if buff_level:
            parser.clear_buff(self.final_buff)
            parser.refresh_buff(self.final_buff, buff_level)


class 残香吞噬(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        for dot_id in self.consume_dots:
            parser.current_dot_ticks[dot_id] += 1
        super().record(actual_critical_strike, actual_damage, parser)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            2183: dict(channel_interval=16), 3067: {}, 13472: {}, 18590: {}, 25044: {}, 25773: {}, 29573: {}, 30918: {},
            32818: {}, 34389: {}, 6648: {}, 37959: {}, 13473: {}, 21303: {}, 38456: {}, 9331: {},
            13476: dict(bind_dots={6218: 1}),
            34643: dict(bind_dots={25917: 1}),
            6238: dict(bind_dots={2509: 1}),
            18700: dict(bind_dots={12557: 1}),
            6237: dict(bind_dots={2296: 1}),
            6236: dict(bind_dots={2295: 1}),
            26226: dict(bind_dots={18882: 1}),
            2226: dict(post_buffs={2543: {1: 1}}),
            2223: dict(pet_buffs={16543: {1: 1}})
        },
        连缘蛊判定: {
            26914: {}
        },
        曲致判定: {
            2477: {}, 2472: {}, 22997: {}, 36292: {}, 25019: {}
        },
        残香吞噬: {
            38454: dict(consume_dots=[{dot_id: 1} for dot_id in (2296, 25917, 2295, 2509, 12557, 22731, 22730)])
        }
    }
}
