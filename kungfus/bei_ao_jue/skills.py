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
            # 通用
            **{skill_id: dict(channel_interval=24) for skill_id in (16419, 16820, 16822)}, 32823: {},
            # 殷雷腿
            16599: {}, 16631: {}, **{skill_id: {} for skill_id in (16097, 16753, 16774, 16775)},
            # 秀明尘身
            20991: {}, **{skill_id: {} for skill_id in (16758, 16759, 16760, 16382)},
            **{skill_id: {} for skill_id in (16800, 16801, 16802, 16803, 16804, 17043, 19423, 19424)},
            # 松烟竹雾
            17092: {}, **{skill_id: dict(bind_dots={11447: 1}) for skill_id in (17058, 17060)},
            **{skill_id: {} for skill_id in range(16933, 16944 + 1)},
            # 雪絮金屏
            16794: {}, **{skill_id: {} for skill_id in range(16787, 16791 + 1)},
            **{skill_id: {} for skill_id in range(16610, 16614 + 1)},
            **{skill_id: {} for skill_id in range(16615, 16619 + 1)},
            # 奇穴
            38533: {}, 37984: {}, 38537: {}, 34585: {},
            # 装备
            25782: {}, 39106: {},
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
