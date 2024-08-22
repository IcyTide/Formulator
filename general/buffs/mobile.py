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
        BUFFS[buff_id] = buff = buff_class(buff_id)
        buff.set_asset(attrs)
        buff.unique, buff.max_stack = False, 99
