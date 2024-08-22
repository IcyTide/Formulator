from typing import Dict

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        4671: {}, 4754: {}, 6277: {}, 28886: {}, 25721: {}, 4423: {},
        -12575: dict(buff_name="用晦而明", activate=False, interval=8),
        25759: dict(buff_name="明光·日", frame_shift=1),
        25758: dict(buff_name="明光·月", frame_shift=1)
    },
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        BUFFS[buff_id] = buff = buff_class(buff_id)
        buff.set_asset(attrs)
