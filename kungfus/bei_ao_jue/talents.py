from typing import Dict

from base.gain import Gain
from base.skill import Skill
from kungfus.bei_ao_jue.skills import 项王击鼎秘章


class 含风(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        pass

    def sub_skills(self, skills: Dict[int, Skill]):
        pass


class 征踏(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id, skill in skills.items():
            if isinstance(skill, 项王击鼎秘章) or skill_id in [101108, 101109, 101110] + list(range(101256, 101260)):
                skill.pre_target_buffs[70188] = {10: 1}
                skill.post_target_buffs[70188] = {10: -1}

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id, skill in skills.items():
            if isinstance(skill, 项王击鼎秘章) or skill_id in [101108, 101109, 101110] + list(range(101256, 101260)):
                skill.pre_target_buffs[70188].pop(10)
                skill.post_target_buffs[70188].pop(10)


class 裁魂(Gain):
    @staticmethod
    def pre_effect(parser):
        if 70454 in parser.current_target_buff_stacks:
            parser.refresh_target_buff(70188, 20)

    @staticmethod
    def post_effect(parser):
        if 70454 in parser.current_target_buff_stacks:
            parser.refresh_target_buff(70188, 20, -1)

    def add_skills(self, skills: Dict[int, Skill]):
        skills[101080].pre_effects.append(self.pre_effect)
        skills[101080].post_effects.append(self.post_effect)
        skills[101198].post_target_buffs[70454] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[101080].pre_effects.remove(self.pre_effect)
        skills[101080].post_effects.remove(self.post_effect)
        skills[101198].post_target_buffs.pop(70454)


TALENTS: Dict[int, Gain] = {
    16691: Gain("龙息"),
    16847: Gain("归酣"),
    26904: Gain("冥鼓", recipes=[(2510, 1), (2511, 1)]),
    17042: Gain("阳关", recipes=[(4298, 1)]),
    16799: Gain("霜天"),
    25633: 含风("含风"),
    32857: Gain("见尘"),
    37982: Gain("临江"),
    17047: Gain("分疆"),
    25258: Gain("掠关"),
    16728: Gain("星火", attributes=dict(strength_gain=102)),
    34677: Gain("绝河", recipes=[(3251, 1)]),
    16737: Gain("楚歌"),
    17056: Gain("绝期", recipes=[(4319, 1), (2833, 1)]),
    16893: Gain("重烟"),
    21858: Gain("降麒式"),

    101296: 征踏("征踏"),
    101299: 裁魂("裁魂", ),
    101300: Gain("霸王"),
    101015: Gain("上将军印")
}

TALENT_CHOICES = [
    [16691, 101296],
    [16847, 101299],
    [26904, 17042, 101300],
    [16799, 101015],
    [25633],
    [32857, 37982],
    [17047],
    [25258, 16728, 34677],
    [16737],
    [17056],
    [16893],
    [21858]
]
