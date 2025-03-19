from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


class 龙驭(Gain):
    @staticmethod
    def pre_effect(parser):
        if parser.current_buff_stacks[21638] and (parser.current_buff_stacks[244] or parser.current_buff_stacks[26444]):
            parser.refresh_target_buff(-21638, 1)

    @staticmethod
    def post_effect(parser):
        if parser.current_buff_stacks[21638] and (parser.current_buff_stacks[244] or parser.current_buff_stacks[26444]):
            parser.clear_target_buff(-21638, 1)

    def add_skills(self, skills: Dict[int, Skill]):
        skills[18773].pre_effects.append(self.pre_effect)
        skills[18773].post_effects.append(self.post_effect)

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[18773].pre_effects.remove(self.pre_effect)
        skills[18773].post_effects.remove(self.post_effect)


TALENTS: List[Dict[int, Gain]] = [
    {
        5656: Gain("封侯", recipes=[(5649, 1)])
    },
    {
        5660: Gain("神勇", recipes=[(1225, 1)])
    },
    {
        5659: Gain("大漠")
    },
    {
        24896: 龙驭("龙驭")
    },
    {
        14824: Gain("驰骋")
    },
    {
        6511: Gain("牧云")
    },
    {
        5666: Gain("风虎")
    },
    {
        6781: Gain("战心")
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
        6517: Gain("虎贲")
    }
]
