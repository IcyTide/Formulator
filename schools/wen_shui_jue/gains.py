from typing import Dict

from base.buff import Buff
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.wen_shui_jue.buffs import BUFFS


class SecondaryWeapon(Gain):
    def __init__(self, secondary_weapon_attrs):
        super().__init__()
        self.secondary_weapon_attrs = secondary_weapon_attrs

    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-1].attributes = self.secondary_weapon_attrs

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-1].attributes = {}


GAINS = {
    1920: CriticalSet(1955, BUFFS[1955].attributes),
    818: DamageAdditionRecipe(102, 0, 1593),
    4347: DamageAdditionRecipe(102, 1600, 1600),
    1536: DamageAdditionRecipe(51, 1646, 1646),
    1537: DamageAdditionRecipe(51, 1590, 0),
    1538: DamageAdditionRecipe(51, 1646, 1646),
    1539: DamageAdditionRecipe(51, 1600, 1600),
    1141: CriticalStrikeRecipe(500, 0, 1646),
    1142: CriticalStrikeRecipe(500, 0, 1600),
    2426: Gain(),
    2427: Gain(),
    1937: Gain(),
    1945: Gain(),
    17368: Gain(),
    17369: Gain(),
    **EQUIPMENT_GAINS,
}
