from typing import Dict

from base.buff import Buff
from base.recipe import ChannelIntervalRecipe, DamageAdditionRecipe

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        3401: {}, 3254: {}, 3316: {}, 6105: {}, 8210: {}, 9981: {}, 10005: {}, 27457: {},
        16234: {}, 16235: {}, 16236: {},
        23081: dict(buff_name="擘两分星"),
        23082: dict(buff_name="擘两分星",
                    gains=[ChannelIntervalRecipe(1.1, skill_id, skill_id) for skill_id in (3108, 3111)] +
                          [DamageAdditionRecipe(103, 25154, 25154)]),
        -24668: dict(buff_name="杀机断魂", activate=False, max_stack=20)
    }
}
BUFFS: Dict[int, Buff] = {}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
