from typing import Dict

from base.gain import Gain

TALENTS: Dict[int, Gain] = {
    22557: Gain("星旗"),
    22560: Gain("秋霁"),
    22562: Gain("雪覆"),
    26760: Gain("遗恨"),
    22586: Gain("折意"),
    22571: Gain("风骨"),
    23309: Gain("北阙"),
    22575: Gain("渊岳", recipes=[(4950, 1)]),
    22579: Gain("玄肃", recipes=[(4952, 1)]),
    29166: Gain("飞刃回转"),
    22583: Gain("王师", attributes=dict(agility_gain=102)),
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
