from base.attribute import PhysicalAttribute, TankAttribute
from base.constant import BINARY_SCALE


class Attribute(PhysicalAttribute, TankAttribute):
    attribute_id = {
        0: 10062
    }
    _tank_buff_level = 3

    vitality_to_physical_attack_power: int = 0
    vitality_to_physical_overcome: int = 0
    recipes = [(1711, 1)]

    @property
    def extra_physical_attack_power(self):
        return int(self.vitality * self.vitality_to_physical_attack_power / BINARY_SCALE)

    @property
    def extra_physical_overcome(self):
        return int(self.vitality * self.vitality_to_physical_overcome / BINARY_SCALE)
