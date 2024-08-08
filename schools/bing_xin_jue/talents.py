from typing import Dict

from base.recipe import DamageAdditionRecipe, MagicalCriticalRecipe
from base.talent import Talent

TALENT_GAINS: Dict[int, Talent] = {
    6569: Talent("明妃"),
    5849: Talent("青梅嗅", [MagicalCriticalRecipe((1000, 102), 0, 2707)]),
    5869: Talent("惊寒", [DamageAdditionRecipe(154, skill_id, skill_id) for skill_id in (561, 553)]),
    5868: Talent("千里冰封", [
        MagicalCriticalRecipe((1000, 102), skill_id, skill_recipe)
        for skill_id, skill_recipe in ((2716, 2716), (6207, 0), (9346, 0))
    ]),
    5852: Talent("新妆"),
    37316: Talent("芳姿畅音"),
    5864: Talent("枕上"),
    23935: Talent("广陵月"),
    34604: Talent("流玉"),
    22732: Talent("钗燕"),
    24995: Talent("盈袖"),
    24996: Talent("化冰"),
    14934: Talent("夜天"),
    23457: Talent("琼宵"),
    34603: Talent("凝华"),
    14715: Talent("轻妒"),

    100585: Talent("红袖"),
    100586: Talent("弦曲"),
    100588: Talent("筝曲"),
    100598: Talent("合璧知意")
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
