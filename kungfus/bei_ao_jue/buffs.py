from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 奇穴
        29561: {}, 19510: {}, 11221: dict(buff_name="化蛟"), 29219: {}
    }
}
