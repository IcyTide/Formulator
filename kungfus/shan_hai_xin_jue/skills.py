from typing import Dict

from base.skill import Skill, NpcSkill


class 射日加成(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_target_buff_stacks.get((71182, 1)):
            parser.refresh_target_buff(70188, 20)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 20, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 白泽加成(NpcSkill):
    pass


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            35894: dict(channel_interval=24), 35866: {}, 35987: {}, 36157: {}, 36177: {}, 36453: {}, 36579: {},
            36580: {},
            35771: dict(bind_dots={26856: 1}),
            36165: dict(consume_dots={26856: 3}),
            35695: dict(pet_buffs={26857: {1: 1}}),
            35696: dict(pet_count=3, pet_buffs={26857: {1: 1}})
        },
        NpcSkill: {
            36056: {}, 36057: {}, 36111: {}, 36112: {}, 36113: {}, 36114: {},
        }
    },
    1: {
        射日加成: {
            102019: {}, 102018: {}, 102037: {}, 102027: {}, 101998: {}, 102035: {},
            102211: dict(bind_dots={71175: 1}),
        },
        白泽加成: {
            102028: {}, 102029: {}, 102030: {}, 102031: {}, 102032: {}, 102033: {},
        }
    }
}
