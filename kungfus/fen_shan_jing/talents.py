from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        13317: Gain("赴敌", recipes=[(5804, 1), (5805, 1)])
    },
    {
        13090: Gain("绝返"),
        37558: Gain("登锋", skill_ids=[29187, 37600], recipes=[(5562, 1)])
    },
    {
        13087: Gain("分野", buff_ids=[17176], recipes=[(1823, 1)])
    },
    {
        13109: Gain("北漠", skill_ids=[13110, 13107, 13108]),
        21281: Gain("嗜血")
    },
    {
        22897: Gain("锋鸣", buff_ids=[14309])
    },
    {
        37239: Gain("麾远", skill_ids=[37253], recipes=[(5821, 1)]),
        37559: Gain("履刃", skill_ids=[37601, 37600])
    },
    {
        34912: Gain("业火麟光", skill_ids=[34674, 37448])
    },
    {
        36058: Gain("援戈", skill_ids=[36482, 36065])
    },
    {
        38969: Gain("血魄"),
        13126: Gain("恋战", attributes=dict(all_damage_addition=102))
    },
    {
        13304: Gain("愤恨", buff_ids=[8385]),
        36205: Gain("惊涌", buff_ids=[27161], skill_ids=[38890])
    },
    {
        14838: Gain("刀煞", recipes=[(5745, 1), (5746, 1)])
    },
    {
        30769: Gain("阵云结晦", skill_ids=[30925, 30926, 30857]),
        25213: Gain("断马摧城", skill_ids=[25215])
    }
]
