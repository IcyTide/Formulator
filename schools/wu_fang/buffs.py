from typing import Dict

from assets.setter import set_buff
from base.buff import Buff
from base.recipe import DamageAdditionRecipe
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        21758: {}, 20680: {}, 20696: {},
        20718: dict(buff_name="炮阳", gains=[DamageAdditionRecipe(358, 28081, 28081)]),
        21168: dict(buff_name="植物温性",
                    gains=[[DamageAdditionRecipe(value, 27652, 27652) for value in (51, 717, 0)]]),
        21856: dict(buff_name="荆障", gains=[DamageAdditionRecipe(154, 27652, 27652)]),
        20699: dict(buff_name="养荣"),
        24659: dict(buff_name="应理与药", gains=[DamageAdditionRecipe(3277, 28081, 28081)])
    },
}
MOBILE_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        71230: {}, 71258: {}
    }
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        set_buff(buff)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
for buff_class, buffs in MOBILE_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        set_buff(buff)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
