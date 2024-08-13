from typing import Dict

from base.gain import Gain, Gains
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


TALENT_GAINS: Dict[int, Gains] = {
    5807: Gains("心固", [PhysicalCriticalRecipe((1000, 102), 0, 364)]),
    32407: Gains("环月"),
    5800: Gains("白虹"),
    357: Gains("化三清"),
    5818: Gains("无意", [无意(skill_id=365, recipe_type=365)]),
    21812: Gains("云中剑"),
    17742: Gains("风逝"),
    5821: Gains("叠刃"),
    6481: Gains("雾外江山"),
    21725: Gains("长生"),
    24962: Gains("裂云"),
    14598: Gains("若水"),
    18799: Gains("故长"),
    34656: Gains("剑入"),
    14832: Gains("虚极", [ChannelIntervalRecipe(1.2, 600, 0)]),
    14833: Gains("玄门"),

    100448: Gains("周行"),
    100449: Gains("神灵"),
    100451: Gains("固强"),
    100015: Gains("行剑千风")
}

TALENTS = [
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
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
