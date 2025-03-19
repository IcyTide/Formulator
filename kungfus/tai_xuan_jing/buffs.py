from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    0: {
        Buff: {
            18002: {}, 18021: {}, 18174: {}, 18176: {}, 28303: {}, 28304: {}, 28305: {},
            29835: dict(buff_name="度冥")
        }
    },
    1: {
        Buff: {
            71259: {}, 71260: {}, 71232: {}
        }
    }
}
