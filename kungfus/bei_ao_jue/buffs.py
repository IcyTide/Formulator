from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            23066: {}, 19510: {}, 19244: {}, 29219: {}, 29561: {},
            11222: dict(buff_name="沧雪"),
            11221: dict(buff_name="化蛟"),
            19499: dict(buff_name="砺锋", begin_frame_shift=-2)
        }
    },
    1: {
        Buff: {
            71047: {}, 70454: dict(interval=16)
        }
    }
}
