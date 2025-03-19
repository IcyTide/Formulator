from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    0: {
        Buff: {
            8244: {}, 8385: {}, 27161: {}, 17176: {}, 14309: {}, 16957: {}, 8451: {}, 8474: {}, 8423: {},
            25937: dict(buff_name="祭血关山"),
            8627: dict(buff_name="刀魂"),
            9052: dict(buff_name="绝刀增伤", begin_frame_shift=-2),
        }
    },
    1: {
        Buff: {
            70382: {}, 71320: {}, 71321: {}, 71095: {},
        }
    }
}
