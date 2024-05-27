from typing import Dict, Union

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS: Dict[int, Union[Buff, dict]] = {
    2557: {
        "buff_name": "蛊殇",
        "activate": False,
        "gain_attributes": {
            "magical_critical_strike_rate": 400,
            "magical_critical_power_rate": 41
        }
    },
    2543: {
        "buff_name": "灵蛇献祭",
        "gain_attributes": {
            "magical_attack_power_gain": 512
        }
    },
    12497: {
        "buff_name": "虫兽",
        "gain_attributes": {
            "magical_attack_power_gain": 154
        }
    },
    # 25769: {
    #     "buff_name": "重蛊",
    #     "gain_skills": {
    #         skill_id: {
    #             "skill_damage_addition": 154
    #         } for skill_id in (29573, 25044, 30918)
    #     }
    # },
    22232: {
        "buff_name": "嗜蛊",
        "gain_attributes": {
            "all_shield_ignore": 820
        }
    },
    16103: {
        "buff_name": "引魂",
        "gain_attributes": {
            "all_damage_addition": 102
        }
    },
    19513: {
        "buff_name": "连缘蛊",
        "frame_shift": 1,
        "gain_skills": {
            25044: {
                "skill_damage_addition": [819, 1638, 2458, 3277]
            }
        }
    },
    # 16543: {
    #     "buff_name": "宠物",
    #     "gain_attributes": {
    #         "pve_addition": 154
    #     }
    # },
    16102: {
        "buff_name": "引魂",
        "gain_attributes": {
            "magical_attack_power_gain": 410,
            "surplus_gain": 410
        }
    },
    17988: {
        "buff_name": "曲致",
        "gain_attributes": {
            "magical_critical_strike_rate": 3000
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
