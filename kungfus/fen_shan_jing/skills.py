from typing import Dict

from base.skill import Skill


class 劫刀(Skill):
    damage_cof: int = 5

    def record(self, actual_critical_strike, actual_damage, parser):
        if buff_stack := parser.current_dot_stacks[70402]:
            parser.refresh_target_buff(70188, self.damage_cof * buff_stack)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, self.damage_cof * buff_stack, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 盾刀(Skill):
    damage_cof: int = 20

    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_dot_stacks[70402]:
            parser.refresh_target_buff(70188, self.damage_cof)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, self.damage_cof, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


SKILLS: Dict[type, Dict[int, dict]] = {
    0: {
        Skill: {
            13039: dict(channel_interval=24), 36065: {}, 38889: {}, 38890: {}, 38971: {}, 37448: {}, 13463: {},
            36482: {}, 37253: {}, 34673: {}, 34674: {}, 34714: {}, 30925: {}, 30926: {}, 30857: {}, 23284: {},
            23285: {}, 23286: {}, 23287: {}, 23294: {}, 25780: {}, 19409: {}, 16727: {}, 13099: {}, 13044: {},
            38973: {}, 38651: {}, 33097: {}, 13453: {},
            **{skill_id: {} for skill_id in list(range(13076, 13085 + 1)) + [13075]},
            **{skill_id: {} for skill_id in list(range(18355, 18364 + 1)) + [13092]},
            **{skill_id: {} for skill_id in list(range(28468, 28477 + 1)) + [28479]},
            **{skill_id: {} for skill_id in (13106, 13107, 13108, 13110, 13160, 13161)},
            32745: dict(physical_shield_gain=[0] * 8 + [-1024]),
            **{
                skill_id: dict(bind_dots={8249: 1})
                for skill_id in (29187, 29188, 37568, 37569, 37600, 37601)
            },
        }
    },
    1: {
        Skill: {
            101040: {}, 102212: {}, 101089: {}, 101317: {},
            102040: dict(pre_buffs={70382: {1: 1}}),
            101171: dict(bind_dots={70402: 1}),
            **{skill_id: dict(damage_cof_add=512 / 2) for skill_id in (101041, 101174)},
            **{skill_id: dict(damage_addition_add=358) for skill_id in (101189, 101271)},
            **{skill_id: dict(damage_addition_add=307) for skill_id in (101194, 101042)}
        },
        劫刀: {
            101038: {}
        },
        盾刀: {
            101029: {}, 101065: {}, 101066: {}
        }
    }
}
