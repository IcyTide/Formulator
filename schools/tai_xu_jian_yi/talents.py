from typing import Dict

from base.gain import Gain
from base.recipe import PhysicalCriticalRecipe, ChannelIntervalRecipe
from base.skill import Skill
from base.talent import Talent


class 无意(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id in (390, 391, 392, 393, 394):
            skill.physical_critical_strike_rate_extra += 1000
            skill.physical_critical_power_rate_extra += 307

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (390, 391, 392, 393, 394):
            skill.physical_critical_strike_rate_extra -= 1000
            skill.physical_critical_power_rate_extra -= 307


TALENT_GAINS: Dict[int, Talent] = {
    5807: Talent("心固", [PhysicalCriticalRecipe((1000, 102), 0, 364)]),
    32407: Talent("环月"),
    5800: Talent("白虹"),
    357: Talent("化三清"),
    5818: Talent("无意", [无意(skill_id=365, skill_recipe=365)]),
    21812: Talent("云中剑"),
    17742: Talent("风逝"),
    5821: Talent("叠刃"),
    6481: Talent("雾外江山"),
    21725: Talent("长生"),
    24962: Talent("裂云"),
    14598: Talent("若水"),
    18799: Talent("故长"),
    34656: Talent("剑入"),
    14832: Talent("虚极", [ChannelIntervalRecipe(1.2, 600, 0)]),
    14833: Talent("玄门"),

    100448: Talent("周行"),
    100449: Talent("神灵"),
    100451: Talent("固强"),
    100015: Talent("行剑千风")
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
