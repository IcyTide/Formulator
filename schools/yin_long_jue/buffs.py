from typing import Dict

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        16025: {}, 15893: {}, 15932: {}, 15926: {}, 15927: {}, 15928: {}, 15929: {},
        16596: dict(buff_name="崔嵬鬼步"),
        15832: dict(buff_name="星旗"),
        21588: dict(buff_name="孤路")
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
