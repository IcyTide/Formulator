from typing import Dict, List

from base.gain import Gain

TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            28371: Gain("血影留痕")
        },
        {
            6493: Gain("天风汲雨")
        },
        {
            6495: Gain("弩击急骤")
        },
        {
            6506: Gain("千机之威"),
            30921: Gain("擘两分星")
        },
        {
            6441: Gain("流星赶月", recipes=[(1204, 1)]),
            6504: Gain("天罗地网")
        },
        {
            6451: Gain("聚精凝神")
        },
        {
            18249: Gain("化血迷心")
        },
        {
            14857: Gain("雷甲三铉")
        },
        {
            6461: Gain("秋风散影")
        },
        {
            17572: Gain("分水逐旌"),
            34679: Gain("雀引彀中"),
            37327: Gain("云合影从")
        },
        {
            14856: Gain("曙色催寒")
        },
        {
            32742: Gain("诡鉴冥微"),
            18675: Gain("千秋万劫")
        }
    ]
}
