from typing import Dict

from base.skill import Skill


class 用晦而明判定(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        level = 1
        check_buff_id = 30644 + self.skill_level - 1
        if parser.current_buffs[check_buff_id]:
            level = 2

        parser.refresh_buff(12575, level)


SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        4326: dict(channel_interval=16), 32816: {}, 19055: {},
        # 日月净世
        14701: {}, 4476: {}, 40088: {}, 40089: {}, 6257: {}, 6258: {},
        13359: dict(bind_dots={4202: 1}),
        # 御暗烬灭令
        4480: {}, 4482: {},
        # 奇穴
        18280: {}, 18281: {}, 26916: {}, 26708: {}, 26709: {}, 18631: dict(post_buffs={-12575: {1: 1}}),
        34985: {}, 34348: {}, 34349: {}, 34356: {}, 34355: {}, 34359: {}, 34361: {}, 34362: {}, 34363: {},
        34373: dict(bind_dots={25725: 1}), 34374: dict(bind_dots={25726: 1}),
        37336: {},
        # 装备
        25777: {}, 35065: {},
    },
    用晦而明判定: {40655: {}}
}
