from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        40721: Gain("征北", skill_ids=[40721])
    },
    {
        13089: Gain("炼狱", skill_ids=[29187])
    },
    {
        13136: Gain("铿锵")
    },
    {
        25356: Gain("严阵", buff_ids=[18222])
    },
    {
        13361: Gain("震怒"),
        13422: Gain("振奋")
    },
    {
        13133: Gain("怒炎", buff_ids=[8276])
    },
    {
        39045: Gain("蔑视", buff_ids=[-9889])
    },
    {
        13126: Gain("恋战", attributes=dict(all_damage_addition=102)),
        14840: Gain("肃驾")
    },
    {
        13366: Gain("从容", buff_ids=[8423])
    },
    {
        13134: Gain("寒甲", buff_ids=[8271, 17772]),
        25715: Gain("高城", attributes=dict(tank_buff_level=1))
    },
    {
        26897: Gain("鸿烈", skill_ids=[26898])
    },
    {
        25213: Gain("断马摧城", skill_ids=[25215]),
        15072: Gain("寒啸千军")
    }
]
