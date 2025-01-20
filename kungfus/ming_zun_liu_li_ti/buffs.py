from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            4423: {}, 28355: dict(buff_name="烈日", begin_frame_shift=-2), 12578: dict(buff_name="驱夷逐法")
        },
    }
}
