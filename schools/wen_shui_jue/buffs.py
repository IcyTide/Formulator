from typing import Dict

from base.buff import Buff, CustomBuff
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        1955: {}, 1728: {}, 22913: {}, 12317: {}, 9714: {}, 26047: {}, 9903: {}, 26207: {}, 18008: {},
        21640: dict(buff_name="层云"),
    },
    CustomBuff: {-1: dict(buff_name="重剑", attributes=dict(weapon_damage_base=0))}
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        buff.set_asset()
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
