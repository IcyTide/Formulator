from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        38465: Gain("阳池", recipes=[(5578, 1)])
    },
    {
        38468: Gain("涌泉", recipes=[(5617, 1)])
    },
    {
        38473: Gain("封府", skill_ids=[38531])
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
        38475: Gain("纷飙", skill_ids=[39340], recipes=[(5620, 1)])
    },
    {
        38500: Gain("玉枕", buff_ids=[29243])
    },
    {
        38501: Gain("茫缈", recipes=[(5640, 1)]),
    },
    {
        38507: Gain("摧烟", skill_ids=[38557])
    },
    {
        38515: Gain("胧雾观花", skill_ids=[38590]),
        38511: Gain("一阳来复")
    }
]
