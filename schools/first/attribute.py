from base.attribute import PhysicalAttribute
from base.constant import *


class BeiAoJue(PhysicalAttribute):
    STRENGTH_TO_ATTACK_POWER = 1587 / BINARY_SCALE
    STRENGTH_TO_OVERCOME = 369 / BINARY_SCALE

    def __init__(self):
        super().__init__()
        self.physical_attack_power_base += 3725
        self.pve_addition += 143

        self.grad_attrs = {
            "agility_base": MAJOR_DELTA,
            "strength_base": MAJOR_DELTA,
            "surplus": MINOR_DELTA,
            "strain_base": MINOR_DELTA,
            "physical_attack_power_base": PHYSICAL_DELTA,
            "physical_critical_strike_base": MINOR_DELTA,
            "physical_critical_power_base": MINOR_DELTA,
            "physical_overcome_base": MINOR_DELTA,
            "weapon_damage_base": WEAPON_DELTA
        }

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        strength = int(strength)
        self._strength = strength
        self._extra_physical_attack_power = int(strength * self.STRENGTH_TO_ATTACK_POWER)
        self.base_physical_attack_power = self._physical_attack_power_base + strength * STRENGTH_TO_ATTACK_POWER
        self._extra_physical_overcome = int(strength * self.STRENGTH_TO_OVERCOME)
        self.base_physical_overcome = self._physical_overcome_base + strength * STRENGTH_TO_OVERCOME

