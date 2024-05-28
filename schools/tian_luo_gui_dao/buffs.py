from typing import Dict, Union

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS: Dict[int, Union[Buff, dict]] = {
    3401: {
        "buff_name": "神力",
        "activate": False,
        "gain_attributes": {
            "physical_critical_strike_rate": 400,
            "physical_critical_power_rate": 41
        }
    },
    3254: {
        "buff_name": "气魄",
        "gain_attributes": {
            "strength_gain": 20,
            "spunk_gain": 20
        }
    },
    3316: {
        "buff_name": "扬威",
        "gain_attributes": {
            "magical_attack_power_gain": 512,
        }
    },
    6105: {
        "buff_name": "弩心",
        "gain_attributes": {
            "magical_overcome_gain": 154,
        }
    },
    8210: {
        "buff_name": "心无旁骛",
        "gain_attributes": {
            "physical_critical_strike_rate": 1500,
            "physical_critical_power_rate": 300
        }
    },
    9981: {
        "buff_name": "秋风散影",
        "gain_attributes": {
            "physical_critical_strike_rate": 1000,
            "physical_critical_power_rate": 102
        }
    },
    10005: {
        "buff_name": "催寒",
        "gain_attributes": {
            "all_shield_ignore": 410
        }
    },
    23081: {
        "buff_name": "擘两分星",
        "gain_attributes": {
            "all_damage_addition": 205
        }
    },
    23082: {
        "buff_name": "擘两分星",
        "gain_skills": {
            skill_id: {
                "attack_power_cof_gain": 0.1
            } for skill_id in (3313, 36502, 30894, 30727)
        }
    },
    27457: {
        "buff_name": "诡鉴拟态天绝数量",
    },
    -24668: {
        "buff_name": "杀机断魂",
        "activate": False,
        "max_stack": 5,
        "gain_attributes": {
            "all_damage_addition": 103
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
