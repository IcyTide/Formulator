from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        **{-buff_id: {} for buff_id in range(27784, 27792 + 1)},
        **{-buff_id: {} for buff_id in range(17347, 17364 + 1)},
        **{-buff_id: {} for buff_id in (29274, 29276, 29284, 29285, 29288, 29289, 17365, 18428, 2563, 10100)}
    }
}
