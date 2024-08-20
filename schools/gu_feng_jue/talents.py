from typing import Dict

from base.gain import Gain

TALENTS: Dict[int, Gain] = {
    32450: Gain("渊冲", recipes=[(3011, 1)]),
    32580: Gain("戗风", recipes=[(5584, 1), (5585, 1), (5586, 1)]),
    32464: Gain("溃延"),
    32456: Gain("雨积"),
    32490: Gain("放皓", recipes=[(3023, 1)]),
    32492: Gain("电逝"),
    33027: Gain("威声"),
    32497: Gain("击懈", recipes=[(5588, 1)]),
    32500: Gain("承磊"),
    32502: Gain("滔天"),
    32457: Gain("镇机"),
    32512: Gain("界破"),
    32508: Gain("长溯"),
    32511: Gain("涣衍", recipes=[(-161, 1), (-162, 1)]),
    32513: Gain("涤瑕", recipes=[(3033, 1)]),
    32578: Gain("强膂", attributes=dict(strength_gain=102)),
    32493: Gain("流岚"),
    32452: Gain("聚疏"),
    36035: Gain("潋风"),
    32586: Gain("截辕"),

    101537: Gain("斩涛", attributes=dict(strength_gain=154)),
    101539: Gain("披靡"),
    101542: Gain("倒海"),
    101395: Gain("孤风破浪")
}

TALENT_CHOICES = [
    [32450, 101537],
    [32580, 101539],
    [32464, 32456, 101542],
    [32490, 101395],
    [32492, 33027],
    [32500, 32497],
    [32457, 32512, 32502],
    [32508],
    [32511],
    [32513, 32578],
    [32493, 32452],
    [36035, 32586]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
