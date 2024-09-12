from base.attribute import PhysicalAttribute
from base.constant import *


class Attribute(PhysicalAttribute):
    attribute_id = {
        0: 10144
    }

    agility_to_physical_attack_power = 1843
    agility_to_physical_overcome = 287 / BINARY_SCALE
    recipes = [(1711, 1)]

    @property
    def extra_physical_attack_power(self):
        return int(self.agility * self.agility_to_physical_attack_power / BINARY_SCALE)

    @property
    def extra_physical_overcome(self):
        return int(self.agility * self.agility_to_physical_overcome / BINARY_SCALE)
