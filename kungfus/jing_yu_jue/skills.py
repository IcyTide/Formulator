from typing import Dict

from base.skill import Skill


class 逐一击破判定(Skill):
    final_buff = 10169

    def record(self, actual_critical_strike, actual_damage, parser):
        if not parser.current_buff_stacks[10167].get(1):
            parser.refresh_buff(self.final_buff, 1)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            3121: dict(channel_interval=16), 3095: {}, 3187: {}, 3222: {}, 3227: {}, 3291: {}, 6920: {}, 22789: {},
            25775: {}, 32884: {}, 37616: {}, 33870: {}, 37504: {},
            **{skill_id: {} for skill_id in (21841, 21840, 8470, 8469, 8468, 8467)},
            3125: dict(bind_dot=2237),
            3478: dict(bind_dot=19625)
        },
        逐一击破判定: {
            26551: {}
        }
    }
}
