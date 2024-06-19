from typing import Dict

from assets.setter import set_buff
from base.buff import Buff
from base.recipe import DamageAdditionRecipe, PveAdditionRecipe
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        1439: {}, 375: {}, 1908: {},
        **{buff_id: {} for buff_id in range(12779, 12783 + 1)},
        2757: dict(frame_shift=-2),
        9966: dict(buff_name="同尘",
                   gains=[[DamageAdditionRecipe(value, 368, 368) for value in (359, 717, 1076, 1434)]]),
        17918: dict(gains=[PveAdditionRecipe(1331, 18640, 18640)]),
        -12550: dict(buff_name="跬步", activate=False, interval=4,
                     gains=[[DamageAdditionRecipe(value, 367, 367) for value in (41, 82, 123, 164, 205)]]),
        -12551: dict(buff_name="跬步", activate=False, interval=4,
                     gains=[[DamageAdditionRecipe(value, 301, 301) for value in (41, 82, 123, 164, 205)]])
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
