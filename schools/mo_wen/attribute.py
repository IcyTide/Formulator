from base.attribute import LunarAttribute
from base.constant import *


class MoWen(LunarAttribute):
    SPIRIT_TO_ATTACK_POWER = 1895 / BINARY_SCALE
    SPIRIT_TO_CRITICAL_STRIKE = 389 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.lunar_attack_power_base += 3725
        self.lunar_critical_strike_base += 1279
        self.pve_addition_base += 164

    @property
    def extra_lunar_attack_power(self):
        return int(self.spirit * self.SPIRIT_TO_ATTACK_POWER)

    @property
    def extra_lunar_critical_strike(self):
        return int(self.spirit * self.SPIRIT_TO_CRITICAL_STRIKE)
