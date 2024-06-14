from typing import Dict

from base.buff import Buff
from base.recipe import DamageAdditionRecipe

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        11378: {}, 18384: {}, 14972: {},
        23066: dict(gains=[[DamageAdditionRecipe(value, skill_id, skill_id) for value in (51, 102)]
                           for skill_id in (16085, 16027, 16621)])
    }
}
BUFFS: Dict[int, Buff] = {}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
