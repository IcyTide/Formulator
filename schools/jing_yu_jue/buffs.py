from typing import Dict

from assets.setter import set_buff
from base.buff import Buff, CustomBuff
from base.recipe import DamageAdditionRecipe, PveAdditionRecipe
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        3401: {}, 3254: {}, 8210: {}, 9981: {}, 7659: {},
        17103: dict(buff_name="追命无声", gains=[DamageAdditionRecipe(205, 3096, 3096)]),
        **{buff_id: dict(frame_shift=1, gains=[PveAdditionRecipe(value, 0, 3096)])
           for buff_id, value in ((28225, 1229), (28226, 820), (28227, 615))}
    },
    CustomBuff: {-1: dict(buff_name="逐一击破", attributes=dict(all_damage_addition=103 + 103))}
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        set_buff(buff)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
