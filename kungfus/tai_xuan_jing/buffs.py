from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            18002: {}, 18021: {}, 18174: {}, 18176: {}, 28303: {}, 28304: {}, 28305: {}
        }
    },
    1: {
        Buff: {
            71259: {}, 71260: {}
        }
    }
}
