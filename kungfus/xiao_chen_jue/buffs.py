from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    0: {
        Buff: {
            5994: {}, 6385: {}, 25904: {}, 6377: {}, 9719: {},
            10221: dict(end_frame_shift=-2),
            12356: dict(begin_frame_shift=-2),
            6398: dict(begin_frame_shift=-2),
        }
    },
    1: {
        Buff: {
            70221: {}, 70889: {}
        }
    }
}
