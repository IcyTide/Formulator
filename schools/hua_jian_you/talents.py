from typing import Dict

from base.buff import Buff
from base.gain import Gain
from base.skill import Skill


class 烟霞(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[14941].skill_critical_strike += 1000
        skills[14941].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[14941].skill_critical_strike -= 1000
        skills[14941].skill_critical_power -= 102


class 青冠(Gain):
    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-32489].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-32489].activate = False


TALENT_GAINS: Dict[int, Gain] = {
    5756: 烟霞("烟霞"),
    32489: 青冠("青冠"),
    17510: Gain("倚天"),
    37267:  Gain("墨海临源"),
    21744:  Gain("折花"),
    32477: Gain("雪中行"),
    16855:  Gain("清流"),
    26692: Gain("钟灵"),
    6682: Gain("流离"),
    32480: Gain("雪弃"),
    32469: Gain("焚玉"),
    14643:  Gain("涓流")
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
    [32469],
    [14643]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
