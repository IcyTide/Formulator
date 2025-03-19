from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        20333: Gain("江汉", recipes=[(5426, 1)])
    },
    {
        20335: Gain("扶桑", recipes=[(4694, 1)])
    },
    {
        25267: Gain("驾鸾")
    },
    {
        20348: Gain("清源")
    },
    {
        38669: Gain("青冥")
    },
    {
        38668: Gain("游仙")
    },
    {
        38670: Gain("鸿轨")
    },
    {
        20351: Gain("藏锋")
    },
    {
        21293: Gain("溯徊")
    },
    {
        38667: Gain("驰行")
    },
    {
        20747: Gain("梦悠", attributes=dict(all_shield_ignore=307))
    },
    {
        32594: Gain("怒翼")
    }
]
