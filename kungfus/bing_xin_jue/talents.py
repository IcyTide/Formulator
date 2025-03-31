from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        5848: Gain("伤春", recipes=[(2893, 1)]),
        5849: Gain("青梅嗅", recipes=[(1246, 1)])
    },
    {
        5868: Gain("千里冰封", recipes=[(2014, 1), (2015, 1), (2016, 1)])
    },
    {
        5852: Gain("新妆")
    },
    {
        40177: Gain("步生花"),
        37316: Gain("芳姿畅音")
    },
    {
        5864: Gain("枕上")
    },
    {
        6556: Gain("生莲", recipes=[(5890, 1)]),
        23935: Gain("广陵月")
    },
    {
        34604: Gain("流玉")
    },
    {
        24995: Gain("盈袖")
    },
    {
        22732: Gain("钗燕"),
        6561: Gain("元君")
    },
    {
        24996: Gain("化冰")
    },
    {
        38617: Gain("明空")
    },
    {
        34603: Gain("凝华"),
        14705: Gain("霜降")
    }
]
