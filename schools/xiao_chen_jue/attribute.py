from base.attribute import PhysicalAttribute
from base.constant import *


class XiaoChenJue(PhysicalAttribute):
    STRENGTH_TO_ATTACK_POWER = 1536 / BINARY_SCALE
    STRENGTH_TO_OVERCOME = 481 / BINARY_SCALE

    def __init__(self):
        super().__init__()
        self.physical_attack_power_base += 3621
        self.pve_addition += 41

    @property
    def extra_physical_attack_power(self):
        return int(self.strength * self.STRENGTH_TO_ATTACK_POWER)

    @property
    def extra_physical_overcome(self):
        return int(self.strength * self.STRENGTH_TO_OVERCOME)
