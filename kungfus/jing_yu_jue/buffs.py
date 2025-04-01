from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        3254: {}, 8210: {}, 17103: dict(buff_name="追命无声"),
        # 奇穴
        7659: {},  **{
            buff_id: dict(buff_name=f"蹑景·{i + 1}", begin_frame_shift=2, end_frame_shift=2)
            for i, buff_id in enumerate((28225, 28226, 28227))
        },
        9981: {}, 10167: {}, 10169: dict(buff_name="空山独立"), 15945: dict(end_frame_shift=2), 22750: {},
        # 装备
        3487: {}
    }
}
