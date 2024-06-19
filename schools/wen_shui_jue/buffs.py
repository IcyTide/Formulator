from typing import Dict

from assets.setter import set_buff
from base.buff import Buff, CustomBuff
from base.recipe import DamageAdditionRecipe
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        1955: {}, 1728: {}, 22913: {}, 12317: {}, 9714: {}, 26047: {},
        9903: dict(gains=[[DamageAdditionRecipe(value, skill_id, skill_id) for value in (102, 154)]
                          for skill_id in (1593, 1600)]),
        21640: dict(buff_name="层云",
                    gains=[[DamageAdditionRecipe(value, 18333, 18333) for value in (0, 102, 205, 307, 410, 512)]]),
        26207: dict(gains=[DamageAdditionRecipe(307, skill_id, skill_id) for skill_id in (1593, 1596, 1600)]),
        18008: dict(gains=[DamageAdditionRecipe(410, 18299, 0)])
    },
    CustomBuff: {-1: dict(buff_name="重剑", attributes=True)}
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        set_buff(buff)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
