from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            14083: {}, 13560: {}, 17094: {}, 13966: {}, 26012: {}, 14317: {},
            14321: dict(buff_name="驰行", frame_shift=-2),
            -22585: dict(buff_name="神降", activate=False)
        }
    },
    1: {
        Buff: {
            71252: {}
        }
    }
}
