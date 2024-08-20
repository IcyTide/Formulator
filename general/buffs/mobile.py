from typing import Dict

from base.buff import Buff

GENERAL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        70161: {}, 70167: {}, 70162: {}, 70163: {}, 70345: {}, 70188: {}
    }
}

BUFFS: Dict[int, Buff] = {}
for buff_class, buffs in GENERAL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        buff.set_asset()
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        buff.unique = False
        buff.max_stack = 99
        BUFFS[buff_id] = buff
