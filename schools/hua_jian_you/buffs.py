from typing import Dict

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        1440: {}, 1487: {}, 11809: {}, 28116: {}, 9722: {}, -24599: {},
        14636: dict(buff_name="乱洒"),
        -12588: dict(buff_name="清流", activate=False),
    }
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        BUFFS[buff_id] = buff = buff_class(buff_id)
        buff.set_asset(attrs)
