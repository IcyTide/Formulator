from typing import Dict

from base.gain import Gains
from base.recipe import DamageAdditionRecipe, MagicalCriticalRecipe

TALENT_GAINS: Dict[int, Gains] = {
    6569: Gains("明妃"),
    5849: Gains("青梅嗅", [MagicalCriticalRecipe((1000, 102), 0, 2707)]),
    5869: Gains("惊寒", [DamageAdditionRecipe(154, skill_id, skill_id) for skill_id in (561, 553)]),
    5868: Gains("千里冰封", [
        MagicalCriticalRecipe((1000, 102), skill_id, skill_recipe)
        for skill_id, skill_recipe in ((2716, 2716), (6207, 0), (9346, 0))
    ]),
    5852: Gains("新妆"),
    37316: Gains("芳姿畅音"),
    5864: Gains("枕上"),
    23935: Gains("广陵月"),
    34604: Gains("流玉"),
    22732: Gains("钗燕"),
    24995: Gains("盈袖"),
    24996: Gains("化冰"),
    14934: Gains("夜天"),
    23457: Gains("琼宵"),
    34603: Gains("凝华"),
    14715: Gains("轻妒"),

    100585: Gains("红袖"),
    100586: Gains("弦曲"),
    100588: Gains("筝曲"),
    100598: Gains("合璧知意")
}

TALENTS = [
    [6569, 5849, 100585],
    [5869, 5868, 100586],
    [5852, 100588],
    [37316, 100598],
    [5864],
    [23935],
    [34604],
    [22732],
    [24995],
    [24996],
    [14934, 23457],
    [34603, 14715]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
