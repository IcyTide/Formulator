from typing import Dict, Union

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS: Dict[int, Union[Buff, dict]] = {
    21758: {
        "buff_name": "断肠",
        "activate": False,
        "gain_attributes": {
            "magical_critical_strike_gain": 400,
            "magical_critical_power_gain": 41
        }
    },
    20680: {
        "buff_name": "相使",
        "gain_attributes": {
            "magical_attack_power_gain": 154,
        }
    },
    # 21607: {
    #     "buff_name": "灵荆",
    # },
    21168: {
        "buff_name": "植物温性",
        "gain_skills": {
            27657: {
                "skill_damage_addition": [51, 717, 0],
            }
        }
    },
    20696: {
        "buff_name": "凄骨",
        "gain_attributes": {
            "all_shield_ignore": 512
        }
    },
    24659: {
        "buff_name": "应理以药",
        "frame_shift": -2,
        "gain_skills": {
            28081: {
                "skill_damage_addition": 3277,
            }
        }
    }
}

for buff_id, detail in BUFFS.items():
    BUFFS[buff_id] = Buff(buff_id)
    for attr, value in detail.items():
        setattr(BUFFS[buff_id], attr, value)

for buff_id, buff in GENERAL_BUFFS.items():
    if buff_id not in BUFFS:
        BUFFS[buff_id] = buff
