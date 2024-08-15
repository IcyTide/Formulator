from typing import Dict

from base.gain import Gain
from base.recipe import PhysicalCriticalRecipe, ChannelIntervalRecipe
from base.skill import Skill


class 无意(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id in (390, 391, 392, 393, 394):
            skill.physical_critical_strike_rate_extra += 1000
            skill.physical_critical_power_rate_extra += 307

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (390, 391, 392, 393, 394):
            skill.physical_critical_strike_rate_extra -= 1000
            skill.physical_critical_power_rate_extra -= 307


TALENTS: Dict[int, Gain] = {
    5807: Gain("心固", [PhysicalCriticalRecipe((1000, 102), 0, 364)]),
    32407: Gain("环月"),
    5800: Gain("白虹"),
    357: Gain("化三清"),
    5818: Gain("无意", [无意(skill_id=365, recipe_type=365)]),
    21812: Gain("云中剑"),
    17742: Gain("风逝"),
    5821: Gain("叠刃"),
    6481: Gain("雾外江山"),
    21725: Gain("长生"),
    24962: Gain("裂云"),
    14598: Gain("若水"),
    18799: Gain("故长"),
    34656: Gain("剑入"),
    14832: Gain("虚极", [ChannelIntervalRecipe(1.2, 600, 0)]),
    14833: Gain("玄门"),

    100448: Gain("周行"),
    100449: Gain("神灵"),
    100451: Gain("固强"),
    100015: Gain("行剑千风")
}

TALENT_CHOICES = [
    [5807, 100448],
    [32407, 100449],
    [5800, 357, 100451],
    [5818, 21812, 100015],
    [17742],
    [5821],
    [6481, 21725],
    [24962, 14598],
    [18799],
    [34656],
    [14832],
    [14833]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
