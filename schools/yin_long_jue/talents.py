from typing import Dict

from base.attribute import Attribute
from base.gain import Gain, Gains
from base.recipe import DamageAdditionRecipe, MoveStateDamageAdditionRecipe


class 王师(Gain):
    def add_attribute(self, attribute: Attribute):
        attribute.agility_gain += 102

    def sub_attribute(self, attribute: Attribute):
        attribute.agility_gain -= 102


TALENT_GAINS: Dict[int, Gains] = {
    22557: Gains("星旗"),
    22560: Gains("秋霁"),
    22562: Gains("雪覆"),
    26760: Gains("遗恨"),
    22586: Gains("折意"),
    22571: Gains("风骨"),
    23309: Gains("北阙"),
    22575: Gains("渊岳", [DamageAdditionRecipe(410, 22327, 22327)]),
    22579: Gains("玄肃", [MoveStateDamageAdditionRecipe(307, 22320, 22320)]),
    29166: Gains("飞刃回转"),
    22583: Gains("王师", [王师()]),
    22593: Gains("百节"),
    22587: Gains("忘断"),
    22596: Gains("徵逐"),
    22603: Gains("青山共我"),
    30849: Gains("孤路")
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
