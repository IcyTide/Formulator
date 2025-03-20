from base.attribute import SolarAttribute
from base.constant import *


class Attribute(SolarAttribute):
    attribute_id = 10003

    spunk_to_solar_attack_power: int = 0
    spunk_to_solar_critical_strike: int = 0
    recipes = [(1711, 1)]

    @property
    def extra_solar_attack_power(self):
        return int(self.spunk * self.spunk_to_solar_attack_power / BINARY_SCALE)

    @property
    def extra_solar_critical_strike(self):
        return int(self.spunk * self.spunk_to_solar_critical_strike / BINARY_SCALE)
