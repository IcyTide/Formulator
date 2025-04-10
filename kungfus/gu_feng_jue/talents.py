from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        32450: Gain("渊冲", recipes=[(3011, 1)])
    },
    {
        32580: Gain("戗风", buff_ids=[30304], recipes=[(5584, 1), (5585, 1), (5586, 1)])
    },
    {
        32458: Gain("簇尘"),
        32499: Gain("观衅")
    },
    {
        32490: Gain("放皓", recipes=[(3023, 1)])
    },
    {
        33027: Gain("威声")
    },
    {
        32497: Gain("击懈"),
        32458: Gain("簇尘"),
        32500: Gain("承磊", skill_ids=[40645])
    },
    {
        32512: Gain("界破", skill_ids=[34695]),
        32502: Gain("滔天", skill_ids=list(range(32359, 32361 + 1)) + list(range(32216, 32218 + 1)))
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
        32493: Gain("流岚", buff_ids=[24209]),
        32509: Gain("斩颓"),
    },
    {
        36035: Gain("潋风", skill_ids=[36118])
    }
]
