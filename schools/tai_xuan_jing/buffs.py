from typing import Dict, Union

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS: Dict[int, Union[Buff, dict]] = {
    18555: {
        "buff_name": "星悬",
        "activate": False,
        "gain_attributes": {
            "magical_critical_strike_gain": 400,
            "magical_critical_power_gain": 41
        }
    },
    28303: {
        "buff_name": "重山·一",
        "gain_skills": {
            skill_id: {
                "attack_power_cof_gain": 1.074,
            } for skill_id in (24676, 24813, 24823, 34683)
        }
    },
    28304: {
        "buff_name": "重山·二",
        "gain_skills": {
            skill_id: {
                "attack_power_cof_gain": 1.14815
            } for skill_id in (24676, 24813, 24823, 34683)
        }
    },
    28305: {
        "buff_name": "重山·三",
        "gain_skills": {
            skill_id: {
                "attack_power_cof_gain": 1.2223,
            } for skill_id in (24676, 24813, 24823, 34683)
        }
    },
    18021: {
        "buff_name": "荧入白",
        "gain_attributes": {
            "all_shield_ignore": 512
        }
    },
    18174: {
        "buff_name": "鬼遁",
        "gain_attributes": {
            "magical_attack_power_gain": 308
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
