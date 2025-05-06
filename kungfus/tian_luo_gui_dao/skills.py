from typing import Dict

from base.skill import Skill


class 杀机断魂移除(Skill):
    final_buff = -24668

    def record(self, actual_critical_strike, actual_damage, parser):
        parser.clear_buff(self.final_buff, 1)


class 杀机断魂千机变(杀机断魂移除):
    def record(self, actual_critical_strike, actual_damage, parser):
        if buff_stack := parser.current_buff_stacks[24669].get(1):
            parser.refresh_buff(self.final_buff, 1, buff_stack)


class 杀机断魂天绝地灭(杀机断魂移除):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[16236].get(1):
            parser.refresh_buff(self.final_buff, 1, 6)
        elif parser.current_buff_stacks[16235].get(1):
            parser.refresh_buff(self.final_buff, 1, 4)
        elif parser.current_buff_stacks[16234].get(1):
            parser.refresh_buff(self.final_buff, 1, 2)


class 杀机断魂暗藏杀机(杀机断魂移除):
    def record(self, actual_critical_strike, actual_damage, parser):
        parser.refresh_buff(self.final_buff, 1, 3)


SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        3121: dict(channel_interval=16), 32885: {},
        # 九宫飞星
        3105: {}, 18776: {}, 3393: {}, 3126: dict(bind_dots={3221: 1}), 3313: {}, 36502: {},
        3401: {}, 3404: {}, 3819: {}, 3824: {}, 3367: {},
        # 乾坤一掷
        3223: {}, 3228: {},
        # 奇穴
        30894: {}, 30727: {}, 21266: dict(bind_dots={14611: 1}), 38760: dict(bind_dots=[{}, {29549: 1}]),

        26900: {}, 26901: {}, 15049: dict(post_buffs={10005: {1: 1}}), 31026: {}, 31027: {}, 18677: {}, 28441: {},
        29687: dict(consume_dots={dot_id: (3, 3) for dot_id in (3221, 14611)}),
        # 装备
        25774: {}, 3480: {},
    },
    杀机断魂移除: {33145: {}},
    杀机断魂千机变: {33142: {}},
    杀机断魂天绝地灭: {33143: {}},
    杀机断魂暗藏杀机: {33144: {}}
}
