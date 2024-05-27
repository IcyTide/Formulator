from typing import Dict, Union

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS: Dict[int, Union[Buff, dict]] = {
    3401: {
        "buff_name": "神力",
        "activate": False,
        "gain_attributes": {
            "physical_critical_strike_rate": 400,
            "physical_critical_power_rate": 41
        }
    },
    3254: {
        "buff_name": "气魄",
        "gain_attributes": {
            "strength_gain": 20,
            "spunk_gain": 20
        }
    },
    17103: {
        "buff_name": "追命无声",
        "gain_skills": {
            6920: {
                "skill_damage_addition": 205
            }
        }
    },
    8210: {
        "buff_name": "心无旁骛",
        "gain_attributes": {
            "physical_critical_strike_rate": 1500,
            "physical_critical_power_rate": 300
        }
    },
    9981: {
        "buff_name": "秋风散影",
        "gain_attributes": {
            "physical_critical_strike_rate": 1000,
            "physical_critical_power_rate": 102
        }
    },
    # 23074: {
    #     "buff_name": "逐一击破",
    #     "gain_attributes": {
    #         "all_damage_addition": 103
    #     }
    # },
    # 10169: {
    #     "buff_name": "逐一击破",
    #     "gain_attributes": {
    #         "all_damage_addition": 103
    #     }
    # },
    7659: {
        "buff_name": "命陨",
        "gain_attributes": {
            "physical_attack_power_gain": 205
        }
    },
    28225: {
        "buff_name": "蹑景",
        "gain_skills": {
            6920: {
                "skill_pve_addition": 1229
            }
        }
    },
    28226: {
        "buff_name": "蹑景",
        "gain_skills": {
            6920: {
                "skill_pve_addition": 820
            }
        }
    },
    28227: {
        "buff_name": "蹑景",
        "gain_skills": {
            6920: {
                "skill_pve_addition": 615
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
