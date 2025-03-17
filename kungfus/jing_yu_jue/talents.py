from typing import Dict, List

from base.gain import Gain

TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            6437: Gain("迅电流光", recipes=[(1200, 1)])
        },
        {
            6473: Gain("千里无痕")
        },
        {
            5721: Gain("百步穿杨"),
        },
        {
            21724: Gain("掠影穹苍")
        },
        {
            37324: Gain("蹑景追风"),
        },
        {
            6451: Gain("聚精凝神")
        },
        {
            14851: Gain("空山独立")
        },
        {
            6454: Gain("清夜裁云")
        },
        {
            6461: Gain("秋风散影")
        },
        {
            37325: Gain("牢甲利兵")
        },
        {
            14850: Gain("妙手连环", recipes=[(4588, 1)])
        },
        {
            18672: Gain("百里追魂"),
            30588: Gain("凝形逐踪")
        }
    ]
}
