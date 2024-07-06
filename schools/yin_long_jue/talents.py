from typing import Dict

from base.attribute import Attribute
from base.gain import Gain
from base.recipe import DamageAdditionRecipe, MoveStateDamageAdditionRecipe
from base.talent import Talent


class 王师(Gain):
    def add_attribute(self, attribute: Attribute):
        attribute.agility_gain += 102

    def sub_attribute(self, attribute: Attribute):
        attribute.agility_gain -= 102


TALENT_GAINS: Dict[int, Talent] = {
    22557: Talent("星旗"),
    22560: Talent("秋霁"),
    22562: Talent("雪覆"),
    26760: Talent("遗恨"),
    22586: Talent("折意"),
    22571: Talent("风骨"),
    23309: Talent("北阙"),
    22575: Talent("渊岳", [DamageAdditionRecipe(410, 22327, 22327)]),
    22579: Talent("玄肃", [MoveStateDamageAdditionRecipe(256, 22320, 22320)]),
    29166: Talent("飞刃回转"),
    22583: Talent("王师", [王师()]),
    22593: Talent("百节"),
    22587: Talent("忘断"),
    22596: Talent("徵逐"),
    22603: Talent("青山共我"),
    30849: Talent("孤路")
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
