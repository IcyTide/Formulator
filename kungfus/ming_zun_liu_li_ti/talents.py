from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = {
    0: [
        {
            5974: Gain("血泪成悦")
        },
        {
            18279: Gain("净身明礼", recipes=[(5149, 1), (5150, 1)])
        },
        {
            6745: Gain("寂灭")
        },
        {
            6751: Gain("无明业火")
        },
        {
            6898: Gain("超凡入圣")
        },
        {
            14698: Gain("驱夷逐法")
        },
        {
            26717: Gain("极本溯源", attributes=dict(tank_buff_level=3))
        },
        {
            25160: Gain("五明乐见")
        },
        {
            21835: Gain("孤月无心"),
        },
        {
            25166: Gain("净体不畏")
        },
        {
            6722: Gain("无量妙境")
        },
        {
            25175: Gain("微妙风")
        }
    ]
}
