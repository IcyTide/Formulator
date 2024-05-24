from typing import Dict, Union

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS: Dict[int, Union[Buff, dict]] = {
    11378: {
        "buff_name": "朔气",
        "activate": False,
        "gain_attributes": {
            "physical_critical_strike_gain": 400,
            "physical_critical_power_gain": 41
        }
    },
    18384: {
        "buff_name": "含风",
        "interval": 384,
        "gain_attributes": {
            "physical_critical_strike_gain": 1000,
            "physical_critical_power_gain": 102
        }
    },
    23066: {
        "buff_name": "含风",
        "interval": 384,
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": 102,
            }
            for skill_id in (16787, 16610, 16794)
        }
    },
    14972: {
        "buff_name": "爆体",
        "gain_attributes": {
            "all_damage_addition": 205
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
