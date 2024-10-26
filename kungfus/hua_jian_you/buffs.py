from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            11809: {}, 28116: {},
            1487: dict(max_stack=1),
            -9722: dict(interval=320),
            24599: dict(begin_frame_shift=-2),
            12588: dict(buff_name="清流", continuous=True),
            14636: dict(buff_name="乱洒")
        }
    }
}
