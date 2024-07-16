from typing import Dict

from assets.setter import set_buff
from base.buff import Buff
from base.recipe import MagicalShieldGainRecipe, DamageAdditionRecipe, ChannelIntervalRecipe
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        9586: {}, 9437: {}, 25997: {},
        23101: dict(buff_name="刻梦"),
        12576: dict(buff_name="云汉"),
        9433: dict(gains=[[MagicalShieldGainRecipe(value, skill_id, 0) for value in (-307, -614, -921)]
                          for skill_id in (14474, 14227)]),
        9495: dict(gains=[DamageAdditionRecipe(205, 0, skill_id) for skill_id in (14064, 14067, 14068)] +
                         [ChannelIntervalRecipe(1.2, 0, skill_id) for skill_id in (14065, 14066)]),
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
