from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            6121: {}, 6363: {}, 14981: {}, 7671: {}, 2779: {}, 28169: {},
            21638: dict(continuous=False),
            12608: dict(buff_name="风虎", begin_frame_shift=-2, end_frame_shift=-2),
            26008: dict(buff_name="战心", begin_frame_shift=-2),
        }
    }
}
