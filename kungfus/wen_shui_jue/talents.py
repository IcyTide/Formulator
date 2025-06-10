from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        5953: Gain("淘尽", recipes=[(1235, 1)])
    },
    {
        5954: Gain("清风", recipes=[(1236, 1)])
    },
    {
        5952: Gain("岱宗", buff_ids=[22913])
    },
    {
        6549: Gain("残雪")
    },
    {
        5959: Gain("映波锁澜", recipes=[(3178, 1)], buff_ids=[19187]),
        5964: Gain("造化", buff_ids=[9903])
    },
    {
        5957: Gain("怜光", buff_ids=[12317])
    },
    {
        6545: Gain("层云", buff_ids=[21640])
    },
    {
        30862: Gain("山倾", skill_ids=[30861, 32967]),
        29090: Gain("撼岳", recipes=[(2740, 1)], skill_ids=[29129])
    },
    {
        6534: Gain("雾锁", buff_ids=[9714])
    },
    {
        6548: Gain("碧归", buff_ids=[26207])
    },
    {
        14605: Gain("如风")
    },
    {
        30777: Gain("听晓", buff_ids=[29360])
    }
]
