from base.attribute import NeutralAttribute
from base.constant import *


class Attribute(NeutralAttribute):
    attribute_id = {
        0: 10021,
        1: 100408
    }

    spunk_to_neutral_attack_power: int = 0
    spunk_to_neutral_overcome: int = 0
    recipes = [(1711, 1)]

    @property
    def extra_neutral_attack_power(self):
        return int(self.spunk * self.spunk_to_neutral_attack_power / BINARY_SCALE)

    @property
    def extra_neutral_overcome(self):
        return int(self.spunk * self.spunk_to_neutral_overcome / BINARY_SCALE)
