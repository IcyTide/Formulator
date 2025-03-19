from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        2543: {}, 16543: dict(buff_name="宠物"),
        # 奇穴
        12497: {}, 22232: {}
    }
}
