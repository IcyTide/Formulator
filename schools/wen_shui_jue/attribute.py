from base.attribute import PhysicalAttribute
from base.constant import *


class Attribute(PhysicalAttribute):
    AGILITY_TO_ATTACK_POWER = 1843 / BINARY_SCALE
    AGILITY_TO_OVERCOME = 287 / BINARY_SCALE
    recipes = [(1711, 1)]

    def __init__(self, platform=0):
        super().__init__()
        self.physical_attack_power_base += 6513
        self.physical_critical_strike_base += 7827
        self.pve_addition_base += 102

    @property
    def extra_physical_attack_power(self):
        return int(self.agility * self.AGILITY_TO_ATTACK_POWER)

    @property
    def extra_physical_overcome(self):
        return int(self.agility * self.AGILITY_TO_OVERCOME)
