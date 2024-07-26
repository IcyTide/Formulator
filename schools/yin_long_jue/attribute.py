from base.attribute import PhysicalAttribute
from base.constant import *


class YinLongJue(PhysicalAttribute):
    AGILITY_TO_ATTACK_POWER = 1536 / BINARY_SCALE
    AGILITY_TO_OVERCOME = 481 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.physical_attack_power_base += 3656
        self.physical_overcome_base += 2081
        self.pve_addition_base += 225

    @property
    def extra_physical_attack_power(self):
        return int(self.agility * self.AGILITY_TO_ATTACK_POWER)

    @property
    def extra_physical_overcome(self):
        return int(self.agility * self.AGILITY_TO_OVERCOME)
