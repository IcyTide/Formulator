from typing import Dict

from base.gain import Gain

TALENTS: Dict[int, Gain] = {
    28371: Gain("血影留痕"),
    6493: Gain("天风汲雨"),
    6495: Gain("弩击急骤"),
    6506: Gain("千机之威"),
    30921: Gain("擘两分星"),
    6441: Gain("流星赶月", recipes=[(1204, 1)]),
    37326: Gain("确固不拔"),
    6451: Gain("聚精凝神"),
    18249: Gain("化血迷心"),
    33134: Gain("杀机断魂", buff_ids=[-24668]),
    14857: Gain("雷甲三铉"),
    6461: Gain("秋风散影"),
    34679: Gain("雀引彀中"),
    37327: Gain("云合影从"),
    14856: Gain("曙色催寒"),
    32742: Gain("诡鉴冥微"),
    18675: Gain("千秋万劫")
}

TALENT_CHOICES = [
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
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
