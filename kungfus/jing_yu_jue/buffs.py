from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            3254: {}, 8210: {}, 9981: {}, 7659: {}, 15945: {}, 10167: {},
            **{buff_id: dict(end_frame_shift=1) for buff_id in (28225, 28226, 28227)},
            10169: dict(buff_name="逐一击破"),
            3276: dict(begin_buffs={17103: {1: 1}}),
            17103: dict(buff_name="追命无声"),
        }
    }
}
