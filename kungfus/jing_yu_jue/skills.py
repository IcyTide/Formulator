from typing import Dict

from base.skill import Skill


class 逐一击破增伤(Skill):
    common_buff = -23074
    single_buff = -10169

    def record(self, actual_critical_strike, actual_damage, parser):
        parser.refresh_buff(self.common_buff, 1)
        parser.refresh_buff(self.single_buff, 1)
        super().record(actual_critical_strike, actual_damage, parser)
        parser.clear_buff(self.common_buff, 1)
        parser.clear_buff(self.single_buff, 1)


class 追命箭(逐一击破增伤):
    def record(self, actual_critical_strike, actual_damage, parser):
        super().record(actual_critical_strike, actual_damage, parser)
        parser.clear_buff(-28227, 1)
        if not parser.current_buff_stacks[3276].get(1) and parser.current_buff_stacks[-28226].get(1):
            parser.clear_buff(-28226, 1)
            parser.refresh_buff(-28227, 1)
        if not parser.current_buff_stacks[3276].get(1) and parser.current_buff_stacks[-28225].get(1):
            parser.clear_buff(-28225, 1)
            parser.refresh_buff(-28226, 1)
        if parser.current_buff_stacks[3276].get(1):
            parser.clear_buff(-28227, 1)
            parser.clear_buff(-28226, 1)
            parser.refresh_buff(-28225, 1)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            3121: dict(channel_interval=16), 3222: {}, 3227: {}, 22789: {}, 25775: {}, 32884: {}, 37616: {},
            **{skill_id: {} for skill_id in (21841, 21840, 8470, 8469, 8468, 8467)},
            3478: dict(bind_dot=19625)
        },
        逐一击破增伤: {
            3095: {}, 3187: {}, 33870: {}, 37504: {},
            3125: dict(bind_dot=2237)
        },
        追命箭: {
            6920: {}
        }
    }
}
