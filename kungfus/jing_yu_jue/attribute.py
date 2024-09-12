from base.attribute import PhysicalAttribute
from base.constant import *


class Attribute(PhysicalAttribute):
    attribute_id = {
        0: 10224
    }

    strength_to_physical_attack_power = 1731 / BINARY_SCALE
    strength_to_physical_critical_strike = 707 / BINARY_SCALE
    recipes = [(1711, 1)]

    @property
    def extra_physical_attack_power(self):
        return int(self.strength * self.strength_to_physical_attack_power / BINARY_SCALE)

    @property
    def extra_physical_critical_strike(self):
        return int(self.strength * self.strength_to_physical_critical_strike / BINARY_SCALE)
