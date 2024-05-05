from base.attribute import MagicalAttribute
from base.constant import *


class WuFang(MagicalAttribute):
    SPIRIT_TO_ATTACK_POWER = 1946 / BINARY_SCALE
    SPIRIT_TO_CRITICAL_STRIKE = 287 / BINARY_SCALE

    def __init__(self):
        super().__init__()
        self.magical_attack_power_base += 4222
        self.pve_addition += 51

    @property
    def extra_magical_attack_power(self):
        return int(self.spirit * self.SPIRIT_TO_ATTACK_POWER)

    @property
    def extra_magical_critical_strike(self):
        return int(self.spirit * self.SPIRIT_TO_CRITICAL_STRIKE)
