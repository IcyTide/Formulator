from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


class 明法(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (17641, 17642):
            skills[skill_id].post_target_buffs = {12479: {1: 1}}
        for skill_id in (3848, 3849, 3850):
            skills[skill_id].post_target_buffs[12479] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (17641, 17642):
            skills[skill_id].post_target_buffs = {890: {1: 1}}
        for skill_id in (3848, 3849, 3850):
            skills[skill_id].post_target_buffs.pop(12479)


TALENTS: List[Dict[int, Gain]] = [
    {
        5896: Gain("涅果", recipes=[(959, 3)]),
        6589: 明法("明法")
    },
    {
        5910: Gain("幻身")
    },
    {
        5915: Gain("身意", recipes=[(2299, 1)])
    },
    {
        37455: Gain("布泽")
    },
    {
        5913: Gain("降魔渡厄")
    },
    {
        17730: Gain("金刚怒目")
    },
    {
        6590: Gain("净果")
    },
    {
        6586: Gain("三生"),
        24884: Gain("我闻", recipes=[(5157, 1)])
    },
    {
        6596: Gain("众嗔")
    },
    {
        38957: Gain("华香")
    },
    {
        32648: Gain("金刚日轮")
    },
    {
        32651: Gain("业因")
    }
]
