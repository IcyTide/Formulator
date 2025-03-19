from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    0: {
        Buff: {
            6121: {}, 6363: {}, 2779: {}, 18222: {},
            26008: dict(buff_name="战心", begin_frame_shift=-2),
        }
    }
}
