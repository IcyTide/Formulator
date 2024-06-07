from typing import Dict

from base.buff import Buff
from base.recipe import DamageAdditionRecipe

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        16025: {}, 15893: {}, 15932: {},
        16596: dict(buff_name="崔嵬鬼步"),
        **{
            buff_id: dict(buff_name="百节", frame_shift=-2,
                          gains=[DamageAdditionRecipe(value, skill_id, skill_id)
                                 for skill_id in (22327, 22320, 22321, 22358)])
            for buff_id, value in ((15927, 102), (15928, 205), (15929, 307))
        },
        15832: dict(buff_name="星旗", gains=[[DamageAdditionRecipe(value, 22143, 22143) for value in (154, 307)]])
    }
}
BUFFS: Dict[int, Buff] = {}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
