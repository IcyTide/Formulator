from typing import Dict

from base.skill import Skill

SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            13039: dict(channel_interval=24), 36065: {}, 38889: {}, 38890: {}, 38971: {}, 37448: {},
            36482: {}, 37253: {}, 34673: {}, 34674: {}, 34714: {}, 30925: {}, 30926: {}, 30857: {}, 23284: {},
            23285: {}, 23286: {}, 23287: {}, 23294: {}, 25780: {}, 19409: {}, 13075: {}, 16727: {}, 13099: {},
            13044: {}, 13092: {}, 28479: {}, 13040: {}, 38973: {},
            **{skill_id: {} for skill_id in (13106, 13107, 13108, 13110, 13160, 13161)},
            32745: dict(physical_shield_gain=[0] * 8 + [-1024]),
            13463: dict(post_target_buffs={8248: {1: 1}}),
            29188: dict(bind_dots={8249: 1}, post_target_buffs={8248: {1: -1}})
        }
    }
}
