from typing import Dict, List

from base.gain import Gain

TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            5807: Gain("心固", recipes=[(638, 3)])
        },
        {
            32407: Gain("环月")
        },
        {
            5800: Gain("白虹"),
            357: Gain("化三清")
        },
        {
            5818: Gain("无意", recipes=[(2263, 1)]),
            21812: Gain("云中剑")
        },
        {
            17742: Gain("风逝")
        },
        {
            5821: Gain("叠刃")
        },
        {
            6481: Gain("雾外江山"),
            21725: Gain("长生")
        },
        {
            24962: Gain("裂云"),
            14598: Gain("若水")
        },
        {
            18799: Gain("故长")
        },
        {
            34656: Gain("剑入")
        },
        {
            14832: Gain("虚极", recipes=[(4583, 1), (5173, 1)])
        },
        {
            14833: Gain("玄门")
        }
    ],
    1: [
        {
            100448: Gain("周行")
        },
        {
            100449: Gain("神灵")
        },
        {
            100451: Gain("固强")
        },
        {
            100015: Gain("行剑千风")
        }
    ]
}
