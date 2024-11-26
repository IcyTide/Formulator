from typing import Dict, List

from base.gain import Gain

TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            13317: Gain("刀魂")
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
            22897: Gain("锋鸣"),
            13086: Gain("残楼")
        },
        {
            37239: Gain("麾远"),
            37559: Gain("履刃"),
            32618: Gain("血誓")
        },
        {
            34912: Gain("业火麟光")
        },
        {
            13126: Gain("恋战", attributes=dict(all_damage_addition=205)),
            25203: Gain("扶阵"),
            28490: Gain("过涯")
        },
        {
            36058: Gain("援戈"),
            13366: Gain("从容")
        },
        {
            13304: Gain("愤恨"),
            36205: Gain("惊涌")
        },
        {
            14838: Gain("刀煞", recipes=[(5745, 1), (5746, 1)])
        },
        {
            30769: Gain("阵云结晦"),
            32619: Gain("祭血关山")
        }
    ],
    1: [
        {
            101245: Gain("血狱", attributes=dict(physical_critical_strike_rate=500))
        },
        {
            101248: Gain("陷阵")
        },
        {
            101249: Gain("碎甲")
        },
        {
            102040: Gain("祭血关山")
        }
    ]
}
