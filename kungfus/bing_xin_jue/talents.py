from typing import Dict, List

from base.gain import Gain

TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            6569: Gain("明妃"),
            5848: Gain("伤春", recipes=[(2893, 1)]),
            5849: Gain("青梅嗅", recipes=[(1246, 1)])
        },
        {
            5869: Gain("惊寒", recipes=[(1488, 1), (4478, 1)]),
            5868: Gain("千里冰封", recipes=[(2014, 1), (2015, 1), (2016, 1)])
        },
        {
            5852: Gain("新妆")
        },
        {
            37316: Gain("芳姿畅音")
        },
        {
            5864: Gain("枕上")
        },
        {
            6556: Gain("生莲", recipes=[(1254, 1)]),
            23935: Gain("广陵月")
        },
        {
            34604: Gain("流玉")
        },
        {
            22732: Gain("钗燕")
        },
        {
            24995: Gain("盈袖", recipes=[(5634, 1)])
        },
        {
            24996: Gain("化冰")
        },
        {
            14934: Gain("夜天"),
            23457: Gain("琼宵"),
            38617: Gain("明空")
        },
        {
            34603: Gain("凝华"),
            14715: Gain("轻妒")
        }
    ],

    1: [
        {
            100585: Gain("红袖")
        },
        {
            100586: Gain("弦曲")
        },
        {
            100588: Gain("筝曲")
        },
        {
            100377: Gain("霜天剑泠"),
            100598: Gain("合璧知意")
        }
    ]
}
