from typing import Dict

from base.skill import Skill


class 净世破魔击(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[70891].get(1):
            parser.refresh_target_buff(70188, 15)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 15, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            # 通用
            4326: dict(channel_interval=16), 32816: {}, 19055: {},
            # 日月净世
            14701: {}, 4476: {},  40088: {}, 40089: {},
            13359: dict(bind_dots={4202: 1}),
            # 御暗烬灭令
            4480: {}, 4482: {},
            # 奇穴
            18280: {}, 18281: {}, 26916: {}, 26708: {}, 26709: {}, 18631: dict(post_buffs={-12575: {1: 1}}),
            34985: {}, 34348: {}, 34349: {},
            34361: {}, 34359: {}, 34356: {}, 34355: {},
            37336: {},
            # 装备
            25777: {}, 35065: {},
        }
    },
    1: {
        Skill: {
            100644: {}, 100816: {}, 100720: {}, 100738: {}, 100721: {}, 101862: {},
            100718: dict(damage_addition_add=358),
            **{
                skill_id: dict(pre_target_buffs={70188: {50: 1}}, post_target_buffs={70188: {50: -1}})
                for skill_id in (100620, 100623, 100624)
            }
        },
        净世破魔击: {
            100649: {}, 100650: {}
        }
    }
}
