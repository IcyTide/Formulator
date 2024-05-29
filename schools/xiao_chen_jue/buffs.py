from typing import Dict, Union

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS: Dict[int, Union[Buff, dict]] = {
    1438: {
        "buff_name": "剑鸣",
        "activate": False,
        "gain_attributes": {
            "physical_critical_strike_rate": 400,
            "physical_critical_power_rate": 41
        }
    },
    5994: {
        "buff_name": "酣畅淋漓",
        "gain_attributes": {
            "physical_critical_strike_rate": 2000,
            "all_shield_ignore": [0, 0, 0, 440]
        }
    },
    6385: {
        "buff_name": "亢龙·镇慑",
        "gain_attributes": {
            "physical_overcome_gain": [256, 358]
        }
    },
    6398: {
        "buff_name": "亢龙·霆击",
        "gain_attributes": {
            "physical_attack_power_gain": 204
        }
    },
    25904: {
        "buff_name": ["蛟影·一重", "蛟影·二重", "蛟影·三重", "蛟影·四重", "蛟影·易损"],
        "gain_attributes": {
            "all_damage_addition": [82, 123, 184, 266, 440]
        }
    },
    6377: {
        "buff_name": "无疆",
        "gain_attributes": {
            "physical_attack_power_gain": 154
        }
    },
    12356: {
        "buff_name": "盈久",
        "gain_attributes": {
             "all_damage_addition": [51, 102, 205, 154]
        }
    },
    9719: {
        "buff_name": "酒中仙",
        "gain_attributes": {
            "physical_critical_power_rate": 123
        }
    },
    10221: {
        "buff_name": "青龙",
        "gain_attributes": {
            "all_damage_addition": 31
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
