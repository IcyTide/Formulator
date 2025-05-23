from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


TALENTS: List[Dict[int, Gain]] = [
    {
        38631: Gain("连茹")
    },
    {
        28344: Gain("鸩羽", recipes=[(2549, 1)])
    },
    {
        40211: Gain("往馥", skill_ids=[40212])
    },
    {
        29498: Gain("灵荆")
    },
    {
        39661: Gain("逆势")
    },
    {
        30507: Gain("渌波"),
        40194: Gain("六微", skill_ids=[40208])
    },
    {
        28413: Gain("相使", buff_ids=[20680])
    },
    {
        28419: Gain("凄骨", buff_ids=[30352])
    },
    {
        38965: Gain("紫伏", skill_ids=[28434])
    },
    {
        36067: Gain("香繁饮露")
    },
    {
        28443: Gain("甘遂")
    },
    {
        28426: Gain("养荣", buff_ids=[20699])
    }
]
