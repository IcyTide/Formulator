from base.attribute import PhysicalAttribute
from base.constant import *


class Attribute(PhysicalAttribute):
    STRENGTH_TO_ATTACK_POWER = 1843 / BINARY_SCALE
    STRENGTH_TO_CRITICAL_STRIKE = 287 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.physical_attack_power_base += 6318
        self.physical_critical_strike_base += 8546
        self.platform = platform
        if not platform:
            self.pve_addition_base += 184
        else:
            self.pve_addition_base += 461
            self.all_shield_ignore += 614

    @property
    def extra_physical_attack_power(self):
        return int(self.strength * self.STRENGTH_TO_ATTACK_POWER)

    @property
    def extra_physical_critical_strike(self):
        return int(self.strength * self.STRENGTH_TO_CRITICAL_STRIKE)
