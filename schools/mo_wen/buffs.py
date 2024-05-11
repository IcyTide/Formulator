from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS = {
    9586: {
        "buff_name": "挥散",
        "activate": False,
        "gain_attributes": {
            "magical_critical_strike_gain": 400,
            "magical_critical_power_gain": 41
        }
    },
    9433: {
        "buff_name": "阳春白雪",
        "gain_skills": {
            skill_id: {
                "skill_shield_gain": [-307, -614, -921]
            } for skill_id in (14227, 18859, 18860)
        }
    },
    12576: {
        "buff_name": "云汉",
        "frame_shift": -3,
        "gain_attributes": {
            "all_damage_addition": 51,
        }
    },
    9495: {
        "buff_name": "明津",
        "gain_skills": {
            **{
                skill_id: {
                    "skill_damage_addition": 205,
                } for skill_id in (14227, 18859, 14100, 18860)
            },
            **{
                skill_id: {
                    "attack_power_cof_gain": 1.2
                } for skill_id in (9357, 9361)
            }
        }
    },
    9437: {
        "buff_name": "参连",
        "gain_attributes": {
            "magical_attack_power_gain": 102
        }
    },
    25997: {
        "buff_name": "知音妙意",
        "frame_shift": -1,
        "gain_attributes": {
            "magical_critical_power_gain": [102, 204, 410]
        }
    },
}

for buff_id, detail in BUFFS.items():
    BUFFS[buff_id] = Buff(buff_id)
    for attr, value in detail.items():
        setattr(BUFFS[buff_id], attr, value)

for buff_id, buff in GENERAL_BUFFS.items():
    if buff_id not in BUFFS:
        BUFFS[buff_id] = buff