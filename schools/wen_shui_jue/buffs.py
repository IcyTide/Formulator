from typing import Dict, Union

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS: Dict[int, Union[Buff, dict]] = {
    1955: {
        "buff_name": "器攻",
        "activate": False,
        "gain_attributes": {
            "physical_critical_strike_rate": 400,
            "physical_critical_power_rate": 41
        }
    },
    -1905: {
        "buff_name": "重剑",
        "gain_attributes": True
    },
    1728: {
        "buff_name": "莺鸣",
        "gain_attributes": {
            "physical_critical_strike_rate": 2000
        }
    },
    22913: {
        "buff_name": "岱宗",
        "gain_attributes": {
            "physical_critical_power_rate": 82
        }
    },
    9903: {
        "buff_name": "造化",
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": [102, 154]
            } for skill_id in [2896] + [1594, 1595, 18317]
        }
    },
    12317: {
        "buff_name": "怜光",
        "gain_attributes": {
            "all_damage_addition": 102
        }
    },
    21640: {
        "buff_name": "层云",
        "gain_skills": {
            18991: {
                "skill_damage_addition": [0, 102, 205, 307, 410, 512]
            }
        }
    },
    26207: {
        "buff_name": "碧归",
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": 307
            } for skill_id in [2896] + [1594, 1595, 18317] + [1598]
        }
    },
    9714: {
        "buff_name": "雾锁",
        "gain_attributes": {
            "all_shield_ignore": 614,
        }
    },
    18008: {
        "buff_name": "闻踪",
        "gain_attributes": {
            "physical_critical_strike_rate": 1000
        },
        "gain_skills": {
            18299: {
                "skill_damage_addition": 410
            }
        }
    },
    26047: {
        "buff_name": "飞来",
        "gain_attributes": {
            "physical_critical_power_rate": [150, 120, 90]
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
