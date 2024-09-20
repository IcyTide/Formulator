from typing import Dict, List

from base.gain import Gain

TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            5953: Gain("淘尽", recipes=[(1235, 1)])
        },
        {
            5954: Gain("清风", recipes=[(1236, 1)])
        },
        {
            5952: Gain("岱宗")
        },
        {
            18682: Gain("景行")
        },
        {
            5964: Gain("造化")
        },
        {
            5957: Gain("怜光")
        },
        {
            6545: Gain("层云")
        },
        {
            30862: Gain("山倾")
        },
        {
            6534: Gain("雾锁")
        },
        {
            6548: Gain("碧归")
        },
        {
            14605: Gain("如风")
        },
        {
            25070: Gain("飞来闻踪"),
            30777: Gain("听晓")
        }
    ]
}
