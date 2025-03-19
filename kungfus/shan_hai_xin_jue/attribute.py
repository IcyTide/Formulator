from base.attribute import PhysicalAttribute
from base.constant import *


class Attribute(PhysicalAttribute):
    attribute_id = 10756

    agility_to_physical_attack_power: int = 0
    agility_to_physical_critical_strike: int = 0
    recipes = [(1711, 1)]

    @property
    def extra_physical_attack_power(self):
        return int(self.agility * self.agility_to_physical_attack_power / BINARY_SCALE)

    @property
    def extra_physical_critical_strike(self):
        return int(self.agility * self.agility_to_physical_critical_strike / BINARY_SCALE)
