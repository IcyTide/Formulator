from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            8244: {}, 8385: {}, 27161: {}, 8474: {}, 17176: {}, 14309: {}, 16957: {}, 8451: {},
            8248: dict(interval=400),
            25937: dict(buff_name="祭血关山"),
            8627: dict(buff_name="刀魂"),
            26212: dict(begin_target_buffs={8248: {1: 1}}),
            9052: dict(buff_name="绝刀增伤", begin_frame_shift=-2),
        }
    }
}
