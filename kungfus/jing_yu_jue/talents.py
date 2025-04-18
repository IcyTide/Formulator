from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        6437: Gain("迅电流光", recipes=[(1200, 1)])
    },
    {
        6473: Gain("千里无痕", buff_ids=[7659])
    },
    {
        5721: Gain("百步穿杨", skill_ids=[3291]),
    },
    {
        21724: Gain("掠影穹苍", skill_ids=[22789])
    },
    {
        37324: Gain("蹑景追风", buff_ids=[28225, 28226, 28227]),
    },
    {
        6451: Gain("聚精凝神")
    },
    {
        14851: Gain("空山独立", buff_ids=[10167, 10169])
    },
    {
        6454: Gain("清夜裁云", buff_ids=[15945])
    },
    {
        6461: Gain("秋风散影", buff_ids=[9981])
    },
    {
        37325: Gain("牢甲利兵", skill_ids=[37504])
    },
    {
        14850: Gain("妙手连环", recipes=[(4588, 1)])
    },
    {
        18672: Gain("百里追魂", skill_ids=[33870]),
        30588: Gain("凝形逐踪", buff_ids=[22750], skill_ids=[30629]),
        34644: Gain("敛影无锋", buff_ids=[22750], skill_ids=[33870, 30629])
    }
]
