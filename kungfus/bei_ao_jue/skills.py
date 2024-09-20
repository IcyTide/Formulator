from typing import Dict

from base.skill import Skill


class 项王击鼎秘章(Skill):
    damage_addition_add = 256


class 霸王加成(项王击鼎秘章):
    def record(self, actual_critical_strike, actual_damage, parser):
        if stack := parser.current_buff_stacks[71047].get(1):
            parser.refresh_target_buff(70188, 10 * stack)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 10 * stack, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 闹须弥秘章(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_dot_ticks.get(70364):
            parser.refresh_target_buff(70188, 50)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 50, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            **{skill_id: dict(channel_interval=24) for skill_id in (16419, 16820, 16822)},
            32823: {}, 16599: {}, 16631: {}, 16794: {}, 16760: {}, 16382: {}, 17092: {}, 20991: {}, 19424: {},
            30645: {}, 34585: {}, 32859: {}, 37984: {}, 25782: {}, 38533: {}, 38537: {}, 16097: {}, 16753: {},
            **{skill_id: {} for skill_id in range(16787, 16791 + 1)},
            **{skill_id: {} for skill_id in range(16610, 16614 + 1)},
            **{skill_id: {} for skill_id in range(16615, 16619 + 1)},
            **{skill_id: {} for skill_id in range(16933, 16944 + 1)},
            **{skill_id: {} for skill_id in (16804, 16803, 16802, 16801, 16800, 17043, 19423)},
            **{skill_id: dict(bind_dot=11447) for skill_id in (17058, 17060)},
            26934: dict(bind_dot=19555)
        }
    },
    1: {
        Skill: {
            101198: {}, 101200: {}, 101080: {}, 101110: {}, 101109: {}, 101108: {}, 101260: {}, 101259: {},
            101257: {},
            101258: {}, 101256: {},
        },
        项王击鼎秘章: {
            101001: {}, 101000: {}, 100999: {}
        },
        霸王加成: {
            101050: {}
        },
        闹须弥秘章: {
            101068: dict(bind_dot=70364)
        }
    }
}
