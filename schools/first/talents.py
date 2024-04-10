from typing import Dict, List

from base.buff import Buff

TALENT_GAINS: List[Dict[int, dict | Buff]] = [
    {16691: {"buff_name": "龙息"}},
    {16847: {"buff_name": "归酣"}},
    {
        26904: {
            "buff_name": "冥鼔",
            "gain_skills": {
                **{
                    skill_id: {
                        "physical_damage_addition": 205,
                        "physical_shield_gain": -512
                    } for skill_id in [16760, 16382, 20991]
                },
                32823: {
                    "physical_shield_gain": [0, 0, -512, -512]
                },
            }
        },
        17042: {
            "buff_name": "阳关",
            "gain_skills": {
                **{
                    skill_id: {
                        "physical_damage_addition": 154,
                        "physical_shield_gain": -205
                    } for skill_id in [16803, 16802, 16801, 16800, 17043, 19423, 19424]
                },
                32859: {
                    "physical_damage_addition": 154,
                },
            }
        }
    },
    {16799: {"buff_name": "霜天"}},
    {25633: {"buff_name": "含风"}},
    {32857: {"buff_name": "见尘"}},
    {17047: {"buff_name": "分疆"}},
    {
        25258: {"buff_name": "掠关"},
        16728: {
            "buff_name": "星火",
            "gain_attributes": {
                "strength_gain": 102
            }
        },
        34677: {
            "buff_name": "绝河",
            "gain_skills": {
                20991: {
                    "physical_damage_addition": 307
                }
            }
        }
    },
    {16737: {"buff_name": "楚歌"}},
    {
        17056: {
            "buff_name": "绝期",
            "gain_skills": {
                11447: {
                    "attack_power_cof_gain": 0.7
                }
            }
        }
    },
    {16893: {"buff_name": "重烟"}},
    {21858: {"buff_name": "降麒式"}}
]

for talent in TALENT_GAINS:
    for talent_id, detail in talent.items():
        if not detail:
            talent[talent_id] = Buff()
        else:
            talent[talent_id] = Buff(talent_id, detail.pop("buff_name"))
        for attr, value in detail.items():
            setattr(talent[talent_id], attr, value)


TALENT_DECODER = {talent_id: talent.buff_name for talents in TALENT_GAINS for talent_id, talent in talents.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
