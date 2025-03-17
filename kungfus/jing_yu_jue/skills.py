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
            # 通用
            3121: dict(channel_interval=16), 32884: {},
            # 百步穿杨
            3187: {}, 3095: {}, 6920: {},
            # 乾坤一掷
            3222: {}, **{skill_id: {} for skill_id in (21841, 21840, 3227, 8470, 8469, 8468, 8467)},
            # 奇穴
            3291: {}, 22789: {}, 37504: {}, 33870: {},
            # 装备
            25775: {},
            3125: dict(bind_dots={2237: 1})
        },
        逐一击破判定: {
            26551: {}
        }
    }
}
