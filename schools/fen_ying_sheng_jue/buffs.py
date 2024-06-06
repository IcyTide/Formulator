from typing import Dict

from base.buff import Buff
from base.recipe import MagicalAttackPowerRecipe, MagicalCriticalRecipe


SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        4671: {}, 4754: {}, 6277: {}, 12575: {},
        25758: dict(gains=[MagicalAttackPowerRecipe(246, skill_id, skill_recipe)
                           for skill_id, skill_recipe in ((0, 3966), (0, 3967), (34348, 0))]),
        25759: dict(gains=[MagicalCriticalRecipe(246, skill_id, skill_recipe)
                           for skill_id, skill_recipe in ((0, 3966), (4476, 0), (34349, 0))])
    },
}
BUFFS: Dict[int, Buff] = {}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
