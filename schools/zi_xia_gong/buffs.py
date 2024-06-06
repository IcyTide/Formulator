from typing import Dict

from base.buff import Buff
from base.recipe import DamageAdditionRecipe, PveAdditionRecipe

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        1439: {}, 375: {}, 1908: {},
        **{buff_id: {} for buff_id in range(12779, 12783)},
        2757: dict(frame_shift=-2),
        9966: dict(buff_name="同尘",
                   gains=[[DamageAdditionRecipe(value, 368, 368) for value in (359, 717, 1076, 1434)]]),
        17918: dict(gains=[PveAdditionRecipe(1331, 18640, 18640)])
    },
    # 12550: {
    #     "buff_name": "跬步",
    #     "gains": {
    #         896: {
    #             "skill_damage_addition": [40, 81, 122, 163, 204]
    #         }
    #     }
    # },
    # 12551: {
    #     "buff_name": "跬步",
    #     "gains": {
    #         skill_id: {
    #             "skill_damage_addition": [40, 81, 122, 163, 204]
    #         } for skill_id in (3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448)
    #     }
    # },
}
BUFFS: Dict[int, Buff] = {}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
