from typing import Dict

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain, Gains
from base.recipe import PhysicalCriticalRecipe, DamageAdditionRecipe, PveAdditionRecipe


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


TALENT_GAINS: Dict[int, Gains] = {
    20324: Gains("海隅", [DamageAdditionRecipe(102, 19737, 19737)]),
    20333: Gains("江汉", [PhysicalCriticalRecipe((1000, 102), 19818, 19818)]),
    20756: Gains("凌霄", [DamageAdditionRecipe(205, 20052, 0)]),
    20335: Gains("扶桑", [DamageAdditionRecipe(102, 19827, 19827)]),
    20746: Gains("羽彰"),
    20348: Gains("清源"),
    30912: Gains("游仙"),
    25272: Gains("青冥"),
    20751: Gains("鸿轨"),
    25270: Gains("烟涛"),
    20730: Gains("怅归"),
    21293: Gains("溯徊"),
    32476: Gains("风驰"),
    20374: Gains("驰行"),
    20758: Gains("神降", [神降()]),
    20747: Gains("梦悠", [梦悠()]),
    20701: Gains("濯流", [PveAdditionRecipe(1536, 20259, 20259)]),

    101166: Gains("鹏程"),
    101168: Gains("浩渺"),
    101170: Gains("海溟"),
    102111: Gains("澹然若海"),
}

TALENTS = [
    [20333, 20324, 20756, 101166],
    [20335, 101168],
    [20746, 101170],
    [20348, 102111],
    [30912],
    [25272],
    [20751],
    [25270, 20730],
    [21293, 32476],
    [20374, 20758],
    [20747],
    [20701]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
