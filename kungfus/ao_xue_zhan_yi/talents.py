from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            18487: Gain("百折"),
            5656: Gain("封侯", recipes=[(5649, 1)]),
            5657: Gain("扬戈", recipes=[(1224, 1)])
        },
        {
            5660: Gain("神勇", recipes=[(1225, 1)])
        },
        {
            5659: Gain("大漠"),
            18602: Gain("骁勇", recipes=[(recipe_id, 1) for recipe_id in (4686, 4687, 4688, 4689)])
        },
        {
            24896: Gain("龙驭"),
            18226: Gain("击水", recipes=[(recipe_id, -1) for recipe_id in (-132, -153)])
        },
        {
            14824: Gain("驰骋")
        },
        {
            6511: Gain("牧云")
        },
        {
            5666: Gain("风虎")
        },
        {
            6781: Gain("战心")
        },
        {
            6524: Gain("破楼兰"),
            2628: Gain("渊")
        },
        {
            5678: Gain("夜征")
        },
        {
            15001: Gain("龙血")
        },
        {
            6517: Gain("虎贲")
        }
    ]
}
