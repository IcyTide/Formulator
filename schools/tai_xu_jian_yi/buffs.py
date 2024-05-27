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
    378: {
        "buff_name": "碎星辰",
        "gain_attributes": {
            "physical_critical_strike_rate": [0] * 7 + [500, 1000] * 2,
            "physical_critical_power_rate": [0] * 6 + [100] + [100, 200] * 2,
            "all_shield_ignore": [0] * 9 + [614] * 2
        }
    },
    2757: {
        "buff_name": "紫气东来",
        "frame_shift": -2,
        "gain_attributes": {
            "physical_attack_power_gain": [256, 256, 512, 256],
            "magical_attack_power_gain": [256, 256, 512, 256],
            "all_critical_strike_rate": 2500,
            "all_critical_power_rate": 250
        }
    },
    14931: {
        "buff_name": "风逝",
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": 307
            } for skill_id in (386, 387, 388, 389, 390, 391, 392, 393, 394)
        }
    },
    17933: {
        "buff_name": "裂云",
        "gain_attributes": {
            "physical_critical_power_rate": 154,
        }
    },
    9949: {
        "buff_name": "玄门",
        "gain_attributes": {
            "physical_critical_strike_rate": 300,
            "physical_overcome_gain": 204
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
