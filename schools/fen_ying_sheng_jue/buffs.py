from typing import Dict

from assets.setter import set_buff
from base.buff import Buff
from base.recipe import MagicalAttackPowerRecipe, MagicalCriticalRecipe
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        4671: {}, 4754: {}, 6277: {},
        12575: dict(buff_name="用晦而明"),
        25758: dict(buff_name="明光·月",
                    gains=[MagicalAttackPowerRecipe(246, skill_id, skill_recipe)
                           for skill_id, skill_recipe in ((0, 3966), (0, 3967), (34348, 0))]),
        25759: dict(buff_name="明光·日",
                    gains=[MagicalCriticalRecipe((1500, 102), skill_id, skill_recipe)
                           for skill_id, skill_recipe in ((0, 3966), (4476, 0), (34349, 0))])
    },
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        set_buff(buff)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
