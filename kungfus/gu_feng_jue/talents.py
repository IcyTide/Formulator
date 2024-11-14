from typing import Dict, List

from base.gain import Gain

TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            32450: Gain("渊冲", recipes=[(3011, 1)]),
            32449: Gain("中峙", recipes=[(3010, 1)])
        },
        {
            32580: Gain("戗风", recipes=[(5584, 1), (5585, 1), (5586, 1)])
        },
        {
            32464: Gain("溃延"),
            32456: Gain("雨积")
        },
        {
            32490: Gain("放皓", recipes=[(3023, 1)])
        },
        {
            32492: Gain("电逝"),
            33027: Gain("威声")
        },
        {
            32497: Gain("击懈", recipes=[(5588, 1)]),
            32500: Gain("承磊")
        },
        {
            32502: Gain("滔天"),
            32457: Gain("镇机"),
            32512: Gain("界破")
        },
        {
            32508: Gain("长溯")
        },
        {
            32511: Gain("涣衍", recipes=[(-161, 1), (-162, 1)])
        },
        {
            32513: Gain("涤瑕", recipes=[(3033, 1)]),
            32578: Gain("强膂", attributes=dict(strength_gain=102, strain_gain=102))
        },
        {
            32493: Gain("流岚"),
        },
        {
            36035: Gain("潋风"),
            32586: Gain("截辕")
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
