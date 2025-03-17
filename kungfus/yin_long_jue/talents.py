from typing import Dict, List

from base.gain import Gain

TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            22557: Gain("星旗"),
            22560: Gain("秋霁")
        },
        {
            22562: Gain("雪覆")
        },
        {
            26760: Gain("遗恨"),
            40161: Gain("蹈厉")
        },
        {
            22571: Gain("风骨")
        },
        {
            23309: Gain("北阙")
        },
        {
            22575: Gain("渊岳", recipes=[(4950, 1)])
        },
        {
            22579: Gain("玄肃", recipes=[(4952, 1)])
        },
        {
            29166: Gain("飞刃回转")
        },
        {
            22593: Gain("百节")
        },
        {
            22587: Gain("忘断")
        },
        {
            22596: Gain("徵逐")
        },
        {
            22603: Gain("青山共我"),
            30849: Gain("孤路")
        }
    ]
}
