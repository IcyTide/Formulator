from typing import Dict, List

from base.gain import Gain


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            402: Gain("定军"),
        },
        {
            5688: Gain("龙痕")
        },
        {
            5659: Gain("大漠"),
            18602: Gain("骁勇", recipes=[(recipe_id, 1) for recipe_id in (4686, 4687, 4688, 4689)])
        },
        {
            18226: Gain("击水", recipes=[(recipe_id, 1) for recipe_id in (-132, -153)])
        },
        {
            5681: Gain("留侯")
        },
        {
            18238: Gain("掠如火")
        },
        {
            5702: Gain("踏北邙")
        },
        {
            6781: Gain("战心")
        },
        {
            25354: Gain("崩决"),
            2628: Gain("渊")
        },
        {
            18239: Gain("昂如岳")
        },
        {
            14827: Gain("载戎")
        },
        {
            15115: Gain("号令三军")
        }
    ]
}
