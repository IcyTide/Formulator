from base.attribute import PhysicalAttribute
from base.constant import *


class Attribute(PhysicalAttribute):
    attribute_id = 10698

    strength_to_physical_attack_power: int = 0
    strength_to_physical_critical_strike: int = 0

    @property
    def extra_physical_attack_power(self):
        return int(self.strength * self.strength_to_physical_attack_power / BINARY_SCALE)

    @property
    def extra_physical_critical_strike(self):
        return int(self.strength * self.strength_to_physical_critical_strike / BINARY_SCALE)
