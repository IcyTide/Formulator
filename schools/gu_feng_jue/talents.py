from typing import Dict

from base.recipe import PhysicalCriticalRecipe, ExtraTickRecipe
from base.talent import Talent
from base.gain import Gain
from base.skill import Skill


class 放皓(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id in (32216, 32359, 32602):
            skill.physical_critical_strike_rate_extra += 1000
            skill.physical_critical_power_rate_extra += 102
        elif skill.skill_id in (32217, 32360, 32603):
            skill.physical_critical_strike_rate_extra += 2000
            skill.physical_critical_power_rate_extra += 205
        elif skill.skill_id in (32218, 32361, 32604):
            skill.physical_critical_strike_rate_extra += 3000
            skill.physical_critical_power_rate_extra += 307

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (32216, 32359, 32602):
            skill.physical_critical_strike_rate_extra -= 1000
            skill.physical_critical_power_rate_extra -= 102
        elif skill.skill_id in (32217, 32360, 32603):
            skill.physical_critical_strike_rate_extra -= 2000
            skill.physical_critical_power_rate_extra -= 205
        elif skill.skill_id in (32218, 32361, 32604):
            skill.physical_critical_strike_rate_extra -= 3000
            skill.physical_critical_power_rate_extra -= 307


class 涤瑕(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id in (32372, 32874):
            skill.channel_interval_extra *= 1.1
        elif skill.skill_id in (32371, 32873):
            skill.channel_interval_extra *= 1.2
        elif skill.skill_id in (32370, 32872):
            skill.channel_interval_extra *= 1.3
        elif skill.skill_id in (32369, 32871):
            skill.channel_interval_extra *= 1.4
        elif skill.skill_id == 32870:
            skill.channel_interval_extra *= 1.5
        elif skill.skill_id == 32869:
            skill.channel_interval_extra *= 1.6

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (32372, 32874):
            skill.channel_interval_extra /= 1.1
        elif skill.skill_id in (32371, 32873):
            skill.channel_interval_extra /= 1.2
        elif skill.skill_id in (32370, 32872):
            skill.channel_interval_extra /= 1.3
        elif skill.skill_id in (32369, 32871):
            skill.channel_interval_extra /= 1.4
        elif skill.skill_id == 32870:
            skill.channel_interval_extra /= 1.5
        elif skill.skill_id == 32869:
            skill.channel_interval_extra /= 1.6


TALENT_GAINS: Dict[int, Talent] = {
    32450: Talent("渊冲", [PhysicalCriticalRecipe((1000, 102), 32132, 32132)]),
    32580: Talent("戗风"),
    32464: Talent("溃延"),
    32490: Talent("放皓", [放皓(skill_id=32601, skill_recipe=32601)]),
    32492: Talent("电逝"),
    32500: Talent("承磊"),
    32457: Talent("镇机"),
    32508: Talent("长溯"),
    32511: Talent("涣衍", [ExtraTickRecipe(6, 24443, 0)]),
    32513: Talent("涤瑕", [涤瑕(skill_id=32144, skill_recipe=32144)]),
    32493: Talent("流岚"),
    36035: Talent("潋风")
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
TALENT_DECODER = {talent_id: talent.talent_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
