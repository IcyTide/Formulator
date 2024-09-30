from typing import Dict

from base.skill import Skill


class 折花吞噬(Skill):
    consume_dots = {
        i + 9: dot_id for i, dot_id in enumerate([714, 666, 711, 24158])
    }

    def record(self, actual_critical_strike, actual_damage, parser):
        self.consume_dot = self.consume_dots[self.skill_level]
        super().record(actual_critical_strike, actual_damage, parser)


class 丹青吞噬(Skill):
    consume_dots = {
        i: dot_id for i, dot_id in enumerate([666, 714, 711, 24158])
    }
    consume_tick = 1

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


class 快雪时晴秘章(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_dot_ticks.get(70041):
            parser.refresh_target_buff(70188, 35)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 35, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            16: dict(channel_interval=16), 182: {}, 186: {},6233: {}, 6693: {}, 14941: {}, 25768: {}, 32467: {},
            32501: {}, 37270: {}, 32629: {}, 30648: {},33222: {},
            37525: dict(pre_buffs={28116: {1: 1}}), 2645: dict(post_buffs={14636: {1: 1}}),
            **{skill_id: dict(bind_dot=711) for skill_id in (18730, 13848, 6136)},
            **{skill_id: dict(bind_dot=714) for skill_id in (285, 3086, 13847, 6135)},
            **{skill_id: dict(bind_dot=666) for skill_id in (180, 13849, 6134)},
            **{skill_id: dict(bind_dot=24158) for skill_id in (32481, 32409)},
            6129: dict(consume_dot=711),
            6126: dict(consume_dot=714),
            6128: dict(consume_dot=666),
            32410: dict(consume_dot=24158)
        },
        折花吞噬: {601: {}},
        丹青吞噬: {32630: {}},
        清流判定: {18722: {}}
    },
    1: {
        Skill: {
            101939: {}, 100047: {}, 100041: {},
            101593: dict(bind_dot=70041),
            100043: dict(consume_dot=70041)
        },
        快雪时晴秘章: {
            100458: {}, 101583: {}
        }
    }
}
