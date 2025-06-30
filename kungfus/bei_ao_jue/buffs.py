from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 奇穴
        29561: {}, 19499: dict(buff_name="砺锋", begin_frame_shift=-2), 19510: dict(begin_frame_shift=-2),
        11221: dict(buff_name="化蛟"), 29219: {},
        # 装备
        15291: {}
    }
}
