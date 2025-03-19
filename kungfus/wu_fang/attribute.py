from base.attribute import PoisonAttribute
from base.constant import *


class Attribute(PoisonAttribute):
    attribute_id = 10627

    spirit_to_poison_attack_power: int = 0
    spirit_to_poison_overcome: int = 0
    recipes = [(1711, 1)]

    @property
    def extra_poison_attack_power(self):
        return int(self.spirit * self.spirit_to_poison_attack_power / BINARY_SCALE)

    @property
    def extra_poison_overcome(self):
        return int(self.spirit * self.spirit_to_poison_overcome / BINARY_SCALE)
