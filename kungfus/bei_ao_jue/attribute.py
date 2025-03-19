from base.attribute import PhysicalAttribute
from base.constant import BINARY_SCALE


class Attribute(PhysicalAttribute):
    attribute_id = 10464

    strength_to_physical_attack_power: int = 0
    strength_to_physical_overcome: int = 0

    @property
    def extra_physical_attack_power(self):
        return int(self.strength * self.strength_to_physical_attack_power / BINARY_SCALE)

    @property
    def extra_physical_overcome(self):
        return int(self.strength * self.strength_to_physical_overcome / BINARY_SCALE)
