from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS = {
    1437: {
        "buff_name": "嗔怒",
        "activate": False,
        "gain_attributes": {
            "magical_critical_strike_gain": 400,
            "magical_critical_power_gain": 41
        }
    },
    409: {
        "buff_name": "剑舞",
        "gain_attributes": {
            "magical_attack_power_gain": 31
        }
    },
    10240: {
        "buff_name": "满堂",
        "gain_attributes": {
            "magical_critical_strike_gain": 800,
            "magical_critical_power_gain": 21
        }
    },
    25902: {
        "buff_name": "流玉",
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": 512,
            } for skill_id in (6234, 6554)
        }
    },
    538: {
        "buff_name": "繁音急节",
        "gain_attributes": {
            "magical_attack_power_gain": 461
        }
    },
    17010: {
        "buff_name": "广陵月",
        "gain_attributes": {
            "magical_critical_power_gain": 20
        }
    },
    5788: {
        "buff_name": "枕上",
        "gain_attributes": {
            "magical_shield_ignore": 102,
        }
    },
    9927: {
        "buff_name": "夜天",
        "gain_attributes": {
            "all_damage_addition": 102,
        }
    },
    17969: {
        "buff_name": "化冰",
        "gain_attributes": {
            "pve_addition": 71,
        }
    },
}

for buff_id, detail in BUFFS.items():
    BUFFS[buff_id] = Buff(buff_id, detail.pop("buff_name"))
    for attr, value in detail.items():
        setattr(BUFFS[buff_id], attr, value)

for buff_id, buff in GENERAL_BUFFS.items():
    BUFFS[buff_id] = buff
