from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        8244: {}, 9052: dict(buff_name="绝刀增伤", begin_frame_shift=-2),
        # 奇穴
        8385: {}, 17176: {}, 14309: {}, 27161: {},
        # 装备
        8474: {}
    }
}
