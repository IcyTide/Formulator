from typing import Dict

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        11378: {}, 24553: {}, 24209: {}, 24557: {},
        24179: dict(buff_name="雨积"),
        24180: dict(buff_name="镇机")
    }
}
MOBILE_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        71297: {}
    }
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        BUFFS[buff_id] = buff = buff_class(buff_id)
        buff.set_asset(attrs)
for buff_class, buffs in MOBILE_BUFFS.items():
    for buff_id, attrs in buffs.items():
        BUFFS[buff_id] = buff = buff_class(buff_id)
        buff.set_asset(attrs)
