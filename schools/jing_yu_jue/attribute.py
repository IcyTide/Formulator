from base.attribute import PhysicalAttribute
from base.constant import *


class Attribute(PhysicalAttribute):
    STRENGTH_TO_ATTACK_POWER = 1731 / BINARY_SCALE
    STRENGTH_TO_CRITICAL_STRIKE = 707 / BINARY_SCALE
    recipes = [(1711, 1)]

    def __init__(self, platform=0):
        super().__init__()
        self.physical_attack_power_base += 6187
        self.physical_overcome_base += 9025
        self.pve_addition_base += 133

    @property
    def extra_physical_attack_power(self):
        return int(self.strength * self.STRENGTH_TO_ATTACK_POWER)

    @property
    def extra_physical_critical_strike(self):
        return int(self.strength * self.STRENGTH_TO_CRITICAL_STRIKE)
