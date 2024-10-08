from typing import Dict

from base.skill import Skill, NpcSkill


class 射日加成(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_target_buff_stacks.get((71182, 1)):
            parser.refresh_target_buff(70188, 20)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 20, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 白泽加成(NpcSkill):
    pass


class 贯穿(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if 35759 in parser.select_talents[parser.current_player]:
            current_stack = parser.current_dot_stacks.get(26856, 0)
            if parser.current_dot_ticks.get(26856) and current_stack == 6:
                if parser.current_target_buff_stacks[-1].get(1, 0) < 3:
                    parser.current_dot_ticks[26856] += 4
                    parser.refresh_target_buff(-1, 1)
            else:
                super().record(actual_critical_strike, actual_damage, parser)
                parser.clear_target_buff(-1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            35894: dict(channel_interval=24), 35866: {}, 35987: {}, 36157: {}, 36177: {}, 36453: {}, 36579: {},
            36580: {},
            36165: dict(consume_dots={26856: 3}),
            35695: dict(pet_buffs={26857: {1: 1}}),
            35696: dict(pet_count=3, pet_buffs={26857: {1: 1}})
        },
        贯穿: {
            35771: dict(bind_dots={26856: 1})
        },
        NpcSkill: {
            36056: {}, 36057: {}, 36111: {}, 36112: {}, 36113: {}, 36114: {},
        }
    },
    1: {
        射日加成: {
            102019: {}, 102018: {}, 102037: {}, 102027: {}, 101998: {}, 102035: {},
            102211: dict(bind_dots={71175: 1}),
        },
        白泽加成: {
            102028: {}, 102029: {}, 102030: {}, 102031: {}, 102032: {}, 102033: {},
        }
    }
}
