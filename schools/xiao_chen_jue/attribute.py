from base.attribute import PhysicalAttribute
from base.constant import *


class Attribute(PhysicalAttribute):
    STRENGTH_TO_ATTACK_POWER = 1772 / BINARY_SCALE
    STRENGTH_TO_OVERCOME = 553 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.physical_attack_power_base += 6839
        self.pve_addition_base += 41

    @property
    def extra_physical_attack_power(self):
        return int(self.strength * self.STRENGTH_TO_ATTACK_POWER)

    @property
    def extra_physical_overcome(self):
        return int(self.strength * self.STRENGTH_TO_OVERCOME)
