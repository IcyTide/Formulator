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
            30921: Gain("擘两分星")
        },
        {
            40275: Gain("天罗地网")
        },
        {
            27267: Gain("神威穿彻")
        },
        {
            30721: Gain("巧夺天工")
        },
        {
            14857: Gain("雷甲三铉")
        },
        {
            6508: Gain("千机不殆", recipes=[(1223, 1)])
        },
        {
            34679: Gain("雀引彀中")
        },
        {
            14856: Gain("曙色催寒")
        },
        {
            30723: Gain("千机连环")
        }
    ]
}
