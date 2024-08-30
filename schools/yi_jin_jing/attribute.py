from base.attribute import SolarAttribute
from base.constant import *


class Attribute(SolarAttribute):
    SPUNK_TO_ATTACK_POWER = 1894 / BINARY_SCALE
    SPUNK_TO_CRITICAL_STRIKE = 389 / BINARY_SCALE
    recipes = [(1711, 1)]

    def __init__(self, platform=0):
        super().__init__()
        self.solar_attack_power_base += 4139
        self.pve_addition_base += 103

    @property
    def extra_solar_attack_power(self):
        return int(self.spunk * self.SPUNK_TO_ATTACK_POWER)

    @property
    def extra_solar_critical_strike(self):
        return int(self.spunk * self.SPUNK_TO_CRITICAL_STRIKE)
