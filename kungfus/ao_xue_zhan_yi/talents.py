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
        5659: Gain("大漠", skill_ids=[37618])
    },
    {
        18226: Gain("击水", dot_ids=[12461], skill_ids=[401, 36568],
                    recipes=[(recipe_id, 1) for recipe_id in (-132, -153)]),
        24896: 龙驭("龙驭", buff_ids=[244, 26444, 21638, -21638])
    },
    {
        14824: Gain("驰骋", skill_ids=[24898])
    },
    {
        6511: Gain("牧云", buff_ids=[7671])
    },
    {
        5666: Gain("风虎", buff_ids=[12608])
    },
    {
        6781: Gain("战心", buff_ids=[26008])
    },
    {
        6524: Gain("破楼兰", skill_ids=[6525, 6526]),
        2628: Gain("渊", buff_ids=[2779])
    },
    {
        5678: Gain("夜征")
    },
    {
        15001: Gain("龙血", skill_ids=[15002])
    },
    {
        6517: Gain("虎贲")
    }
]
