from base.attribute import MagicalAttribute
from base.constant import *


class TaiXuanJing(MagicalAttribute):
    SPUNK_TO_ATTACK_POWER = 1843 / BINARY_SCALE
    SPUNK_TO_CRITICAL_STRIKE = 481 / BINARY_SCALE

    def __init__(self):
        super().__init__()
        self.magical_attack_power_base += 4222
        self.magical_critical_strike_base += 2390
        self.pve_addition += 123

    @property
    def extra_magical_attack_power(self):
        return int(self.spunk * self.SPUNK_TO_ATTACK_POWER)

    @property
    def extra_magical_critical_strike(self):
        return int(self.spunk * self.SPUNK_TO_CRITICAL_STRIKE)
