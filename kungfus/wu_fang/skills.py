from typing import Dict

from base.skill import Skill


class 钩吻断肠秘章(Skill):
    damage_addition_add = 154

    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[70529].get(1):
            parser.refresh_target_buff(70188, 15)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 15, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 苍棘缚地(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[71230].get(1):
            parser.refresh_target_buff(70188, 10)
        if parser.current_buff_stacks[71258].get(1):
            parser.refresh_target_buff(70188, 10)
        super().record(actual_critical_strike, actual_damage, parser)
        if parser.current_buff_stacks[71230].get(1):
            parser.refresh_target_buff(70188, 10, -1)
        if parser.current_buff_stacks[71258].get(1):
            parser.refresh_target_buff(70188, 10, -1)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            27451: dict(channel_interval=16), 32841: {}, 28081: {}, 27552: {}, 27555: {}, 27557: {}, 27579: {},
            27584: {}, 28409: {}, 28346: {}, 34699: {}, 27539: {}, 32922: {}, 27657: {}, 29674: {}, 28385: {},
            28434: {}, 29698: {}, 29695: {}, 36068: {}, 38636: {},
            35367: dict(post_buffs={24659: {1: 1}}),
            **{skill_id: dict(consume_dots={20052: 2}) for skill_id in (29505, 29506, 34700, 34702, 30735)},
            27560: dict(bind_dots={20052: 1})
        }
    },
    1: {
        Skill: {
            102159: {}, 102157: {}, 102158: {}, 102164: {}, 101365: {},
            101417: dict(bind_dots={71171: 1}),
            102163: dict(consume_dots={71171: 0}),
        },
        钩吻断肠秘章: {
            101357: {}, 101358: {},
        },
        苍棘缚地: {
            101425: {}
        }
    }
}
