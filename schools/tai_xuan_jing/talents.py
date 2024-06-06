from typing import Dict

from base.attribute import Attribute
from base.talent import Talent
from base.recipe import DamageAdditionRecipe, MagicalCriticalRecipe
from base.gain import Gain
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


TALENT_GAINS: Dict[int, Talent] = {
    24936: Talent("水盈"),
    24925: Talent("正夏", [DamageAdditionRecipe(102, 24369, 24369)]),
    24930: Talent("明心", [MagicalCriticalRecipe((1000, 102), 24369, 24369)]),
    24932: Talent("天网"),
    24934: Talent("望旗", [DamageAdditionRecipe(102, 24371, 24371)]),
    25034: Talent("顺祝"),
    32791: Talent("列宿游"),
    24994: Talent("龙回首"),
    24983: Talent("重山", [重山(1.286, skill_id, skill_id) for skill_id in (24369, 24371, 24372)]),
    25025: Talent("地遁"),
    25072: Talent("鬼遁"),
    25137: Talent("堪卜"),
    25368: Talent("亘天"),
    37456: Talent("追叙"),
    25378: Talent("连断"),
    25066: Talent("神元", [神元()]),
    25085: Talent("荧入白"),
    25379: Talent("征凶"),
    25173: Talent("灵器"),
    37505: Talent("镇星入舆")
}

TALENTS = [
    [24936, 24925, 24930],
    [24932, 24934],
    [25034],
    [32791, 24994],
    [24983, 25025],
    [25072, 25137],
    [25368, 37456],
    [25378, 25066],
    [25085],
    [25379],
    [25173],
    [37505]
]
TALENT_DECODER = {talent_id: talent.talent_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
