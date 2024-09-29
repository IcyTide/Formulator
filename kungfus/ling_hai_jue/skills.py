from typing import Dict

from base.skill import Skill


class 击水加成(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        parser.refresh_target_buff(70188, 30)
        super().record(actual_critical_strike, actual_damage, parser)
        parser.refresh_target_buff(70188, 30, -1)


class 逐波加成(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        parser.refresh_target_buff(70188, 80)
        super().record(actual_critical_strike, actual_damage, parser)
        parser.refresh_target_buff(70188, 80, -1)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            19712: dict(channel_interval=24), 19766: {}, 19767: {}, 20014: {}, 19819: {}, 20016: {}, 20052: {},
            20054: {}, 30503: {}, 20322: {}, 20323: {}, 20684: {}, 20685: {}, 20734: {}, 25783: {}, 31250: {},
            32478: {}, 32815: {}, 36282: {}, 32595: {},
            38675: dict(bind_dot=29350),
            26935: dict(bind_dot=19557)
        }
    },
    1: {
        Skill: {
            102134: {}, 102173: {}, 102145: {}, 102111: {}, 102161: {}, 102228: {}, 102103: {}
        },
        击水加成: {
            102091: {}, 102092: {}, 102093: {}
        },
        逐波加成: {
            102104: {}
        }
    }
}
