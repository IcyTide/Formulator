from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            375: {}, 1908: {}, 2757: {}, 6103: {},
            **{buff_id: {} for buff_id in range(12779, 12783 + 1)},
            29183: dict(buff_name="霜锋"),
            9966: dict(buff_name="同尘"),
            17918: dict(activate=False),
            -12550: dict(buff_name="跬步", activate=False, interval=4),
            -12551: dict(buff_name="跬步", activate=False, interval=4)
        }
    }
}
