from typing import Dict

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS: Dict[int, Buff | dict] = {
    1428: {
        "buff_name": "军啸",
        "activate": False,
        "gain_attributes": {
            "physical_critical_strike_gain": 400,
            "physical_critical_power_gain": 41
        }
    },
    9052: {
        "buff_name": "绝刀",
        "gain_skills": {
            13075: {
                "skill_damage_addition": [205, 410, 614, 819] * 2
            }
        }
    },
    8244: {
        "buff_name": "血怒",
        "gain_attributes": {
            "physical_attack_power_gain": 102
        }
    },
    8627: {
        "buff_name": "刀魂",
        "gain_attributes": {
            "physical_attack_power_gain": 154
        }
    },
    17176: {
        "buff_name": "分野",
        "gain_attributes": {
            "all_damage_addition": 51
        }
    },
    8267: {
        "buff_name": "恋战",
        "gain_attributes": {
            "physical_critical_strike_gain": 300,
        }
    },
    14309: {
        "buff_name": "锋鸣",
        "gain_attributes": {
            "physical_overcome_gain": 154
        }
    },
    27161: {
        "buff_name": "血怒·惊涌",
        "gain_attributes": {
            "physical_attack_power_gain": 102
        }
    },
    9889: {
        "buff_name": "蔑视",
        "gain_attributes": {
            "all_shield_ignore": 512
        }
    },
}

for buff_id, detail in BUFFS.items():
    BUFFS[buff_id] = Buff(buff_id)
    for attr, value in detail.items():
        setattr(BUFFS[buff_id], attr, value)

for buff_id, buff in GENERAL_BUFFS.items():
    BUFFS[buff_id] = buff
