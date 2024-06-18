from typing import Dict

from base.buff import Buff
from base.gain import Gain
from base.recipe import PhysicalCriticalRecipe
from base.talent import Talent


class 杀机断魂(Gain):
    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-24668].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-24668].activate = False


TALENT_GAINS: Dict[int, Talent] = {
    28371: Talent("血影留痕"),
    6493: Talent("天风汲雨"),
    6495: Talent("弩击急骤"),
    30921: Talent("擘两分星"),
    6441: Talent("流星赶月", [PhysicalCriticalRecipe((1000, 100), 3093, 3093)]),
    6451: Talent("聚精凝神"),
    18249: Talent("化血迷心"),
    33134: Talent("杀机断魂", [杀机断魂()]),
    6461: Talent("秋风散影"),
    34679: Talent("雀引彀中"),
    37327: Talent("云合影从"),
    14856: Talent("曙色催寒"),
    32742: Talent("诡鉴冥微")
}

TALENTS = [
    [28371],
    [6493],
    [6495],
    [30921],
    [6441],
    [6451],
    [18249],
    [33134],
    [6461],
    [34679, 37327],
    [14856],
    [32742]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
