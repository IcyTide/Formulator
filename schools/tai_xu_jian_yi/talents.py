from typing import Dict

from base.gain import Gain
from base.talent import Talent
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
    18799: Talent("故长"),
    34656: Talent("剑入"),
    14832: Talent("虚极", [ChannelIntervalRecipe(1.2, 600, 0)]),
    14833: Talent("玄门"),
}

TALENTS = [
    [5807],
    [32407],
    [5800, 357],
    [5818, 21812],
    [17742],
    [5821],
    [6481, 21725],
    [24962],
    [18799],
    [34656],
    [14832],
    [14833]
]
TALENT_DECODER = {talent_id: talent.talent_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
