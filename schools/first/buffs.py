from base.buff import Buff

buffs = {
    18384: {
        "buff_name": "含风",
        "gain_attributes": {
            "physical_critical_strike_gain": 1000,
            "physical_critical_power_gain": 102
        }
    },
    23066: {
        "buff_name": "含风",
        "gain_skills": {
            16787: {
                "skill_damage_addition": 102,
            },
            16610: {
                "skill_damage_addition": 102,
            }
        }
    },
    14972: {
        "buff_name": "爆体",
        "gain_attributes": {
            "all_damage_addition": 205
        }
    }
}

for buff_id, detail in buffs.items():
    buffs[buff_id] = Buff(buff_id, detail.pop("buff_name"))
    for attr, value in detail.items():
        setattr(buffs[buff_id], attr, value)
