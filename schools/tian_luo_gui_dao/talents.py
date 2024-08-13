from typing import Dict

from base.buff import Buff
from base.gain import Gain, Gains
from base.recipe import PhysicalCriticalRecipe


class 杀机断魂(Gain):
    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-24668].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-24668].activate = False


TALENT_GAINS: Dict[int, Gains] = {
    28371: Gains("血影留痕"),
    6493: Gains("天风汲雨"),
    6495: Gains("弩击急骤"),
    6506: Gains("千机之威"),
    30921: Gains("擘两分星"),
    6441: Gains("流星赶月", [PhysicalCriticalRecipe((1000, 100), 3093, 3093)]),
    37326: Gains("确固不拔"),
    6451: Gains("聚精凝神"),
    18249: Gains("化血迷心"),
    33134: Gains("杀机断魂", [杀机断魂()]),
    14857: Gains("雷甲三铉"),
    6461: Gains("秋风散影"),
    34679: Gains("雀引彀中"),
    37327: Gains("云合影从"),
    14856: Gains("曙色催寒"),
    32742: Gains("诡鉴冥微"),
    18675: Gains("千秋万劫")
}

TALENTS = [
    [28371],
    [6493],
    [6495],
    [30921, 6506],
    [6441, 37326],
    [6451],
    [18249],
    [33134, 14857],
    [6461],
    [34679, 37327],
    [14856],
    [32742, 18675]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
