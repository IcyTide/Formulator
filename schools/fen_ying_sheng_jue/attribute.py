from base.attribute import LunarAttribute
from base.constant import *


class Attribute(LunarAttribute):
    SPUNK_TO_ATTACK_POWER = 2038 / BINARY_SCALE
    SPUNK_TO_CRITICAL_STRIKE = 307 / BINARY_SCALE
    recipes = [(1711, 1)]

    def __init__(self, platform=0):
        super().__init__()
        self.solar_and_lunar_attack_power_base += 7604
        self.pve_addition_base += 82

    @property
    def extra_solar_attack_power(self):
        return int(self.spunk * self.SPUNK_TO_ATTACK_POWER)

    @property
    def extra_lunar_attack_power(self):
        return int(self.spunk * self.SPUNK_TO_ATTACK_POWER)

    @property
    def extra_solar_critical_strike(self):
        return int(self.spunk * self.SPUNK_TO_CRITICAL_STRIKE)

    @property
    def extra_lunar_critical_strike(self):
        return int(self.spunk * self.SPUNK_TO_CRITICAL_STRIKE)
