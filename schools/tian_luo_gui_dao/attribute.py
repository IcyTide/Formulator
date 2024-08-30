from base.attribute import MixingAttribute
from base.constant import *


class Attribute(MixingAttribute):
    SPUNK_TO_ATTACK_POWER = 1946 / BINARY_SCALE
    SPUNK_TO_CRITICAL_STRIKE = 635 / BINARY_SCALE
    recipes = [(1711, 1)]

    def __init__(self, platform=0):
        super().__init__()
        self.poison_attack_power_base += 6518
        self.physical_critical_strike_base += 3962
        self.pve_addition_base += 21

    @property
    def extra_poison_attack_power(self):
        return int(self.spunk * self.SPUNK_TO_ATTACK_POWER)

    @property
    def extra_physical_critical_strike(self):
        return int(self.spunk * self.SPUNK_TO_CRITICAL_STRIKE)
