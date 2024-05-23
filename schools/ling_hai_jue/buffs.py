from typing import Dict, Union

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS: Dict[int, Union[Buff, dict]] = {
    14353: {
        "buff_name": "羽念",
        "activate": False,
        "gain_attributes": {
            "physical_critical_strike_gain": 400,
            "physical_critical_power_gain": 41
        }
    },
    14083: {
        "buff_name": "太息",
        "gain_attributes": {
            "physical_attack_power_gain": [102, 205],
        }
    },
    13560: {
        "buff_name": "羽彰",
        "activate": False,
        "gain_attributes": {
            "physical_overcome_gain": 205
        }
    },
    17094: {
        "buff_name": "鸿轨",
        "gain_attributes": {
            "physical_critical_strike_gain": 1500,
            "physical_critical_power_gain": 205
        }
    },
    13966: {
        "buff_name": "梦悠",
        "gain_attributes": {
            "all_shield_ignore": 205
        }
    },
    14321: {
        "buff_name": "驰行",
        "frame_shift": -2,
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": 307,
            }
            for skill_id in (20322, 20684, 20685, 20323)
        }
    },
    14317: {
        "buff_name": "神降",
        "gain_skills": {
            20054: {
                "skill_critical_strike": [1000, 2000, 3000, 4000, 5000],
                "skill_critical_power": [102, 205, 307, 410, 512]
            }
        }
    },
    14029: {
        "buff_name": "神降",
        "activate": False,
        "gain_attributes": {
            "all_damage_addition": 102
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
