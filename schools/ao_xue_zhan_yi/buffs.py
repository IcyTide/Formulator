from typing import Dict, Union

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS: Dict[int, Union[Buff, dict]] = {
    1428: {
        "buff_name": "军啸",
        "activate": False,
        "gain_attributes": {
            "physical_critical_strike_rate": 400,
            "physical_critical_power_rate": 41
        }
    },
    -1: {
        "buff_name": "战意",
        "max_stack": 5
    },
    6121: {
        "buff_name": "驰骋",
        "gain_attributes": {
            "physical_attack_power_gain": [154, 307]
        }
    },
    6363: {
        "buff_name": "激雷",
        "gain_attributes": {
            "physical_attack_power_gain": [205, 0, 205, 0],
            "physical_overcome_gain": [205, 0, 205, 0],
            "physical_critical_strike_rate": [0, 3000, 3000, 3000],
            "all_shield_ignore": [0, 0, 0, 717]
        }
    },
    14981: {
        "buff_name": "百折",
        "gain_attributes": {
            "all_damage_addition": 307
        }
    },
    7671: {
        "buff_name": "牧云",
        "gain_attributes": {
            "physical_critical_strike_rate": 300,
            "physical_critical_power_rate": 102
        }
    },
    21638: {
        "buff_name": "龙驭",
        "gain_attributes": {
            "all_damage_addition": 72
        }
    },
    2779: {
        "buff_name": "渊",
        "gain_attributes": {
            "physical_attack_power_gain": 512
        }
    },
    -12608: {
        "buff_name": "风虎",
        "activate": False,
        "interval": 1,
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": [51, 102, 154, 205, 256]
            } for skill_id in [18207] + [18603] + [18773, 15002] + [702, 24898, 6526]
        }
    },
    -26008: {
        "buff_name": "战心",
        "interval": 4,
        "gain_skills": {
            3442: {
                "attack_power_cof_gain": 1.2
            }
        }
    },
    -28169: {
        "buff_name": "龙印",
        "interval": 480,
        "max_stack": 3
    },
}

for buff_id, detail in BUFFS.items():
    BUFFS[buff_id] = Buff(buff_id)
    for attr, value in detail.items():
        setattr(BUFFS[buff_id], attr, value)

for buff_id, buff in GENERAL_BUFFS.items():
    if buff_id not in BUFFS:
        BUFFS[buff_id] = buff
