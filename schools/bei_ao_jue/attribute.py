from base.attribute import PhysicalAttribute
from base.constant import *


class BeiAoJue(PhysicalAttribute):
    STRENGTH_TO_ATTACK_POWER = 1587 / BINARY_SCALE
    STRENGTH_TO_OVERCOME = 369 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.physical_attack_power_base += 3725
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
