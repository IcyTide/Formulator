from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        6121: {}, 6363: {},
        # 奇穴
        244: {}, 26444: {}, -21638: dict(attributes=dict(all_damage_cof=0.3 * 1024)), 7671: {},
        12608: dict(buff_name="风虎", begin_frame_shift=-2), 26008: dict(buff_name="战心", begin_frame_shift=-2),
        2779: {}
    }
}
