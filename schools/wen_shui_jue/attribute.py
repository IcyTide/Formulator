from base.attribute import PhysicalAttribute
from base.constant import *


class WenShuiJue(PhysicalAttribute):
    AGILITY_TO_ATTACK_POWER = 1638 / BINARY_SCALE
    AGILITY_TO_OVERCOME = 256 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.physical_attack_power_base += 3449
        self.physical_critical_strike_base += 2544
        self.pve_addition += 102

    @property
    def extra_physical_attack_power(self):
        return int(self.agility * self.AGILITY_TO_ATTACK_POWER)

    @property
    def extra_physical_overcome(self):
        return int(self.agility * self.AGILITY_TO_OVERCOME)
