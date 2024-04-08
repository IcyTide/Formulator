from base.buff import Buff

talents = {
    "26904": {
        "buff_name": "冥鼔",
        "gain_skills": {
            **{
                skill_id: {
                    "physical_damage_addition": 205,
                    "physical_shield_gain": -512
                } for skill_id in ["16760", "16382", "20991"]
            },
            "32823": {
                "physical_shield_gain": [0, 0, -512, -512]
            },
        }
    },
    "17042": {
        "buff_name": "阳关",
        "gain_skills": {
            **{
                skill_id: {
                    "physical_damage_addition": 154,
                    "physical_shield_gain": -205
                } for skill_id in ["16803", "16802", "16801", "16800", "17043", "19423", "19424"]
            },
            "32859": {
                "physical_damage_addition": 154,
            },
        }
    },
    "16728": {
        "buff_name": "星火",
        "gain_attributes": {
            "strength_gain": 102
        }
    },
    "34677": {
        "buff_name": "绝河",
        "gain_skills": {
            "20991": {
                "physical_damage_addition": 307
            }
        }
    },
    "17056": {
        "buff_name": "绝期",
        "gain_skills": {
            "11447": {
                "attack_power_cof_gain": 0.7
            }
        }
    }
}

for talent_id, detail in talents.items():
    talents[talent_id] = Buff(talent_id, detail.pop("buff_name"))
    for attr, value in detail.items():
        setattr(talents[talent_id], attr, value)
print(len(talents))
