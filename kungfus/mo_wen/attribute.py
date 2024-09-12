from base.attribute import LunarAttribute
from base.constant import *


class Attribute(LunarAttribute):
    attribute_id = {
        0: 10447
    }

    spirit_to_lunar_attack_power: int = 0
    spirit_to_lunar_critical_strike: int = 0

    @property
    def extra_lunar_attack_power(self):
        return int(self.spirit * self.spirit_to_lunar_attack_power / BINARY_SCALE)

    @property
    def extra_lunar_critical_strike(self):
        return int(self.spirit * self.spirit_to_lunar_critical_strike / BINARY_SCALE)
