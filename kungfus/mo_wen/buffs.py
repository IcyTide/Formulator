from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            9437: {}, 25997: {}, 9433: {}, 9495: {},
            -23167: dict(buff_name="流照", interval=96),
            23101: dict(buff_name="刻梦"),
            12576: dict(buff_name="云汉"),
        }
    }
}
