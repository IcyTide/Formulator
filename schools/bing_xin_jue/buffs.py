from typing import Dict

from base.recipe import DamageAdditionRecipe
from base.buff import Buff

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        1437: {}, 409: {}, 10240: {}, 538: {}, 5788: {}, 9927: {}, 17969: {},
        17010: dict(buff_name="广陵月"),
        25902: dict(gains=[DamageAdditionRecipe(512, 2707, 2707)]),
    }
}
BUFFS: Dict[int, Buff] = {}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
