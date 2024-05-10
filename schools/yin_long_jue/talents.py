from typing import Dict

from base.attribute import Attribute
from base.gain import Gain
from base.skill import Skill


class 渊岳(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (22604, 22605, 36267, 36268):
            skills[skill_id].skill_damage_addition += 410

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (22604, 22605, 36267, 36268):
            skills[skill_id].skill_damage_addition -= 410


class 玄肃(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (22490, 22554, 36265, 36266):
            skills[skill_id].extra_damage_addition += 256

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (22490, 22554, 36265, 36266):
            skills[skill_id].extra_damage_addition -= 256


class 王师(Gain):
    def add_attribute(self, attribute: Attribute):
        attribute.agility_gain += 102

    def sub_attribute(self, attribute: Attribute):
        attribute.agility_gain -= 102


TALENT_GAINS: Dict[int, Gain] = {
    22557: Gain("星旗"),
    22560: Gain("秋霁"),
    22562: Gain("雪覆"),
    26760: Gain("遗恨"),
    22586: Gain("折意"),
    22571: Gain("风骨"),
    23309: Gain("北阙"),
    22575: 渊岳("渊岳"),
    22579: 玄肃("玄肃"),
    29166: Gain("飞刃回转"),
    22583: 王师("王师"),
    22593: Gain("百节"),
    22587: Gain("忘断"),
    22596: Gain("徵逐"),
    22603: Gain("青山共我"),
    30849: Gain("孤路")
}

TALENTS = [
    [22557, 22560],
    [22562],
    [26760, 22586],
    [22571],
    [23309],
    [22575],
    [22579],
    [29166, 22583],
    [22593],
    [22587],
    [22596],
    [22603, 30849]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
