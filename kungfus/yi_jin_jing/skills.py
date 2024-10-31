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


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            11: dict(channel_interval=27), 233: {}, 236: {}, 243: {}, 271: {}, 14951: {}, 17641: {}, 17642: {},
            19090: {}, 25766: {}, 28619: {}, 32656: {}, 32659: {}, 32660: {}, 32887: {}, 3814: {}, 3816: {}, 28542: {},
            24883: {}, 24028: {}, 38615: {}, 24886: {},
            **{skill_id: {} for skill_id in range(3848, 3850 + 1)},
            **{skill_id: {} for skill_id in range(13681, 13686 + 1)},
            **{skill_id: {} for skill_id in range(36049, 36051 + 1)},
            **{skill_id: dict(bind_dots={743: 1}) for skill_id in (3808, 3810, 3830, 28539)},
            24026: dict(consume_dots={743: 3})
        },
        明法判定: {26989: {}},
        明法移除: {26991: {}}
    }
}
