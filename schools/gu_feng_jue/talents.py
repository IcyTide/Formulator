from typing import Dict

from base.attribute import Attribute
from base.gain import Gain
from base.recipe import PhysicalCriticalRecipe, DamageAdditionRecipe, ExtraTickRecipe, PveAdditionRecipe
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


class 强膂(Gain):
    def add_attribute(self, attribute: Attribute):
        attribute.strength_gain += 102

    def sub_attribute(self, attribute: Attribute):
        attribute.strength_gain -= 102


class 斩涛(Gain):
    def add_attribute(self, attribute: Attribute):
        attribute.strength_gain += 154

    def sub_attribute(self, attribute: Attribute):
        attribute.strength_gain -= 154


TALENTS: Dict[int, Gain] = {
    32450: Gain("渊冲", [PhysicalCriticalRecipe((1000, 102), 32132, 32132)]),
    32580: Gain("戗风", [DamageAdditionRecipe(82, skill_id, skill_id) for skill_id in (32145, 32144, 32601)]),
    32464: Gain("溃延"),
    32456: Gain("雨积"),
    32490: Gain("放皓", [放皓(skill_id=32601, recipe_type=32601)]),
    32492: Gain("电逝"),
    33027: Gain("威声"),
    32497: Gain("击懈", [PveAdditionRecipe(1024, 32134, 32134)]),
    32500: Gain("承磊"),
    32502: Gain("滔天"),
    32457: Gain("镇机"),
    32512: Gain("界破"),
    32508: Gain("长溯"),
    32511: Gain("涣衍", [ExtraTickRecipe(6, 24443, 0)]),
    32513: Gain("涤瑕", [涤瑕(skill_id=32144, recipe_type=32144)]),
    32578: Gain("强膂", [强膂()]),
    32493: Gain("流岚"),
    32452: Gain("聚疏"),
    36035: Gain("潋风"),
    32586: Gain("截辕"),

    101537: Gain("斩涛", [斩涛()]),
    101539: Gain("披靡"),
    101542: Gain("倒海"),
    101395: Gain("孤风破浪")
}

TALENT_CHOICES = [
    [32450, 101537],
    [32580, 101539],
    [32464, 101542],
    [32490, 101395],
    [32492, 33027],
    [32500, 32497],
    [32457, 32512, 32502],
    [32508],
    [32511],
    [32513, 32578],
    [32493, 32452],
    [36035, 32586]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
