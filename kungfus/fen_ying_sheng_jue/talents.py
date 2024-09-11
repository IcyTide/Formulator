from typing import Dict, List

from base.gain import Gain

TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            5972: Gain("腾焰飞芒", recipes=[(1314, 1), (1315, 1)])
        },
        {
            18279: Gain("净身明礼", recipes=[(5149, 1), (5150, 1)])
        },
        {
            22888: Gain("诛邪镇魔")
        },
        {
            6717: Gain("无明业火")
        },
        {
            34383: Gain("明光恒照")
        },
        {
            34395: Gain("日月同辉")
        },
        {
            34372: Gain("靡业报劫")
        },
        {
            17567: Gain("用晦而明", buff_ids=[-12575])},
        {
            25166: Gain("净体不畏"),
            5979: Gain("天地诛戮")
        },
        {
            34378: Gain("降灵尊")
        },
        {
            34347: Gain("悬象著明")
        },
        {
            37337: Gain("崇光斩恶"),
            34370: Gain("日月齐光")
        }
    ],
    1: []
}
