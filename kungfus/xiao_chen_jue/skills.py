from typing import Dict

from base.skill import Skill


class 载物加成(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[70221].get(1) and not any(parser.current_buff_stacks[70167]):
            parser.refresh_buff(70161, 10)
            parser.refresh_buff(70167, 10)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_buff(70161, 10, -1)
            parser.refresh_buff(70167, 10, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 刚健加成(载物加成):
    pass


class 拨狗朝天(刚健加成):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[70221].get(1):
            parser.refresh_target_buff(70188, 50)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 50, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            32908: {}, 13520: {}, 34916: {}, 6337: {}, 26703: {}, 32898: {}, 14927: {}, 14928: {}, 36570: {}, 28819: {},
            25779: {}, 34998: {}, 28952: {},
            **{skill_id: {} for skill_id in range(6355, 6374 + 1)},
            **{skill_id: {} for skill_id in range(13523, 13530 + 1)},
            **{skill_id: dict(bind_dot=6367) for skill_id in (6853, 14930)},
            **{skill_id: dict(bind_dot=6401) for skill_id in (6867, 14931)}
        }
    },
    1: {
        载物加成: {
            100774: {}, 100776: {},
        },
        刚健加成: {
            101960: {}, 100662: {}
        },
        拨狗朝天: {
            100664: {}, 100653: {}
        }
    }
}
