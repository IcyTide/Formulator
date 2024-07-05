from base.attribute import PhysicalAttribute
from base.constant import *


class GuFengJue(PhysicalAttribute):
    STRENGTH_TO_ATTACK_POWER = 1638 / BINARY_SCALE
    STRENGTH_TO_CRITICAL_STRIKE = 256 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.physical_attack_power_base += 3346
        self.physical_critical_strike_base += 2775
        if not platform:
            self.pve_addition += 184
        else:
            self.pve_addition += 461
            self.all_shield_ignore += 614

    @property
    def extra_physical_attack_power(self):
        return int(self.strength * self.STRENGTH_TO_ATTACK_POWER)

    @property
    def extra_physical_critical_strike(self):
        return int(self.strength * self.STRENGTH_TO_CRITICAL_STRIKE)
