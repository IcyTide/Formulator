from typing import Dict

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
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


TALENTS: Dict[int, Gain] = {
    20333: Gain("江汉", [PhysicalCriticalRecipe((1000, 102), 19818, 19818)]),
    20756: Gain("凌霄", [DamageAdditionRecipe(205, 20052, 0)]),
    20335: Gain("扶桑", [DamageAdditionRecipe(102, 19827, 19827)]),
    20746: Gain("羽彰"),
    20348: Gain("清源"),
    30912: Gain("游仙"),
    25272: Gain("青冥"),
    20751: Gain("鸿轨"),
    25270: Gain("烟涛"),
    20730: Gain("怅归"),
    21293: Gain("溯徊"),
    32476: Gain("风驰"),
    20374: Gain("驰行"),
    20758: Gain("神降", [神降()]),
    20747: Gain("梦悠", [梦悠()]),
    20701: Gain("濯流", [PveAdditionRecipe(1536, 20259, 20259)]),

    101166: Gain("鹏程"),
    101168: Gain("浩渺"),
    101170: Gain("海溟"),
    102111: Gain("澹然若海"),
}

TALENT_CHOICES = [
    [20333, 20756, 101166],
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
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
