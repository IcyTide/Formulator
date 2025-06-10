from typing import Dict

from base.buff import Buff, CustomBuff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        1728: {},
        # 奇穴
        22913: {}, 19187: {}, 9903: {}, 12317: {}, 21640: dict(buff_name="层云"), 9714: {},
        26207: dict(stackable=False), 29360: {}
    },
    CustomBuff: {-1: dict(buff_name="重剑", attributes=dict(weapon_damage_base=0))}
}
