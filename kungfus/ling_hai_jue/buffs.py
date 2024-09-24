from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            14083: {}, 13560: {}, 13966: {}, 26012: {}, 14317: {}, 29344: {},
            **{buff_id: dict(buff_name="澄穆") for buff_id in (19253, 19254, 19255)},
            29348: dict(buff_name="鸿轨"),
            14321: dict(buff_name="驰行"),
            -22585: dict(buff_name="神降", activate=False)
        }
    },
    1: {
        Buff: {
            71252: {}
        }
    }
}
