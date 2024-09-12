from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            2543: {}, 12497: {}, 22232: {}, 16103: {}, 25769: {},
            16543: dict(buff_name="宠物"),
            -17988: dict(buff_name="曲致", activate=False),
            16102: dict(buff_name="引魂", attribute=dict(magical_attack_power_gain=410, surplus_gain=410)),
            -19513: dict(buff_name="连缘蛊增伤", interval=32)
        }
    }
}
