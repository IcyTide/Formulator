from typing import Dict

from base.buff import Buff
from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain


class SecondaryWeapon(Gain):
    def __init__(self, secondary_weapon_attrs):
        super().__init__(type(self).__name__)
        self.secondary_weapon_attrs = secondary_weapon_attrs

    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-1905].gain_attributes = self.secondary_weapon_attrs

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-1905].gain_attributes = True


GAINS = {
    1920: CriticalSet(1955),
    818: damage_addition_recipe([1594, 1595, 18317], 102),
    4347: damage_addition_recipe([2896], 102),
    1536: damage_addition_recipe([1706], 51),
    1537: Gain(),
    1538: damage_addition_recipe([1707], 51),
    1539: damage_addition_recipe([2896], 51),
    1141: critical_strike_recipe([1706], 500),
    1142: critical_strike_recipe([2896], 500),
    2426: Gain(),
    2427: Gain(),
    1937: Gain(),
    1945: Gain(),
    17368: Gain(),
    17369: Gain(),
    **EQUIPMENT_GAINS,
}
