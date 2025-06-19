from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        2543: {}, 16543: dict(buff_name="宠物"),
        # 奇穴
        12497: {}, 25769: {}, 22232: {},
        16102: dict(buff_name="引魂", end_frame_shift=2), 16103: {},
        19513: dict(buff_name="连缘蛊增伤", begin_frame_shift=-2),
        # 装备
        16259: {}
    }
}
