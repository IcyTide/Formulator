from typing import Dict

from base.attribute import Attribute
from base.buff import Buff
from base.talent import Talent
from base.recipe import PhysicalCriticalRecipe, DamageAdditionRecipe, PveAdditionRecipe
from base.gain import Gain


class 神降(Gain):
    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[14029].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[14029].activate = False


class 梦悠(Gain):
    def add_attribute(self, attribute: Attribute):
        attribute.all_shield_ignore += 307

    def sub_attribute(self, attribute: Attribute):
        attribute.all_shield_ignore -= 307


TALENT_GAINS: Dict[int, Talent] = {
    20333: Talent("江汉", [PhysicalCriticalRecipe((1000, 102), 19818, 19818)]),
    20335: Talent("扶桑", [DamageAdditionRecipe(102, 19827, 19827)]),
    20746: Talent("羽彰"),
    20348: Talent("清源"),
    30912: Talent("游仙"),
    25272: Talent("青冥"),
    20751: Talent("鸿轨"),
    25270: Talent("烟涛"),
    20730: Talent("怅归"),
    21293: Talent("溯徊"),
    32476: Talent("风驰"),
    20374: Talent("驰行"),
    20758: Talent("神降", [神降()]),
    20747: Talent("梦悠", [梦悠()]),
    20701: Talent("濯流", [PveAdditionRecipe(1536, 20259, 20259)])
}

TALENTS = [
    [20333],
    [20335],
    [20746],
    [20348],
    [30912],
    [25272],
    [20751],
    [25270, 20730],
    [21293, 32476],
    [20374, 20758],
    [20747],
    [20701]
]
TALENT_DECODER = {talent_id: talent.talent_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
