from typing import Dict

from base.gain import Gains
from base.recipe import PhysicalCriticalRecipe

TALENT_GAINS: Dict[int, Gains] = {
    5953: Gains("淘尽", [PhysicalCriticalRecipe((1000, 102), 1600, 1600)]),
    5954: Gains("清风", [PhysicalCriticalRecipe((1000, 102), 1593, 1593)]),
    5952: Gains("岱宗"),
    18682: Gains("景行"),
    5964: Gains("造化"),
    5957: Gains("怜光"),
    6545: Gains("层云"),
    30862: Gains("山倾"),
    6534: Gains("雾锁"),
    6548: Gains("碧归"),
    14605: Gains("如风"),
    25070: Gains("飞来闻踪")
}

TALENTS = [
    [5953],
    [5954],
    [5952],
    [18682],
    [5964],
    [5957],
    [6545],
    [30862],
    [6534],
    [6548],
    [14605],
    [25070],
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
