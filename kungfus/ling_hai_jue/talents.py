from typing import Dict, List

from base.gain import Gain

TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            20333: Gain("江汉", recipes=[(5426, 1)]),
            20324: Gain("海隅", recipes=[(4691, 1)]),
            20756: Gain("凌霄", recipes=[(4762, 1)])
        },
        {
            20335: Gain("扶桑", recipes=[(4694, 1)])
        },
        {
            20746: Gain("羽彰")
        },
        {
            20348: Gain("清源")
        },
        {
            30912: Gain("游仙")
        },
        {
            25272: Gain("青冥")
        },
        {
            20751: Gain("鸿轨")
        },
        {
            25270: Gain("烟涛"),
            20730: Gain("怅归")
        },
        {
            21293: Gain("溯徊"),
            32476: Gain("风驰")
        },
        {
            20374: Gain("驰行"),
            20758: Gain("神降", buff_ids=[-22585])
        },
        {
            20747: Gain("梦悠", attributes=dict(all_shield_ignore=307))
        },
        {
            20701: Gain("濯流", recipes=[(3270, 1)])
        }
    ],
    1: [
        {
            101166: Gain("鹏程")
        },
        {
            101168: Gain("浩渺")
        },
        {
            101170: Gain("海溟")
        },
        {
            102111: Gain("澹然若海")
        }
    ]
}
