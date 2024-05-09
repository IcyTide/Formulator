from typing import Dict

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS: Dict[int, Buff | dict] = {
    1439: {
        "buff_name": "气涌",
        "activate": False,
        "gain_attributes": {
            "magical_critical_strike_gain": 400,
            "magical_critical_power_gain": 41
        }
    },
    375: {
        "buff_name": "破苍穹",
        "gain_attributes": {
            "magical_critical_strike_gain": [300, 350, 400, 450, 0, 600, 700, 800, 900, 500, 500, 1000, 500, 1000],
            "magical_critical_power_gain": [61, 71, 81, 82, 102, 122, 143, 163, 184, 102, 102, 204, 102, 204],
            "all_shield_ignore": [0] * 12 + [614] * 2
        }
    },
    1908: {
        "buff_name": "会神",
        "gain_attributes": {
            "magical_critical_power_gain": 204,
        }
    },
    2757: {
        "buff_name": "紫气东来",
        "frame_shift": -1,
        "gain_attributes": {
            "physical_attack_power_gain": [256, 256, 512, 256],
            "magical_attack_power_gain": [256, 256, 512, 256],
            "all_critical_strike_gain": 2500,
            "all_critical_power_gain": 256
        }
    },
    9966: {
        "buff_name": "同尘",
        "gain_skills": {
            18670: {
                "skill_damage_addition": [358, 716, 1075, 1433]
            }
        }
    },
    # 12550: {
    #     "buff_name": "跬步",
    #     "gain_skills": {
    #         896: {
    #             "skill_damage_addition": [40, 81, 122, 163, 204]
    #         }
    #     }
    # },
    # 12551: {
    #     "buff_name": "跬步",
    #     "gain_skills": {
    #         skill_id: {
    #             "skill_damage_addition": [40, 81, 122, 163, 204]
    #         } for skill_id in (3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448)
    #     }
    # },
    17918: {
        "buff_name": "破势",
        "gain_skills": {
            skill_id: {
                "skill_pve_addition": 1331
            } for skill_id in (18649, 18650, 18651, 18652, 18653, 22014)
        }
    }
}

for buff_id, detail in BUFFS.items():
    BUFFS[buff_id] = Buff(buff_id)
    for attr, value in detail.items():
        setattr(BUFFS[buff_id], attr, value)

for buff_id, buff in GENERAL_BUFFS.items():
    BUFFS[buff_id] = buff
