from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        **{-buff_id: {} for buff_id in range(27784, 27792 + 1)},
        **{-buff_id: {} for buff_id in range(17347, 17364 + 1)},
        **{-buff_id: {} for buff_id in (24731, 24732, 24735, 24736, 24733, 24734, 17365, 18428, 2563, 10100)}
    }
}
