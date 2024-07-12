from typing import Dict

from assets.setter import set_buff
from base.buff import Buff

GENERAL_GAINS: Dict[int, dict] = {
    **{gain_id: {} for gain_id in range(24731, 24736 + 1)},
    **{gain_id: {} for gain_id in range(17347, 17365 + 1)},
    **{gain_id: {} for gain_id in range(27784, 27792 + 1)},
    18428: {}, 2563: {}, 10100: {}
}

GAINS: Dict[int, Buff] = {}
for buff_id, attrs in GENERAL_GAINS.items():
    buff = Buff(buff_id)
    buff.activate = False
    set_buff(buff)
    for attr, value in attrs.items():
        setattr(buff, attr, value)
    GAINS[buff_id] = buff
