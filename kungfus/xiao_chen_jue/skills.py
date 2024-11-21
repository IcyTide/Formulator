from typing import Dict

from base.skill import Skill


class 御鸿于天(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        super().record(actual_critical_strike, actual_damage, parser)
        for dot_id in (6367, 6401):
            parser.current_dot_ticks.pop(dot_id, None)
            parser.current_dot_stacks.pop(dot_id, None)


class 拨狗朝天秘章(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[70221].get(1):
            parser.refresh_target_buff(70188, 50)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 50, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 蛟龙翻江秘章(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[70889].get(1):
            parser.refresh_target_buff(70188, 20)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 20, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            32908: {}, 13520: {}, 34916: {}, 6337: {}, 26703: {}, 32898: {}, 14928: {}, 36570: {}, 28819: {},
            25779: {}, 34998: {}, 28952: {}, 25201: {}, 25202: {},
            38891: dict(global_damage_factor=1048576 * (0.2925 * 1.15 - 1)),
            **{skill_id: {} for skill_id in range(6355, 6374 + 1)},
            **{skill_id: {} for skill_id in range(13523, 13530 + 1)},
            **{skill_id: dict(bind_dots={6367: 1}) for skill_id in (6853, 14930)},
            **{skill_id: dict(bind_dots={6401: 1}) for skill_id in (6867, 14931)}
        },
        御鸿于天: {
            14927: {}
        }
    },
    1: {
        Skill: {
            101960: {}, 100662: {}, 100773: {}, 100821: {},
            100775: dict(damage_addition_add=51)
        },
        拨狗朝天秘章: {
            100664: {}, 100653: {}
        },
        蛟龙翻江秘章: {
            102332: {}, 100819: {}, 100820: {}, 102331: {}
        }
    }
}
