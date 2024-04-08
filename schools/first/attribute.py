from base.attribute import Attribute
from base.constant import *


class BeiAoJue(Attribute):
    STRENGTH_TO_ATTACK_POWER = 1587 / BINARY_SCALE
    STRENGTH_TO_OVERCOME = 369 / BINARY_SCALE

    def __init__(self):
        super().__init__()
        self.physical_attack_power_base += 3725
        self.pve_addition += 143 / BINARY_SCALE

        self.grad_attrs = [
            "agility_base",
            "strength_base",
            "surplus",
            "strain_base",
            "physical_attack_power_base",
            "physical_critical_strike_base",
            "physical_critical_power_base",
            "physical_overcome_base",
            "weapon_damage_base"
        ]

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

    @property
    def attack_power(self):
        return self.physical_attack_power

    @property
    def critical_strike(self):
        return self.physical_critical_strike

    @property
    def critical_power(self):
        return self.physical_critical_power

    @property
    def overcome(self):
        return self.physical_overcome

    @property
    def shield_ignore(self):
        return self.physical_shield_ignore

    @property
    def damage_addition(self):
        return self.physical_damage_addition

    @property
    def shield_base(self):
        return self.physical_shield_base

    @property
    def shield_gain(self):
        return self.physical_shield_gain

    @property
    def vulnerable(self):
        return self.physical_vulnerable
