from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        20333: Gain("江汉", recipes=[(5426, 1)])
    },
    {
        20335: Gain("扶桑", recipes=[(4694, 1)]),
        20716: Gain("苍梧", recipes=[(4724, 1)]),
        30504: Gain("潮音", skill_ids=[30506])
    },
    {
        25267: Gain("驾鸾"),
        20746: Gain("羽彰", buff_ids=[13560])
    },
    {
        20348: Gain("清源", buff_ids=[29344]),
        32592: Gain("倾波", skill_ids=[32593])
    },
    {
        38669: Gain("青冥", dot_ids=[29350], skill_ids=[38675])
    },
    {
        38668: Gain("游仙", buff_ids=[14083])
    },
    {
        38670: Gain("鸿轨", buff_ids=[29348]),
        20694: Gain("凝气")
    },
    {
        20351: Gain("藏锋"),
        32488: Gain("海碧")
    },
    {
        21293: Gain("溯徊", skill_ids=[30503])
    },
    {
        38667: Gain("驰行", buff_ids=[14321])
    },
    {
        20747: Gain("梦悠", buff_ids=[13966], attributes=dict(all_shield_ignore=307))
    },
    {
        32594: Gain("怒翼", skill_ids=[32595])
    }
]
