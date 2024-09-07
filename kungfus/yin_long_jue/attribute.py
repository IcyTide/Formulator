from base.attribute import PhysicalAttribute
from base.constant import *


class Attribute(PhysicalAttribute):
    AGILITY_TO_ATTACK_POWER = 1772 / BINARY_SCALE
    AGILITY_TO_OVERCOME = 553 / BINARY_SCALE
    recipes = [(1711, 1)]

    def __init__(self, platform=0):
        super().__init__()
        self.physical_attack_power_base += 6904
        self.physical_overcome_base += 6389
        self.pve_addition_base += 225

    @property
    def extra_physical_attack_power(self):
        return int(self.agility * self.AGILITY_TO_ATTACK_POWER)

    @property
    def extra_physical_overcome(self):
        return int(self.agility * self.AGILITY_TO_OVERCOME)
