from typing import Dict

from base.buff import Buff, CustomBuff
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        1428: {}, 6121: {}, 6363: {}, 14981: {}, 7671: {}, 21638: {}, 2779: {}, 28169: {},
        -12608: dict(buff_name="风虎", activate=False, interval=4),
        -26008: dict(buff_name="战心", interval=4),
        1911: dict(begin_buffs={-1: {1: 5}}),
    },
    CustomBuff: {
        -1: dict(buff_name="战意", max_stack=5),
    }
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        BUFFS[buff_id] = buff = buff_class(buff_id)
        buff.set_asset(attrs)
