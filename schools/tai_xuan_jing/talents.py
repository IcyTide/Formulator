from typing import Dict

from base.attribute import Attribute
from base.gain import Gain, Gains
from base.recipe import DamageAdditionRecipe, MagicalCriticalRecipe
from base.skill import Skill


class 重山(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id in (24823, 24676, 24813, 34683):
            skill.channel_interval_extra *= self.value

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (24823, 24676, 24813, 34683):
            skill.channel_interval_extra /= self.value


class 神元(Gain):
    def add_attribute(self, attribute: Attribute):
        attribute.spunk_gain += 102

    def sub_attribute(self, attribute: Attribute):
        attribute.spunk_gain -= 102


TALENT_GAINS: Dict[int, Gains] = {
    24936: Gains("水盈"),
    24925: Gains("正夏", [DamageAdditionRecipe(102, 24369, 24369)]),
    24930: Gains("明心", [MagicalCriticalRecipe((1000, 102), 24369, 24369)]),
    24932: Gains("天网"),
    24934: Gains("望旗", [DamageAdditionRecipe(102, 24371, 24371)]),
    25034: Gains("顺祝"),
    32791: Gains("列宿游"),
    24994: Gains("龙回首"),
    25071: Gains("枭神"),
    24983: Gains("重山", [重山(1.286, skill_id, skill_id) for skill_id in (24369, 24371, 24372)]),
    25025: Gains("地遁"),
    25072: Gains("鬼遁"),
    25137: Gains("堪卜"),
    25022: Gains("祝祷"),
    25368: Gains("亘天"),
    37456: Gains("追叙"),
    25378: Gains("连断"),
    25066: Gains("神元", [神元()]),
    25085: Gains("荧入白"),
    25379: Gains("征凶"),
    25173: Gains("灵器"),
    37505: Gains("镇星入舆")
}

TALENTS = [
    [24936, 24925, 24930],
    [24932, 24934],
    [25034],
    [32791, 24994, 25071],
    [24983, 25025],
    [25072, 25137],
    [25368, 37456, 25022],
    [25378, 25066],
    [25085],
    [25379],
    [25173],
    [37505]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
