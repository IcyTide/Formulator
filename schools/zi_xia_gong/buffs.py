from typing import Dict

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        1439: {}, 375: {}, 1908: {}, 2757: {},
        **{buff_id: {} for buff_id in range(12779, 12783 + 1)},
        9966: dict(buff_name="同尘"),
        17918: dict(activate=False),
        -12550: dict(buff_name="跬步", activate=False, interval=4),
        -12551: dict(buff_name="跬步", activate=False, interval=4)
    }
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        BUFFS[buff_id] = buff = buff_class(buff_id)
        buff.set_asset(attrs)
