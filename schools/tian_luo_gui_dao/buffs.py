from typing import Dict

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        3401: {}, 3254: {}, 3316: {}, 6105: {}, 8210: {}, 9981: {}, 27457: {}, 16234: {}, 16235: {}, 16236: {},
        6112: {}, 28228: {}, 3426: {},
        10005: dict(stackable=False),
        13165: dict(buff_name="雷甲三铉"),
        27405: dict(buff_name="雷甲三铉"),
        23081: dict(buff_name="擘两分星"),
        23082: dict(buff_name="擘两分星"),
        -24668: dict(buff_name="杀机断魂", activate=False, max_stack=20)
    }
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        BUFFS[buff_id] = buff = buff_class(buff_id)
        buff.set_asset(attrs)
