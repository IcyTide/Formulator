from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        378: {}, 2757: {}, 29204: {},
        # 奇穴
        6093: dict(end_frame_shift=2),
        29451: dict(max_stack=4, interval=80), -29451: dict(attributes=dict(all_damage_cof=0.5 * 1024), max_stack=4),
        # 装备
        1915: {}
    }
}
