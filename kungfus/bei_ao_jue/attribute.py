from base.attribute import PhysicalAttribute
from base.constant import *


class Attribute(PhysicalAttribute):
    STRENGTH_TO_ATTACK_POWER = 1802 / BINARY_SCALE
    STRENGTH_TO_OVERCOME = 420 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.physical_attack_power_base += 7034
        self.platform = platform
        if not platform:
            self.pve_addition_base += 174
        else:
            self.pve_addition_base += 440
            self.all_shield_ignore += 614

    @property
    def extra_physical_attack_power(self):
        return int(self.strength * self.STRENGTH_TO_ATTACK_POWER)

    @property
    def extra_physical_overcome(self):
        return int(self.strength * self.STRENGTH_TO_OVERCOME)
