from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        28371: Gain("血影留痕", skill_ids=[30894]),
        6490: Gain("天魔蚀肌", recipes=[(1219, 1)]),
        6491: Gain("毒手尊拳", recipes=[(1220, 1)])
    },
    {
        6493: Gain("天风汲雨", skill_ids=[30727])
    },
    {
        6495: Gain("弩击急骤", buff_ids=[6105])
    },
    {
        30921: Gain("擘两分星", buff_ids=[23081, 23082])
    },
    {
        40275: Gain("天罗地网", recipes=[(5920, 1)])
    },
    {
        27267: Gain("神威穿彻"),
        6451: Gain("聚精凝神", buff_ids=[8210]),
        6778: Gain("神机千算", recipes=[(2372, 1)])
    },
    {
        30721: Gain("巧夺天工"),
        18249: Gain("化血迷心", dot_ids=[14611], skill_ids=[21266])
    },
    {
        14857: Gain("雷甲三铉", buff_ids=[13165, 27405]),
        33134: Gain("杀机断魂", buff_ids=[-24668, 24669, 16234, 16235, 16236], skill_ids=list(range(33142, 33145 + 1)))
    },
    {
        6508: Gain("千机不殆", recipes=[(1223, 1), (5830, 1)]),
        6461: Gain("秋风散影", buff_ids=[9981])
    },
    {
        34679: Gain("雀引彀中", dot_ids=[29549], skill_ids=[38760]),
        24037: Gain("云奔雨骤", skill_ids=[26900, 26901])
    },
    {
        14856: Gain("曙色催寒", buff_ids=[10005], skill_ids=[15049])
    },
    {
        30723: Gain("千机连环"),
        18675: Gain("千秋万劫", skill_ids=[18677, 28441, 29687])
    }
]
