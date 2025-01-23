from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            9052: dict(buff_name="绝刀增伤", begin_frame_shift=-2),
        }
    }
}
