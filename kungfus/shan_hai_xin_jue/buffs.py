from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            26857: {}, -27099: {},
            27406: dict(buff_name="朱厌")
        }
    },
    1: {
        Buff: {
            71172: {},
            71182: dict(interval=96)
        }
    }
}
