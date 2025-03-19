from typing import Dict

from base.skill import Skill


class 听雷绝篇(Skill):
    damage_cof: int = 0

    def record(self, actual_critical_strike, actual_damage, parser):
        if buff_stack := parser.current_buff_stacks[70271].get(1):
            parser.refresh_target_buff(70188, buff_stack * self.damage_cof)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, buff_stack * self.damage_cof, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class Temp2(Skill):
    damage_cof: int = 0


SKILLS: Dict[type, Dict[int, dict]] = {
    0: {
        Skill: {
            1795: dict(channel_interval=32), 18383: dict(channel_interval=21), 1594: {}, 1595: {}, 1598: {}, 1706: {},
            1707: {}, 2896: {}, 13471: {}, 18299: {}, 18317: {}, 18685: {}, 18991: {}, 25776: {}, 26673: {}, 30861: {},
            32821: {}, 32967: {}, 34984: {}, 35051: {}, 38666: {},
            1658: dict(post_buffs={-1: {1: 1}}),
            1659: dict(post_buffs={-1: {1: -1}})
        }
    },
    1: {
        Skill: {
            100807: {}, 100784: {}, 100906: {}, 100844: {}, 100733: {}, 100732: {}, 100786: {}
        },
        听雷绝篇: {
            100796: dict(damage_cof=15),
            100728: dict(damage_cof=5)
        }
    }
}
