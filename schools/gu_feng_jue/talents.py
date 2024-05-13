from typing import Dict

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from base.skill import Skill


class 渊冲(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (32149, 32150, 32151):
            skills[skill_id].skill_critical_strike += 1000
            skills[skill_id].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (32149, 32150, 32151):
            skills[skill_id].skill_critical_strike -= 1000
            skills[skill_id].skill_critical_power -= 102


class 放皓(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[32602].skill_critical_strike += 1000
        skills[32602].skill_critical_power += 102

        skills[32603].skill_critical_strike += 2000
        skills[32603].skill_critical_power += 205

        skills[32604].skill_critical_strike += 3000
        skills[32604].skill_critical_power += 307

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[32602].skill_critical_strike -= 1000
        skills[32602].skill_critical_power -= 102

        skills[32603].skill_critical_strike -= 2000
        skills[32603].skill_critical_power -= 205

        skills[32604].skill_critical_strike -= 3000
        skills[32604].skill_critical_power -= 307


class 涣衍(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[24443].tick += 3

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[24443].tick -= 3


class 涤瑕(Gain):
    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-24222].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-24222].activate = False


TALENT_GAINS: Dict[int, Gain] = {
    32450: 渊冲("渊冲"),
    32580: Gain("戗风"),
    32464: Gain("溃延"),
    32490: 放皓("放皓"),
    32492: Gain("电逝"),
    32500: Gain("承磊"),
    32457: Gain("镇机"),
    32508: Gain("长溯"),
    32511: 涣衍("涣衍"),
    32513: 涤瑕("涤瑕"),
    32493: Gain("流岚"),
    36035: Gain("潋风")
}

TALENTS = [
    [32450],
    [32580],
    [32464],
    [32490],
    [32492],
    [32500],
    [32457],
    [32508],
    [32511],
    [32513],
    [32493],
    [36035]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
