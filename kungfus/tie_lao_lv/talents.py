from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        402: Gain("定军", skill_ids=[402]),
    },
    {
        5688: Gain("龙痕")
    },
    {
        5659: Gain("大漠", skill_ids=[37618]),
        18602: Gain("骁勇", recipes=[(recipe_id, 1) for recipe_id in (4686, 4687, 4688, 4689)])
    },
    {
        18226: Gain("击水", dot_ids=[12461], skill_ids=[401, 36568],
                    recipes=[(recipe_id, 1) for recipe_id in (-132, -153)]),
        5695: Gain("望西京")
    },
    {
        5681: Gain("留侯")
    },
    {
        18238: Gain("掠如火")
    },
    {
        5702: Gain("踏北邙"),
        40300: Gain("振甲")
    },
    {
        14827: Gain("载戎")
    },
    {
        25354: Gain("崩决", buff_ids=[18222]),
        2628: Gain("渊", buff_ids=[2779])
    },
    {
        18239: Gain("昂如岳"),
        24895: Gain("疾雨", skill_ids=[24894]),
        18557: Gain("流电", skill_ids=[32979, 32980])
    },
    {
        6781: Gain("战心", buff_ids=[26008])
    },
    {
        15115: Gain("号令三军"),
        24841: Gain("力破万钧", skill_ids=[24843])
    }
]
