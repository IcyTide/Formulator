from base.buff import Buff
from general.buffs import GENERAL_BUFFS


BUFFS = {
    11378: {
        "buff_name": "朔气",
        "activate": False,
        "gain_attributes": {
            "physical_critical_strike_gain": 400,
            "physical_critical_power_gain": 41
        }
    },
    24553: {
        "buff_name": "灭影追风",
        "gain_attributes": {
            "physical_overcome_gain": 102,
            "physical_critical_strike_gain": 1000,
            "physical_critical_power_gain": 102
        }
    },
    24557: {
        "buff_name": "戗风",
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": 154,
            }
            for skill_id in [32602, 32603, 32604, 32234] + [32235, 32236, 32237, 32238, 32239, 32891, 32892]
        }
    },
    24180: {
        "buff_name": "镇机",
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": [123, 246, 369, 492, 614, 737]
            } for skill_id in (32167, 32348)
        }
    },
    24209: {
        "buff_name": "流岚",
        "gain_attributes": {
            "all_shield_ignore": 410
        }
    },
    -32513: {
        "buff_name": "涤瑕",
        "activate": False,
        "gain_skills": {
            24443: {
                "attack_power_cof_gain": 0.1
            }
        }
    }
}

for buff_id, detail in BUFFS.items():
    BUFFS[buff_id] = Buff(buff_id, detail.pop("buff_name"))
    for attr, value in detail.items():
        setattr(BUFFS[buff_id], attr, value)

for buff_id, buff in GENERAL_BUFFS.items():
    BUFFS[buff_id] = buff
