from typing import Dict

from base.gain import Gain
from base.skill import Skill


class 流星赶月(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[3228].skill_critical_strike += 1000
        skills[3228].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[3228].skill_critical_strike -= 1000
        skills[3228].skill_critical_power -= 102


class 疾根(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[27560].tick += 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[27560].tick -= 1


TALENT_GAINS: Dict[int, Gain] = {
    28371: Gain("血影留痕"),
    6493: Gain("天风汲雨"),
    6495: Gain("弩击急骤"),
    30921: Gain("擘两分星"),
    37326: 流星赶月("流星赶月"),
    6451: Gain("聚精凝神"),
    18249: Gain("化血迷心"),
    33134: Gain("杀机断魂"),
    6461: Gain("秋风散影"),
    37327: Gain("云合影从"),
    14856: Gain("曙色催寒"),
    32742: Gain("诡鉴冥微"),
}

TALENTS = [
    [28371],
    [6493],
    [6495],
    [30921],
    [37326],
    [6451],
    [18249],
    [33134],
    [6461],
    [37327],
    [14856],
    [32742]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
