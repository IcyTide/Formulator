from typing import Dict

from base.skill import Skill

SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            15: dict(channel_interval=21), 2716: {}, 6234: {}, 6554: {}, 23936: {}, 24999: {}, 25769: {}, 30524: {},
            30532: {}, 32889: {}, 6559: {}, 32957: {}, 34611: {}, 34612: {}, 34642: {}, 34704: {}, 35058: {}, 37317: {},
            37318: {}, 37319: {}, 37320: {}, 506: {}, 36554: {},
            **{skill_id: dict(bind_dot=2920) for skill_id in (6207, 18716)},
            25757: dict(bind_dot=18512),
            3889: dict(consume_dot=2920)
        }
    },
    1: {
        Skill: {
            100388: {}, 101635: {}, 101655: {}, 101649: {}, 101610: {}, 101612: {}, 101609: {}, 100444: {}, 100564: {},
            100414: {}, 100418: {},
            100402: dict(bind_dot=70030),
            101553: dict(consume_dot=70030, consume_tick=1),
            101607: dict(consume_dot=70030)
        }
    }
}
