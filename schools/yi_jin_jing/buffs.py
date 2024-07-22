from typing import Dict

from assets.setter import set_buff
from base.buff import Buff, TargetBuff
from base.recipe import PveAdditionRecipe, DamageAdditionRecipe
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        1436: {}, 11979: {}, 2686: {}, 10023: {}, 24285: {}, 24453: {}, 24288: {}, 21859: {},
        890: dict(max_stack=2, interval=352),
        12479: dict(max_stack=3, interval=352),
        -13910: dict(buff_name="众嗔", interval=4),
        12590: dict(buff_name="三生"),
        28296: dict(gains=[PveAdditionRecipe(820, skill_id, skill_recipe)
                           for skill_id, skill_recipe in ((232, 232), (233, 233), (235, 235), (236, 0))]),
        1919: dict(gains=[DamageAdditionRecipe(922, 233, 233)])
    },
    TargetBuff: {19635: dict(buff_name="普渡", interval=4)},
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        set_buff(buff)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
