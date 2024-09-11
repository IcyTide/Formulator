from typing import Dict, List

from base.dot import Dot
from base.gain import Gain


class 穿林打叶(Gain):
    def add_dots(self, dots: Dict[int, Dot]):
        dots[2237].tick_add -= 1
        # dots[12663].tick_add -= 1

    def sub_dots(self, dots: Dict[int, Dot]):
        dots[2237].tick_add += 1
        # dots[12663].tick_add += 1


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            6437: Gain("迅电流光", recipes=[(1200, 1)]),
            33118: Gain("声若惊雷", recipes=[(3167, 1)])
        },
        {
            6473: Gain("千里无痕")
        },
        {
            28366: Gain("寒江夜雨")
        },
        {
            21724: Gain("掠影穹苍")
        },
        {
            37324: Gain("蹑景追风")
        },
        {
            6451: Gain("聚精凝神")
        },
        {
            14851: Gain("逐一击破")
        },
        {
            28903: 穿林打叶("穿林打叶", recipes=[(-154, 1), (-155, 1), (2864, 1)]),
            6891: Gain("梨花带雨")
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
    ],
    1: []
}
