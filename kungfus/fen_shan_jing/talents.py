from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        13317: Gain("赴敌", recipes=[(5804, 1), (5805, 1)])
    },
    {
        13090: Gain("绝返"),
        37558: Gain("登锋", recipes=[(5562, 1)])
    },
    {
        13087: Gain("分野", recipes=[(1823, 1)])
    },
    {
        13109: Gain("北漠"),
        21281: Gain("嗜血")
    },
    {
        22897: Gain("锋鸣")
    },
    {
        37239: Gain("麾远", recipes=[(5821, 1)]),
        37559: Gain("履刃")
    },
    {
        34912: Gain("业火麟光")
    },
    {
        13126: Gain("恋战", attributes=dict(all_damage_addition=205))
    },
    {
        36058: Gain("援戈")
    },
    {
        13304: Gain("愤恨"),
        36205: Gain("惊涌")
    },
    {
        14838: Gain("刀煞", recipes=[(5745, 1), (5746, 1)])
    },
    {
        30769: Gain("阵云结晦")
    }
]
