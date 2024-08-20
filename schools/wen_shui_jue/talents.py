from typing import Dict

from base.gain import Gain

TALENTS: Dict[int, Gain] = {
    5953: Gain("淘尽", recipes=[(1235, 1)]),
    5954: Gain("清风", recipes=[(1236, 1)]),
    5952: Gain("岱宗"),
    18682: Gain("景行"),
    5964: Gain("造化"),
    5957: Gain("怜光"),
    6545: Gain("层云"),
    30862: Gain("山倾"),
    6534: Gain("雾锁"),
    6548: Gain("碧归"),
    14605: Gain("如风"),
    25070: Gain("飞来闻踪")
}

TALENT_CHOICES = [
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
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
