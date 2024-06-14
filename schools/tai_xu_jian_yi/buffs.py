from typing import Dict

from base.buff import Buff
from base.recipe import DamageAdditionRecipe

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        1438: {}, 378: {}, 17933: {}, 9949: {},
        2757: dict(frame_shift=-2),
        14931: dict(gains=[DamageAdditionRecipe(307, 365, 365)])
    }
}
BUFFS: Dict[int, Buff] = {}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
