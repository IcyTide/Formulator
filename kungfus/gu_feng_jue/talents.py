from typing import Dict, List

from base.gain import Gain

TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            32450: Gain("渊冲", recipes=[(3011, 1)])
        },
        {
            32580: Gain("戗风", recipes=[(5584, 1), (5585, 1), (5586, 1)])
        },
        {
            32458: Gain("簇尘")
        },
        {
            32490: Gain("放皓", recipes=[(3023, 1)])
        },
        {
            33027: Gain("威声")
        },
        {
            32497: Gain("击懈")
        },
        {
            32512: Gain("界破")
        },
        {
            32508: Gain("长溯")
        },
        {
            32511: Gain("涣衍", recipes=[(-161, 1), (-162, 1)])
        },
        {
            32578: Gain("强膂", attributes=dict(strength_gain=102, strain_gain=102))
        },
        {
            32493: Gain("流岚")
        },
        {
            36035: Gain("潋风")
        }
    ],

    1: [
        {
            101537: Gain("斩涛", attributes=dict(strength_gain=154))
        },
        {
            101539: Gain("披靡")
        },
        {
            101542: Gain("倒海")
        },
        {
            101395: Gain("孤风破浪")
        }
    ]
}
