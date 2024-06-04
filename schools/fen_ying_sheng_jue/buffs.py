from typing import Dict, Union

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS: Dict[int, Union[Buff, dict]] = {
    4671: {
        "buff_name": "明尊",
        "activate": False,
        "attributes": {
            "magical_critical_strike_rate": 400,
            "magical_critical_power_rate": 41
        }
    },
    6277: {
        "buff_name": "无明业火",
        "attributes": {
            "magical_critical_strike_rate": 1000,
            "magical_critical_power_rate": 52
        }
    },
    12575: {
        "buff_name": "用晦而明",
        "attributes": {
            "all_shield_ignore": 563
        }
    },
    25758: {
        "buff_name": "明光月",
        "gains": {
            skill_id: {
                "skill_attack_power": 246,
            } for skill_id in [4036, 25726] + [34349] + [4476]
        }
    },
    25759: {
        "buff_name": "明光日",
        "gains": {
            skill_id: {
                "skill_critical_strike": 1500,
                "skill_critical_power": 102
            } for skill_id in [4035, 25725] + [34348] + [4483 + i for i in range(8)] + [26916]
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
