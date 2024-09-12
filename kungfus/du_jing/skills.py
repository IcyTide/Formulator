from typing import Dict

from base.skill import Skill, PetSkill


class 曲致判定(PetSkill):
    final_buff = -17988

    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_dot_ticks.get(2296) or parser.current_dot_ticks.get(25917):
            parser.refresh_buff(self.final_buff, 1)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.clear_buff(self.final_buff, 1)
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


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            2183: dict(channel_interval=16), 3067: {}, 13472: {}, 18590: {}, 25044: {}, 25773: {}, 29573: {}, 30918: {},
            32818: {}, 34389: {}, 6648: {}, 37959: {},
            13476: dict(bind_dot=6218),
            34643: dict(bind_dot=25917),
            6238: dict(bind_dot=2509),
            18700: dict(bind_dot=12557),
            6237: dict(bind_dot=2296),
            6236: dict(bind_dot=2295),
            26226: dict(bind_dot=18882),
            2226: dict(post_buffs={2543: {1: 1}}),
            2223: dict(pet_buffs={16543: {1: 1}})
        },
        连缘蛊判定: {26914: {}},
        曲致判定: {
            2472: {}, 22997: {}, 36292: {}, 25019: {}
        },
    }
}
