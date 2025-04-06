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
        5852: Gain("新妆", skill_ids=[6554])
    },
    {
        40177: Gain("步生花"),
        37316: Gain("芳姿畅音", skill_ids=list(range(37317, 37320 + 1)))
    },
    {
        5864: Gain("枕上", buff_ids=[5788])
    },
    {
        6556: Gain("生莲", recipes=[(5890, 1)]),
        23935: Gain("广陵月", buff_ids=[17010])
    },
    {
        34604: Gain("流玉", buff_ids=[25902])
    },
    {
        24995: Gain("盈袖", skill_ids=[33140])
    },
    {
        22732: Gain("钗燕", skill_ids=[30532]),
        6561: Gain("元君", buff_ids=[12549])
    },
    {
        24996: Gain("化冰", buff_ids=[17969], skill_ids=[24999])
    },
    {
        38617: Gain("明空", buff_ids=[25435])
    },
    {
        34603: Gain("凝华", skill_ids=[34612, 35058]),
        14705: Gain("霜降", buff_ids=[30274])
    }
]
