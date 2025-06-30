from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        5974: Gain("血泪成悦")
    },
    {
        18279: Gain("净身明礼", skill_ids=[18280, 18281], recipes=[(5149, 1), (5150, 1)])
    },
    {
        25178: Gain("昭昭", skill_ids=[25179])
    },
    {
        6751: Gain("无明业火", skill_ids=[6750])
    },
    {
        6760: Gain("纵遇善缘", skill_ids=[40255])
    },
    {
        14698: Gain("驱夷逐法", buff_ids=[12578])
    },
    {
        26717: Gain("极本溯源", attributes=dict(tank_buff_level=3))
    },
    {
        6895: Gain("妙镜惊寂")
    },
    {
        6766: Gain("斩火"),
    },
    {
        25166: Gain("净体不畏", buff_ids=[30644, 30645], skill_ids=[26708, 26709])
    },
    {
        25355: Gain("怜世人", buff_ids=[18222])
    },
    {
        14678: Gain("圣浴明心")
    }
]
