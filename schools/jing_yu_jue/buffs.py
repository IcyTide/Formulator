from typing import Dict

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        3401: {}, 3254: {}, 8210: {}, 9981: {}, 7659: {}, 3276: {}, -28225: {}, -28226: {}, -28227: {},
        17103: dict(buff_name="追命无声"),
        **{buff_id: dict(buff_name="逐一击破") for buff_id in (-23074, -10169)},
    }
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        BUFFS[buff_id] = buff = buff_class(buff_id)
        buff.set_asset(attrs)
