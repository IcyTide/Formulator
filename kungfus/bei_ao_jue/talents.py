from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


class 斩纷(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in range(16615, 16619 + 1):
            skills[skill_id].pre_buffs[19510] = {1: 1}
        for skill_id in range(16920, 16925 + 1):
            skills[skill_id].pre_buffs[19510] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in range(16615, 16619 + 1):
            skills[skill_id].pre_buffs.pop(19510)
        for skill_id in range(16920, 16925 + 1):
            skills[skill_id].pre_buffs.pop(19510)


TALENTS: List[Dict[int, Gain]] = [
    {
        16691: Gain("龙息")
    },
    {
        16847: Gain("归酣"),
        16816: Gain("碎影")
    },
    {
        26904: Gain("冥鼓", recipes=[(2510, 1), (2511, 1)])
    },
    {
        16728: Gain("星火", attributes=dict(strength_gain=102, strain_gain=307)),
    },
    {
        16724: Gain("击瑕")
    },
    {
        37982: Gain("临江")
    },
    {
        16733: 斩纷("斩纷")
    },
    {
        16779: Gain("化蛟")
    },
    {
        38535: Gain("楚歌")
    },
    {
        17056: Gain("绝期", recipes=[(4319, 1), (2833, 1)])
    },
    {
        16977: Gain("冷川")
    },
    {
        21858: Gain("斩狂枭")
    }
]
