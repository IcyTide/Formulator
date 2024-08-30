from base.attribute import PhysicalAttribute
from base.constant import *


class Attribute(PhysicalAttribute):
    AGILITY_TO_ATTACK_POWER = 1731 / BINARY_SCALE
    AGILITY_TO_CRITICAL_STRIKE = 690 / BINARY_SCALE
    recipes = [(1711, 1)]

    def __init__(self, platform=0):
        super().__init__()
        self.physical_attack_power_base += 6187
        self.physical_critical_strike_base += 9025
        self.platform = platform
        if not platform:
            self.pve_addition_base += 82
        else:
            self.pve_addition_base += 460
            self.all_shield_ignore += 614

    @property
    def extra_physical_attack_power(self):
        return int(self.agility * self.AGILITY_TO_ATTACK_POWER)

    @property
    def extra_physical_critical_strike(self):
        return int(self.agility * self.AGILITY_TO_CRITICAL_STRIKE)
