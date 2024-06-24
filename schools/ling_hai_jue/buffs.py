from typing import Dict

from assets.setter import set_buff
from base.buff import Buff, CustomBuff
from base.recipe import DamageAdditionRecipe, PhysicalCriticalRecipe
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        14353: {}, 14083: {}, 13560: {}, 17094: {}, 13966: {}, 26012: {},
        14321: dict(buff_name="驰行", frame_shift=-2,
                    gains=[DamageAdditionRecipe(307, skill_id, skill_id) for skill_id in (20715, 20083, 20084)]),
        14317: dict(gains=[[PhysicalCriticalRecipe(value, 20053, 20053)
                            for value in ((1000, 102), (2000, 205), (3000, 307), (4000, 410), (5000, 512))]]),
    },
    CustomBuff: {14029: dict(buff_name="神降", activate=False, attributes=dict(all_damage_addition=102))}
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        set_buff(buff)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
