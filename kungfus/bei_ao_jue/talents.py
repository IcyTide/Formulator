from typing import Dict, List

from base.gain import Gain


TALENTS: List[Dict[int, Gain]] = [
    {
        16691: Gain("龙息")
    },
    {
        16847: Gain("归酣"),
        16816: Gain("碎影")
    },
    {
        26904: Gain("冥鼓", recipes=[(2510, 1), (2511, 1)])
    },
    {
        16728: Gain("星火", attributes=dict(strength_gain=102, strain_gain=307)),
    },
    {
        26735: Gain("砺锋")
    },
    {
        37982: Gain("临江")
    },
    {
        16733: Gain("斩纷")
    },
    {
        16779: Gain("化蛟")
    },
    {
        38535: Gain("楚歌")
    },
    {
        17056: Gain("绝期", recipes=[(4319, 1), (2833, 1)])
    },
    {
        16977: Gain("冷川")
    },
    {
        21858: Gain("斩狂枭")
    }
]
