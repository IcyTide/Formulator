from base.attribute import PhysicalAttribute
from base.constant import BINARY_SCALE


class Attribute(PhysicalAttribute):
    attribute_id = {
        0: 10390
    }

    agility_to_physical_attack_power: int = 0

    @property
    def extra_physical_attack_power(self):
        return int(self.agility * self.agility_to_physical_attack_power / BINARY_SCALE)
