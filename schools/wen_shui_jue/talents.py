from typing import Dict

from base.gain import Gain
from base.skill import Skill


class 淘尽(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2896].skill_critical_strike += 1000
        skills[2896].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2896].skill_critical_strike -= 1000
        skills[2896].skill_critical_power -= 102


class 清风(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (1594, 1595, 18317):
            skills[skill_id].skill_critical_strike += 1000
            skills[skill_id].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (1594, 1595, 18317):
            skills[skill_id].skill_critical_strike -= 1000
            skills[skill_id].skill_critical_power -= 102


TALENT_GAINS: Dict[int, Gain] = {
    5953: 淘尽("淘尽"),
    5954: 清风("清风"),
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
