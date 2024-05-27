from base.attribute import PhysicalAttribute
from base.constant import *


class LingHaiJue(PhysicalAttribute):
    AGILITY_TO_ATTACK_POWER = 1587 / BINARY_SCALE
    AGILITY_TO_CRITICAL_STRIKE = 369 / BINARY_SCALE

    def __init__(self):
        super().__init__()
        self.physical_attack_power_base += 3621
        self.physical_critical_strike_base += 2158

    @property
    def extra_physical_attack_power(self):
        return int(self.agility * self.AGILITY_TO_ATTACK_POWER)

    @property
    def extra_physical_critical_strike(self):
        return int(self.agility * self.AGILITY_TO_CRITICAL_STRIKE)
