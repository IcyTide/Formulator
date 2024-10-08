from typing import Dict, List

from base.gain import Gain


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            13317: Gain("刀魂")
        },
        {
            13090: Gain("绝返")
        },
        {
            13087: Gain("分野", recipes=[(1823, 1)])
        },
        {
            21281: Gain("血魄"),
            13109: Gain("北漠")
        },
        {
            22897: Gain("锋鸣")
        },
        {
            37239: Gain("麾远")
        },
        {
            34912: Gain("业火麟光")
        },
        {
            13126: Gain("恋战", attributes=dict(all_damage_addition=205)),
            25203: Gain("扶阵")
        },
        {
            36058: Gain("援戈")
        },
        {
            36205: Gain("惊涌")
        },
        {
            14838: Gain("蔑视")
        },
        {
            30769: Gain("阵云结晦"),
            32619: Gain("祭血关山")
        }
    ]
}
