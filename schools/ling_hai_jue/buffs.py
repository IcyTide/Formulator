from typing import Dict

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        14353: {}, 14083: {}, 13560: {}, 17094: {}, 13966: {}, 26012: {}, 14317: {},
        14321: dict(buff_name="驰行", frame_shift=-2),
        -22585: dict(buff_name="神降", activate=False)
    }
}
MOBILE_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        71252: {}
    }
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        buff.set_asset()
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
for buff_class, buffs in MOBILE_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        buff.set_asset()
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
