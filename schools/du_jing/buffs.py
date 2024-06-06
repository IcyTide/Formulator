from typing import Dict

from base.buff import Buff
from base.recipe import DamageAdditionRecipe

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        2557: {}, 2543: {}, 12497: {}, 22232: {}, 16103: {},
        16543: dict(buff_name="宠物"),
        17988: dict(buff_name="曲致"),
        16102: dict(buff_name="引魂", attribute=dict(surplus_gain=410)),
        25769: dict(gains=[DamageAdditionRecipe(154, skill_id, 0) for skill_id in (29573, 25044, 30918, 18590)]),
        19513: dict(gains=[[DamageAdditionRecipe(value, 25044, 0) for value in (819, 1638, 2458, 3277)]])
    }
}
BUFFS: Dict[int, Buff] = {}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
