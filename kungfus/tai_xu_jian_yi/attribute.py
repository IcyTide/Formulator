from base.attribute import PhysicalAttribute
from base.constant import *


class Attribute(PhysicalAttribute):
    attribute_id = 10015

    agility_to_physical_attack_power: int = 0
    agility_to_physical_critical_strike: int = 0
    surplus_to_pve_addition: int = 0
    recipes = [(1711, 1)]

    @property
    def extra_physical_attack_power(self):
        return int(self.agility * self.agility_to_physical_attack_power / BINARY_SCALE)

    @property
    def extra_physical_critical_strike(self):
        return int(self.agility * self.agility_to_physical_critical_strike / BINARY_SCALE)

    @property
    def extra_pve_addition(self):
        if self.surplus_to_pve_addition:
            return int(self.surplus_base / (self.surplus_to_pve_addition * 100) * BINARY_SCALE)
        else:
            return 0
