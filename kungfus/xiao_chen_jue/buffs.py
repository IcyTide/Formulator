from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        30400: dict(continuous=True),
        # 奇穴
        6377: {}, 5994: {}, 12356: dict(begin_frame_shift=-2)
    }
}
