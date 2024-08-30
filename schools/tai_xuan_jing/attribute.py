from base.attribute import NeutralAttribute
from base.constant import *


class Attribute(NeutralAttribute):
    SPUNK_TO_ATTACK_POWER = 1976 / BINARY_SCALE
    SPUNK_TO_CRITICAL_STRIKE = 512 / BINARY_SCALE
    recipes = [(1711, 1)]

    def __init__(self, platform=0):
        super().__init__()
        self.neutral_attack_power_base += 7387
        self.neutral_critical_strike_base += 7347
        self.pve_addition_base += 144

    @property
    def extra_neutral_attack_power(self):
        return int(self.spunk * self.SPUNK_TO_ATTACK_POWER)

    @property
    def extra_neutral_critical_strike(self):
        return int(self.spunk * self.SPUNK_TO_CRITICAL_STRIKE)
