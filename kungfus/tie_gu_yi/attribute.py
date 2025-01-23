from base.attribute import PhysicalAttribute
from base.constant import BINARY_SCALE


class Attribute(PhysicalAttribute):
    attribute_id = {
        0: 10389
    }

    # buff: 17885-5
    vitality_to_physical_attack_power: int = 174
    vitality_to_physical_overcome: int = 147
    vitality_to_parry: int = 0

    @property
    def extra_physical_attack_power(self):
        return int(self.vitality * self.vitality_to_physical_attack_power / BINARY_SCALE)

    @property
    def extra_physical_overcome(self):
        return int(self.vitality * self.vitality_to_physical_overcome / BINARY_SCALE)

    @property
    def extra_parry(self):
        return int(self.vitality * self.vitality_to_parry / BINARY_SCALE)
