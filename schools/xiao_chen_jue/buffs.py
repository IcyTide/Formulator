from typing import Dict

from assets.setter import set_buff
from base.buff import Buff
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        1438: {}, 5994: {}, 6385: {}, 6398: {}, 25904: {}, 6377: {}, 12356: {}, 9719: {}, 10221: {}
    }
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        set_buff(buff)
        BUFFS[buff_id] = buff
