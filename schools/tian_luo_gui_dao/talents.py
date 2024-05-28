from typing import Dict

from base.buff import Buff
from base.gain import Gain
from base.skill import Skill


class 流星赶月(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[3228].skill_critical_strike += 1000
        skills[3228].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[3228].skill_critical_strike -= 1000
        skills[3228].skill_critical_power -= 102


class 杀机断魂(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (36502, 30894, 30727):
            skills[skill_id].skill_damage_addition += 103 * 2 * 3
        skills[3313].skill_damage_addition += 103 * 3

    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-24668].activate = True

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (36502, 30894, 30727):
            skills[skill_id].skill_damage_addition -= 103 * 2 * 3
        skills[3313].skill_damage_addition -= 103 * 3

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-24668].activate = False


TALENT_GAINS: Dict[int, Gain] = {
    28371: Gain("血影留痕"),
    6493: Gain("天风汲雨"),
    6495: Gain("弩击急骤"),
    30921: Gain("擘两分星"),
    6441: 流星赶月("流星赶月"),
    6451: Gain("聚精凝神"),
    18249: Gain("化血迷心"),
    33134: 杀机断魂("杀机断魂"),
    6461: Gain("秋风散影"),
    34679: Gain("雀引彀中"),
    37327: Gain("云合影从"),
    14856: Gain("曙色催寒"),
    32742: Gain("诡鉴冥微"),
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
