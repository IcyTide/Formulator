from typing import Dict

from base.buff import Buff
from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet


class SecondaryWeapon(Gain):
    def __init__(self, secondary_weapon_attrs):
        super().__init__()
        self.secondary_weapon_attrs = secondary_weapon_attrs

    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-1].attributes = self.secondary_weapon_attrs

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-1].attributes = dict(weapon_damage_base=0)


GAINS = {
    (1920,): CriticalSet(GENERAL_BUFFS[1955]),
    (2744,): Gain(),
    (2743,): Gain(),
    (1945,): Gain(),
    (1937,): Gain(),
    (2427,): Gain(),
    (2426,): Gain(),
    **EQUIPMENT_GAINS,
}
