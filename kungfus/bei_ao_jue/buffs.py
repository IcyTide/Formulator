from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            # 奇穴
            29561: {}, 19510: {}, 11221: dict(buff_name="化蛟"), 29219: {}
        }
    },
    1: {
        Buff: {
            71047: {}, 70454: dict(interval=16)
        }
    }
}
