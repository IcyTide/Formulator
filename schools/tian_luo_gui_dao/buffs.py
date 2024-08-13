from typing import Dict

from base.buff import Buff
from base.recipe import ChannelIntervalRecipe, DamageAdditionRecipe, MagicalShieldGainRecipe
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        3401: {}, 3254: {}, 3316: {}, 6105: {}, 8210: {}, 9981: {}, 27457: {}, 16234: {}, 16235: {}, 16236: {},
        6112: {},
        # 3426: dict(gains=[DamageAdditionRecipe(512, skill_id) for skill_id in (21854, 21850)]), # not work
        10005: dict(stackable=False),
        28228: dict(gains=[DamageAdditionRecipe(-460, 0, 3367)]),
        13165: dict(buff_name="雷甲三铉", gains=[MagicalShieldGainRecipe(-512, 0, 3367)]),
        27405: dict(buff_name="雷甲三铉", gains=[ChannelIntervalRecipe(1.75, 3367, 3367)]),
        23081: dict(buff_name="擘两分星"),
        23082: dict(buff_name="擘两分星",
                    gains=[ChannelIntervalRecipe(1.1, skill_id, skill_id) for skill_id in (3108, 3111)] +
                          [DamageAdditionRecipe(103, 25154, 25154)]),
        -24668: dict(buff_name="杀机断魂", activate=False, max_stack=20)
    }
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        buff.set_asset()
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
