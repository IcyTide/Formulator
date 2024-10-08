from typing import Dict

from base.skill import Skill


class 丹青吞噬(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        for dot_id in self.consume_dots:
            parser.current_dot_ticks[dot_id] += 1
        super().record(actual_critical_strike, actual_damage, parser)


class 清流判定(Skill):
    bind_buff = 711
    final_buff = -12588

    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_dot_ticks.get(self.bind_buff):
            parser.refresh_buff(self.final_buff, 1)
        else:
            parser.clear_buff(self.final_buff)


class 涓流判定(Skill):
    final_buff = -9722
    max_stack = 10

    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[self.final_buff].get(1, 0) >= self.max_stack:
            parser.clear_buff(self.final_buff)
        else:
            parser.refresh_buff(self.final_buff, 1)


class 快雪时晴(Skill):
    final_buff = -24599
    max_stack = 3

    def record(self, actual_critical_strike, actual_damage, parser):
        if buff_levels := parser.current_buff_stacks[self.final_buff]:
            buff_level = max(buff_levels)
            if buff_level < self.max_stack:
                parser.clear_buff(self.final_buff)
                parser.refresh_buff(self.final_buff, buff_level + 1, buff_level + 1)
        else:
            parser.refresh_buff(self.final_buff, 1, 1)
        super().record(actual_critical_strike, actual_damage, parser)


class 玉石俱焚(Skill):
    final_buff = -24599

    def record(self, actual_critical_strike, actual_damage, parser):
        super().record(actual_critical_strike, actual_damage, parser)
        parser.clear_buff(-24599)


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
            16: dict(channel_interval=16), 186: {}, 6693: {}, 14941: {}, 25768: {}, 32467: {}, 32501: {}, 37270: {},
            32629: {}, 30648: {}, 33222: {},
            37525: dict(pre_buffs={28116: {1: 1}}), 2645: dict(post_buffs={14636: {1: 1}}),
            **{skill_id: dict(bind_dots={711: 1}) for skill_id in (18730, 13848, 6136)},
            **{skill_id: dict(bind_dots={714: 1}) for skill_id in (285, 3086, 13847, 6135)},
            **{skill_id: dict(bind_dots={666: 1}) for skill_id in (180, 13849, 6134)},
            **{skill_id: dict(bind_dots={24158: 1}) for skill_id in (32481, 32409)},
            601: dict(consume_dots=[{dot_id: 0} for dot_id in (714, 666, 711, 24158)] * 3),
            6129: dict(consume_dots=[{}, {711: 0}, {711: 0}] * 2),
            6126: dict(consume_dots=[{}, {714: 0}, {714: 0}] * 2),
            6128: dict(consume_dots=[{}, {666: 0}, {666: 0}] * 2),
            32410: dict(consume_dots={24158: 0})
        },
        快雪时晴: {
            6233: {}
        },
        玉石俱焚: {
            182: {}
        },
        丹青吞噬: {
            32630: dict(consume_dots=[{dot_id: 1} for dot_id in (666, 714, 711, 24158)])
        },
        清流判定: {18722: {}},
        涓流判定: {14644: {}}
    },
    1: {
        Skill: {
            101939: {}, 100047: {}, 100041: {},
            101593: dict(bind_dots={70041: 1}),
            100043: dict(consume_dots={70041: 0})
        },
        快雪时晴秘章: {
            100458: {}, 101583: {}
        }
    }
}
