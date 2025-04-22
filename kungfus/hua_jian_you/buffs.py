from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        1487: dict(stackable=False),
        # 奇穴
        11809: dict(end_frame_shift=2), 28116: {}, 12588: dict(buff_name="清流", continuous=True),
        -9722: dict(interval=320),
    }
}
