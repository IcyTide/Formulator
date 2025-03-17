from typing import Dict

from base.skill import Skill


class 丹青吞噬(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        for dot_id in self.consume_dots:
            parser.current_dot_ticks[dot_id] += 1
        super().record(actual_critical_strike, actual_damage, parser)


class 清流判定(Skill):
    bind_buff = 711
    final_buff = 12588

    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_dot_ticks.get(self.bind_buff):
            parser.refresh_buff(self.final_buff, 1)


class 涓流判定(Skill):
    final_buff = -9722
    max_stack = 10

    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[self.final_buff].get(1, 0) >= self.max_stack:
            parser.clear_buff(self.final_buff)
        else:
            parser.refresh_buff(self.final_buff, 1)


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
            # 通用
            16: dict(channel_interval=16), 32467: {},
            # 养心诀
            136: dict(post_buffs={1487: {1: 1}}),
            # 点穴截脉
            6693: {}, 14941: {},
            # 百花拂穴手
            182: {}, 186: {}, 6233: {},
            # 奇穴
            38955: {}, 26696: {}, 32501: {}, 32629: {}, 30648: {}, 37270: {},

            **{skill_id: dict(bind_dots={711: 1}) for skill_id in (18730, 6136, 39906, 13848)},
            **{skill_id: dict(bind_dots={714: 1}) for skill_id in (285, 6135, 39907, 13847)},
            **{skill_id: dict(bind_dots={666: 1}) for skill_id in (180, 6134, 13849)},
            6129: dict(consume_dots=[{}, {711: 0}, {711: 0}, {}, {711: 0}, {711: 0}]),
            6126: dict(consume_dots=[{}, {714: 0}, {714: 0}, {}, {714: 0}, {714: 0}]),
            6128: dict(consume_dots=[{}, {666: 0}, {666: 0}, {}, {666: 0}, {666: 0}]),
            # 奇穴
            601: dict(consume_dots=[{dot_id: 0} for dot_id in (714, 666, 711, 24158)] * 3),
            # 装备
            25768: {},
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
