from typing import Dict

from base.gain import Gain

TALENTS: Dict[int, Gain] = {
    6569: Gain("明妃"),
    5848: Gain("伤春", recipes=[(2893, 1)]),
    5849: Gain("青梅嗅", recipes=[(1246, 1)]),
    5869: Gain("惊寒", recipes=[(1488, 1), (4478, 1)]),
    5868: Gain("千里冰封", recipes=[(2014, 1), (2015, 1), (2016, 1)]),
    5852: Gain("新妆"),
    37316: Gain("芳姿畅音"),
    5864: Gain("枕上"),
    23935: Gain("广陵月"),
    34604: Gain("流玉"),
    22732: Gain("钗燕"),
    24995: Gain("盈袖"),
    24996: Gain("化冰"),
    14934: Gain("夜天"),
    23457: Gain("琼宵"),
    34603: Gain("凝华"),
    14715: Gain("轻妒"),

    100585: Gain("红袖"),
    100586: Gain("弦曲"),
    100588: Gain("筝曲"),
    100377: Gain("霜天剑泠"),
    100598: Gain("合璧知意")
}

TALENT_CHOICES = [
    [5848, 6569, 5849, 100585],
    [5869, 5868, 100586],
    [5852, 100588],
    [37316, 100598, 100377],
    [5864],
    [23935],
    [34604],
    [22732],
    [24995],
    [24996],
    [14934, 23457],
    [34603, 14715]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
