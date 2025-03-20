from typing import Dict

from base.skill import Skill


class 明法判定(Skill):
    final_buff = 19635
    bind_buff_1 = 890
    bind_buff_2 = 12479

    def record(self, actual_critical_strike, actual_damage, parser):
        if buff_level := parser.current_target_buff_stacks[self.bind_buff_1].get(1):
            parser.refresh_target_buff(self.final_buff, buff_level)
        elif buff_level := parser.current_target_buff_stacks[self.bind_buff_2].get(1):
            parser.refresh_target_buff(self.final_buff, buff_level)


class 明法移除(Skill):
    final_buff = 19635

    def record(self, actual_critical_strike, actual_damage, parser):
        parser.clear_target_buff(self.final_buff)


class 降魔(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[13910].get(1):
            parser.clear_buff(13910)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_buff(13910, 1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        11: dict(channel_interval=27), 19090: {}, 32887: {},
        # 罗汉棍法
        236: {}, 17641: {}, 17642: {}, **{skill_id: {} for skill_id in range(3848, 3850 + 1)},
        **{skill_id: dict(bind_dots={743: 1}) for skill_id in (3808, 3810, 3830)},
        # 龙爪功
        14951: {}, 3814: {}, 3816: {}, **{skill_id: {} for skill_id in range(13681, 13686 + 1)},
        # 袈裟伏魔功
        28619: {},
        # 奇穴
        38615: {}, **{skill_id: {} for skill_id in range(36049, 36051 + 1)}, 32656: {}, 32659: {}, 32660: {},
        # 装备
        25766: {},
    },
    明法判定: {26989: {}},
    明法移除: {26991: {}},
    降魔: {271: {}}
}
