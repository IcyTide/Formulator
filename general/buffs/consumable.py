from typing import Dict

from base.buff import Buff

GENERAL_BUFFS: Dict[int, dict] = {
    24731: {}, 24732: {}, 24735: {}, 24736: {}, 24733: {}, 24734: {}, 17365: {},
    **{gain_id: {} for gain_id in range(27784, 27792 + 1)},
    **{gain_id: {} for gain_id in range(17347, 17364 + 1)},
    18428: {}, 2563: {}, 10100: {}
}

BUFFS: Dict[int, Buff] = {}
for buff_id, attrs in GENERAL_BUFFS.items():
    buff_id = -buff_id
    buff = Buff(buff_id)
    buff.set_asset()
    for attr, value in attrs.items():
        setattr(buff, attr, value)
    BUFFS[buff_id] = buff
