from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        24936: Gain("水盈"),
        24925: Gain("正夏", recipes=[(5166, 1)]),
        24930: Gain("明心", recipes=[(5167, 1)])
    },
    {
        24932: Gain("天网"),
        34680: Gain("度冥")
    },
    {
        25034: Gain("顺祝")
    },
    {
        24994: Gain("龙回首"),
        25071: Gain("枭神")
    },
    {
        24983: Gain("重山", recipes=[(5179, 1), (5180, 1), (5181, 1)]),
        25025: Gain("地遁")
    },
    {
        25072: Gain("鬼遁"),
        25137: Gain("堪卜")
    },
    {
        25022: Gain("祝祷"),
        25368: Gain("亘天"),
        37456: Gain("追叙")
    },
    {
        25378: Gain("连断"),
        25066: Gain("神元", attributes=dict(spunk_gain=102)),
        25382: Gain("知微"),
        36191: Gain("趋时")
    },
    {
        25085: Gain("荧入白")
    },
    {
        25379: Gain("征凶")
    },
    {
        25088: Gain("擎羊"),
        25173: Gain("灵器")
    },
    {
        37505: Gain("镇星入舆")
    }
]
