from typing import Dict

from base.skill import Skill


class 百节判定(Skill):
    final_buff = 15926

    def record(self, actual_critical_strike, actual_damage, parser):
        if stack := parser.current_buff_stacks[self.final_buff].get(1, 0):
            parser.refresh_buff(self.final_buff + stack, 1)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.clear_buff(self.final_buff + stack)
        else:
            super().record(actual_critical_strike, actual_damage, parser)
        parser.refresh_buff(self.final_buff + min(stack + 1, 3), 1)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            22126: dict(channel_interval=24), 32822: {}, 22170: {}, 22550: {}, 22551: {}, 22298: {}, 22621: {},
            22620: {},
            22610: {}, 22611: {}, 22612: {}, 22604: {}, 22605: {}, 22490: {}, 22554: {}, 25314: {}, 34981: {},
            29751: {},
            22761: {}, 25784: {}, 22359: {},
            **{skill_id: {} for skill_id in range(36265, 36270 + 1)},
            22330: dict(bind_dots={15568: 1}),
            26980: dict(bind_dots={19626: 1}),
            22787: dict(pre_buffs={15932: {1: 1}}),
        },
        百节判定: {skill_id: {} for skill_id in (36267, 22604, 22328)}
    }
}
