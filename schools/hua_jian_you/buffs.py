from typing import Dict

from base.buff import Buff, CustomBuff
from base.recipe import DamageAdditionRecipe

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        1440: {}, 1487: {}, 11809: {}, 28116: {}, 9722: {},
        -12588: dict(buff_name="清流", activate=False),
        -14636: dict(buff_name="乱洒", gains=[DamageAdditionRecipe(307, 182, 0)]),
        -24599: dict(max_stack=4, gains=[[DamageAdditionRecipe(value, 2636, 2636) for value in (174, 348, 420, 696)]])
    },
    CustomBuff: {-1: dict(buff_name="青冠", attributes=dict(global_damage_cof=[0.25, 1.]))}
}
BUFFS: Dict[int, Buff] = {}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
