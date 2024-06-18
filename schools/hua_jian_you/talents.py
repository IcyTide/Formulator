from typing import Dict

from base.buff import Buff
from base.gain import Gain
from base.recipe import MagicalCriticalRecipe
from base.talent import Talent


class 清流(Gain):
    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-12588].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-12588].activate = False


TALENT_GAINS: Dict[int, Talent] = {
    5756: Talent("烟霞", [MagicalCriticalRecipe((1000, 102), 179, 179)]),
    32489: Talent("青冠"),
    17510: Talent("倚天"),
    37267: Talent("墨海临源"),
    21744: Talent("折花"),
    32477: Talent("雪中行"),
    16855: Talent("清流", [清流()]),
    26692: Talent("钟灵"),
    6682: Talent("流离"),
    32480: Talent("雪弃"),
    32469: Talent("焚玉"),
    26669: Talent("故幽", [
        MagicalCriticalRecipe((1500, 154), skill_id, skill_recipe)
        for skill_id, skill_recipe in ((186, 186), (6134, 0), (6135, 0), (6136, 0), (0, 32409))
    ]),
    14643: Talent("涓流")
}

TALENTS = [
    [5756],
    [32489],
    [17510],
    [37267],
    [21744],
    [32477],
    [16855],
    [26692],
    [6682],
    [32480],
    [32469, 26669],
    [14643]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
