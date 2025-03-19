from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        5974: Gain("血泪成悦"),
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
        25166: Gain("净体不畏")
    },
    {
        17567: Gain("用晦而明", buff_ids=[-12575])},
    {
        5979: Gain("天地诛戮")
    },
    {
        38526: Gain("降灵尊")
    },
    {
        34347: Gain("明赦尊谕")
    },
    {
        37337: Gain("崇光斩恶")
    }
]
