from typing import Dict

from base.skill import Skill


class 一阳指秘章(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[71388].get(1):
            parser.refresh_target_buff(70188, 30)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 30, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 引窍(一阳指秘章):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_target_buff_stacks.get(71382):
            parser.refresh_target_buff(70973, 15)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70973, 15, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 截阳(一阳指秘章):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_target_buff_stacks.get(71382):
            parser.refresh_target_buff(70188, 35)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 35, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 一阳化生(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if buff_stack := parser.current_buff_stacks[71405].get(1):
            parser.refresh_target_buff(70188, 20 * buff_stack)
            parser.refresh_target_buff(70973, 20 * buff_stack)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 20 * buff_stack, -1)
            parser.refresh_target_buff(70973, 20 * buff_stack, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            # 通用
            38034: {}, 38093: {},
            # 一阳指
            38083: {}, 38084: {}, 38085: {}, 38090: {}, 38438: {},
            # 聘风令
            37804: {}, 37816: {}, 38452: {}, 38447: {}, 38453: {},
            # 空蒙扇
            38016: {}, 38075: {}, 38076: {}, 38077: {},
            # 奇穴
            38531: {}, 39340: {}, 38557: {}, 38590: {},
            # 装备
            39081: {},
        }
    },
    1: {
        Skill: {
            102280: {}, 102310: {}, 102312: {}, 102322: dict(post_target_buffs={71382: {1: 1}})
        },
        一阳指秘章: {
            102305: {}, 102311: {}, 102313: {}, 102318: {}, 102323: {}
        },
        引窍: {
            102282: {}
        },
        截阳: {
            102309: {}
        },
        一阳化生: {
            102312: {}
        }
    }
}
