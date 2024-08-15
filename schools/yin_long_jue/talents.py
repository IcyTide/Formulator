from typing import Dict

from base.attribute import Attribute
from base.gain import Gain
from base.recipe import DamageAdditionRecipe, MoveStateDamageAdditionRecipe


class 王师(Gain):
    def add_attribute(self, attribute: Attribute):
        attribute.agility_gain += 102

    def sub_attribute(self, attribute: Attribute):
        attribute.agility_gain -= 102


TALENTS: Dict[int, Gain] = {
    22557: Gain("星旗"),
    22560: Gain("秋霁"),
    22562: Gain("雪覆"),
    26760: Gain("遗恨"),
    22586: Gain("折意"),
    22571: Gain("风骨"),
    23309: Gain("北阙"),
    22575: Gain("渊岳", [DamageAdditionRecipe(410, 22327, 22327)]),
    22579: Gain("玄肃", [MoveStateDamageAdditionRecipe(307, 22320, 22320)]),
    29166: Gain("飞刃回转"),
    22583: Gain("王师", [王师()]),
    22593: Gain("百节"),
    22587: Gain("忘断"),
    22596: Gain("徵逐"),
    22603: Gain("青山共我"),
    30849: Gain("孤路")
}

TALENT_CHOICES = [
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
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
