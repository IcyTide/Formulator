from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            38465: Gain("阳池", recipes=[(5578, 1)])
        },
        {
            38468: Gain("涌泉", recipes=[(5617, 1)])
        },
        {
            38473: Gain("封府")
        },
        {
            38480: Gain("见飓")
        },
        {
            38481: Gain("神封")
        },
        {
            38484: Gain("悬枢")
        },
        {
            40242: Gain("风萦", recipes=[(5845, 1)])
        },
        {
            38475: Gain("纷飙", recipes=[(5620, 1)])
        },
        {
            38500: Gain("玉枕")
        },
        {
            38501: Gain("茫缈", recipes=[(5640, 1)]),
        },
        {
            38507: Gain("摧烟")
        },
        {
            38515: Gain("胧雾观花")
        }
    ],
    1: [
        {
            102293: Gain("驭风"),
            102294: Gain("逆脉", attributes=dict(neutral_critical_strike_rate=1500))
        },
        {
            102296: Gain("风扬")
        },
        {
            102298: Gain("奇脉")
        },
        {
            102290: Gain("一阳化生")
        }
    ]
}
