from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        9433: {},
        # 奇穴
        9495: {}, 30464: {}, 9437: {}, 23101: dict(buff_name="刻梦"), 12576: dict(buff_name="云汉"),
        25997: dict(begin_frame_shift=-2),
    }
}
