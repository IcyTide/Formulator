from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS = {
    1440: {
        "buff_name": "怒叱",
        "activate": False,
        "gain_attributes": {
            "magical_critical_strike_gain": 400,
            "magical_critical_power_gain": 41
        }
    },
    1487: {
        "buff_name": "布散",
        "gain_attributes": {
            "magical_attack_power_gain": 307,
        }
    },
    14636: {
        "buff_name": "乱洒",
        "gain_skills": {
            182: {
                "skill_damage_addition": 307,
            }
        }
    },
    11809: {
        "buff_name": "倚天",
        "gain_attributes": {
            "all_shield_ignore": 102
        }
    },
    12588: {
        "buff_name": "清流",
        "gain_attributes": {
            "all_damage_addition": 102
        }
    },
    24599: {
        "buff_name": "雪中行",
        "gain_attributes": {
            "magical_attack_power_gain": 102,
            "magical_critical_strike_gain": 600
        },
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": [174, 348, 420]
            } for skill_id in (33222,)
        }
    },
    28116: {
        "buff_name": "钟灵",
        "gain_attributes": {
            "magical_attack_power_gain": 102,
            "surplus_gain": 102
        }
    },
    -32489: {
        "buff_name": "青冠",
        "activate": False,
        "gain_attributes": {
            "global_damage_factor": [
                1.25,
                2.
            ]
        }
    },
    9722: {
        "buff_name": "涓流",
        "gain_attributes": {
            "magical_critical_strike_gain": 160,
            "magical_critical_power_gain": 16
        }
    },
}

for buff_id, detail in BUFFS.items():
    BUFFS[buff_id] = Buff(buff_id)
    for attr, value in detail.items():
        setattr(BUFFS[buff_id], attr, value)

for buff_id, buff in GENERAL_BUFFS.items():
    BUFFS[buff_id] = buff
