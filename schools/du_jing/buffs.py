from typing import Dict

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        2557: {}, 2543: {}, 12497: {}, 22232: {}, 16103: {}, 25769: {},
        16543: dict(buff_name="宠物"),
        -17988: dict(buff_name="曲致", activate=False),
        16102: dict(buff_name="引魂", attribute=dict(magical_attack_power_gain=410, surplus_gain=410)),
        -19513: dict(buff_name="连缘蛊增伤", interval=32)
    }
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        BUFFS[buff_id] = buff = buff_class(buff_id)
        buff.set_asset(attrs)
