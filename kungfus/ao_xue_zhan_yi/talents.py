from typing import Dict, List

from base.buff import Buff
from base.gain import Gain
from base.skill import Skill


class 战心(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[423].pre_buffs[-26008] = {1: 1}
        skills[702].post_buffs[-1] = {1: 3}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[423].pre_buffs.pop(-26008)
        skills[702].post_buffs.pop(-1)


class 虎贲(Gain):
    @staticmethod
    def begin_effect(parser):
        parser.current_kungfu.skills[18773].post_buffs[-1] = {1: -3}

    @staticmethod
    def end_effect(parser):
        parser.current_kungfu.skills[18773].post_buffs[-1] = {1: 0}

    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[28169].begin_effects.append(self.begin_effect)
        buffs[28169].end_effects.append(self.end_effect)

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[28169].begin_effects.remove(self.begin_effect)
        buffs[28169].end_effects.remove(self.end_effect)


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            18487: Gain("百折"),
            5656: Gain("封侯", recipes=[(4038, 3)]),
            5657: Gain("扬戈", recipes=[(1224, 1)])
        },
        {
            5660: Gain("神勇", recipes=[(1225, 1)])
        },
        {
            5659: Gain("大漠"),
            18602: Gain("骁勇", recipes=[(recipe_id, 1) for recipe_id in (4686, 4687, 4688, 4689)])
        },
        {
            24896: Gain("龙驭"),
            18226: Gain("击水", recipes=[(recipe_id, -1) for recipe_id in (-132, -153)])
        },
        {
            14824: Gain("驰骋")
        },
        {
            6511: Gain("牧云")
        },
        {
            5666: Gain("风虎", buff_ids=[-12608])
        },
        {
            6781: 战心("战心")
        },
        {
            6524: Gain("破楼兰"),
            2628: Gain("渊")
        },
        {
            5678: Gain("夜征")
        },
        {
            15001: Gain("龙血")
        },
        {
            6517: 虎贲("虎贲")
        }
    ],
    1: []
}
