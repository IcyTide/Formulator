from base.attribute import MixingAttribute
from base.constant import *


class Attribute(MixingAttribute):
    attribute_id = {
        0: 10225
    }

    spunk_to_poison_attack_power: int = 0
    spunk_to_physical_critical_strike: int = 0
    recipes = [(1711, 1)]

    @property
    def extra_poison_attack_power(self):
        return int(self.spunk * self.spunk_to_poison_attack_power / BINARY_SCALE)

    @property
    def extra_physical_critical_strike(self):
        return int(self.spunk * self.spunk_to_physical_critical_strike / BINARY_SCALE)
