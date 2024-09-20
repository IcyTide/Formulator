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
            20348: Gain("清源"),
            20720: Gain("遥思", recipes=[(5390, 1)])
        },
        {
            26745: Gain("澄穆"),
            38669: Gain("青冥")
        },
        {
            38668: Gain("游仙")
        },
        {
            30502: Gain("惊潮"),
            38670: Gain("鸿轨")
        },
        {
            20351: Gain("藏锋"),
            25270: Gain("烟涛"),
        },
        {
            20730: Gain("怅归"),
            21293: Gain("溯徊"),
            32476: Gain("风驰")
        },
        {
            38667: Gain("驰行"),
            20758: Gain("神降", buff_ids=[-22585])
        },
        {
            20747: Gain("梦悠", attributes=dict(all_shield_ignore=307))
        },
        {
            32594: Gain("怒翼")
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
