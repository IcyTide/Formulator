from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            18384: {}, 23066: {}, 14972: {}
        }
    },
    1: {
        Buff: {
            71047: {}, 70454: dict(interval=16)
        }
    }
}
