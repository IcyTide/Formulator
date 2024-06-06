from typing import Dict

from base.talent import Talent
from base.recipe import PhysicalCriticalRecipe


TALENT_GAINS: Dict[int, Talent] = {
    5953: Talent("淘尽", [PhysicalCriticalRecipe((1000, 102), 1600, 1600)]),
    5954: Talent("清风", [PhysicalCriticalRecipe((1000, 102), 1593, 1593)]),
    5952: Talent("岱宗"),
    18682: Talent("景行"),
    5964: Talent("造化"),
    5957: Talent("怜光"),
    6545: Talent("层云"),
    30862: Talent("山倾"),
    6534: Talent("雾锁"),
    6548: Talent("碧归"),
    14605: Talent("如风"),
    25070: Talent("飞来闻踪")
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
TALENT_DECODER = {talent_id: talent.talent_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
