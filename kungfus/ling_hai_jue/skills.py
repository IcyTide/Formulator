from typing import Dict

from base.skill import Skill


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            19712: dict(channel_interval=24), 19766: {}, 19767: {}, 20014: {}, 19819: {}, 20016: {}, 20052: {},
            20054: {}, 30503: {}, 20322: {}, 20323: {}, 20684: {}, 20685: {}, 20734: {}, 25783: {}, 31250: {},
            32478: {}, 32815: {}, 36282: {}, 32595: {},
            38675: dict(bind_dots={29350: 1}),
            26935: dict(bind_dots={19557: 1})
        }
    },
    1: {
        Skill: {
            102091: {}, 102092: {}, 102093: {},
            102134: {}, 102173: {}, 102145: {}, 102111: {}, 102161: {}, 102103: {},
            102228: dict(pre_target_buffs={70188: {40: 1}}, post_target_buffs={70188: {40: -1}}),
            102104: dict(pre_target_buffs={70188: {80: 1}}, post_target_buffs={70188: {80: -1}})
        }
    }
}
