from typing import Dict

from base.skill import Skill


class 兵主逆绝篇(Skill):
    neutral_critical_strike_rate_add = 2000
    neutral_critical_power_rate_add = 205


class 列宿游(Skill):
    damage_cof: int = 5

    def record(self, actual_critical_strike, actual_damage, parser):
        if buff_stack := parser.current_buff_stacks[71232].get(1):
            parser.refresh_target_buff(70188, self.damage_cof * buff_stack)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, self.damage_cof * buff_stack, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            25512: dict(channel_interval=16), 24454: {}, 24558: {}, 24870: {}, 25233: {}, 25174: {}, 25837: {},
            30847: {}, 32886: {}, 28815: {}, 33236: {}, 34683: {}, 37311: {}, 37599: {}, 33588: {},
            **{skill_id: {} for skill_id in range(24675, 24677 + 1)},
            **{skill_id: {} for skill_id in range(24811, 24814 + 1)},
            **{skill_id: {} for skill_id in range(24821, 24824 + 1)},
        }
    },
    1: {
        Skill: {
            101497: {}, 101466: {}, 102205: {}, 102247: {}, 102249: {}, 102238: {}, 101467: {}, 102265: {},
        },
        兵主逆绝篇: {
            101481: {}
        },
        列宿游: {
            102248: {}
        }
    }
}
