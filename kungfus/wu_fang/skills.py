from typing import Dict

from base.skill import Skill


class 鬼门加成(Skill):
    talent_activate = False

    def record(self, actual_critical_strike, actual_damage, parser):
        if self.talent_activate and parser.current_dot_ticks.get(71171):
            parser.refresh_target_buff(70188, 10)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 10, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 钩吻断肠秘章(鬼门加成):
    damage_addition_add = 154

    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[70529].get(1):
            parser.refresh_target_buff(70188, 15)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 15, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 苍棘缚地(鬼门加成):
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
            27584: {},
            28409: {}, 28346: {}, 34699: {}, 27539: {}, 32922: {}, 27657: {}, 29674: {}, 28385: {}, 28434: {},
            36508: {},
            29698: {}, 29695: {}, 36068: {},
            35367: dict(post_buffs={24659: {1: 1}}),
            **{
                skill_id: dict(consume_dot=20052, consume_tick=2) for skill_id in (29505, 29506, 34700, 34702, 30735)
            },
            27560: dict(bind_dot=20052)
        }
    },
    1: {
        鬼门加成: {
            102159: {}, 102157: {}, 102158: {}, 102164: {},
            101417: dict(bind_dot=71171),
            102163: dict(consume_dot=71171),
        },
        钩吻断肠秘章: {
            101357: {}, 101358: {},
        },
        苍棘缚地: {
            101425: {}
        }
    }
}
