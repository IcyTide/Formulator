from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 奇穴
        29254: {}, 29243: dict(buff_name="玉枕")
    }
}
