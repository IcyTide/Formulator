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
            32823: {}, 16599: {}, 16631: {}, 16794: {}, 17092: {}, 20991: {}, 19424: {}, 34585: {}, 32859: {},
            37984: {}, 25782: {}, 38533: {}, 38537: {}, 39106: {},
            **{skill_id: {} for skill_id in (16758, 16759, 16760, 16382)},
            **{skill_id: {} for skill_id in range(16787, 16791 + 1)},
            **{skill_id: {} for skill_id in range(16610, 16614 + 1)},
            **{skill_id: {} for skill_id in range(16913, 16918 + 1)},
            **{skill_id: {} for skill_id in range(16615, 16619 + 1)},
            **{skill_id: {} for skill_id in range(16920, 16925 + 1)},
            **{skill_id: {} for skill_id in range(16933, 16944 + 1)},
            **{skill_id: {} for skill_id in (16804, 16803, 16802, 16801, 16800, 17043, 19423)},
            **{skill_id: {} for skill_id in (16097, 16753, 16774, 16775)},
            **{skill_id: dict(bind_dots={11447: 1}) for skill_id in (17058, 17060)},
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
            101068: dict(bind_dots={70364: 1})
        }
    }
}
