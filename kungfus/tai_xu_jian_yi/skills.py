from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    0: {
        Skill: {
            18121: dict(channel_interval=21), 589: {}, 4954: {}, 21726: {}, 21979: {}, 25771: {}, 32814: {}, 34693: {},
            34694: {}, 36272: {}, 24973: {}, 24977: {}, 38534: {}, 32780: {}, 18528: {}, 18529: {}, 14975: {},
            17689: {}, 17690: {},
            2681: dict(post_buffs={2757: {1: 1}}),
            **{skill_id: {} for skill_id in range(386, 394 + 1)},
            **{skill_id: {} for skill_id in range(6076, 6085 + 1)},
            6761: dict(consume_dots={748: 0}),
            600: dict(bind_dots={748: 1}),
            37453: dict(bind_dots={889: 1})
        }
    },
    1: {
        Skill: {
            100010: {}, 100011: {}, 101658: {}, 100374: {}, 100019: {}, 100012: {}, 100017: {}, 100003: {}, 100008: {},
            101633: {},
            101581: dict(bind_dots={70624: 1}),
            100021: dict(consume_dots={70624: 0}),
            101634: dict(consume_dots={70624: 0}),
        }
    }
}
