from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS = {
    1436: {
        "buff_name": "佛吼",
        "activate": False,
        "gain_attributes": {
            "magical_critical_strike_gain": 400,
            "magical_critical_power_gain": 41
        }
    },
    890: {
        "buff_name": "普渡",
        "interval": 352,
        "max_stack": 2
    },
    12479: {
        "buff_name": "普渡",
        "interval": 352,
        "max_stack": 3
    },
    19635: {
        "buff_name": "普渡",
        "interval": 4,
        "gain_attributes": {
            "magical_vulnerable": [41, 82, 123]
        }
    },
    11979: {
        "buff_name": "罗汉金身",
        "gain_attributes": {
            "magical_attack_power_gain": 308,
            "magical_overcome_gain": 308
        }
    },
    2686: {
        "buff_name": "擒龙诀",
        "gain_attributes": {
            "magical_attack_power_gain": 204
        }
    },
    10023: {
        "buff_name": "伏魔",
        "gain_attributes": {
            "all_damage_addition": 102
        }
    },
    12590: {
        "buff_name": "三生",
        "gain_attributes": {
            "magical_attack_power_gain": [82, 164, 246]
        }
    },
    24285: {
        "buff_name": "金刚日轮",
        "gain_attributes": {
            "magical_critical_strike_gain": 600,
            "magical_critical_power_gain": 62
        }
    },
    13910: {
        "buff_name": "众嗔",
        "frame_shift": -2,
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": 205
            } for skill_id in (3848, 3849, 3850, 3814, 3816, 13685)
        }
    },
    24453: {
        "buff_name": "贪破",
        "gain_attributes": {
            "surplus_gain": -30
        }
    },
    28296: {
        "buff_name": "布泽",
        "gain_skills": {
            skill_id: {
                "skill_pve_addition": 820
            } for skill_id in (17641, 3848, 3849, 3850, 236, 3810, 271, 743)
        }
    },
    1919: {
        "buff_name": "桑莲妙境",
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": 922
            } for skill_id in (3848, 3849, 3850, 271)
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
