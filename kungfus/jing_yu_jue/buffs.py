from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            3254: {}, 8210: {}, 9981: {}, 7659: {}, 10167: {}, 22750: {}, 3487: {},
            15945: dict(end_frame_shift=1),
            **{
                buff_id: dict(buff_name=f"蹑景·{i + 1}", end_frame_shift=1)
                for i, buff_id in enumerate((28225, 28226, 28227))
            },
            10169: dict(buff_name="逐一击破"),
            3276: dict(begin_buffs={17103: {1: 1}}),
            17103: dict(buff_name="追命无声"),
        }
    }
}
