from base.attribute import NeutralAttribute
from base.constant import BINARY_SCALE


class Attribute(NeutralAttribute):
    SPIRIT_TO_ATTACK_POWER = 1946 / BINARY_SCALE
    SPIRIT_TO_CRITICAL_STRIKE = 625 / BINARY_SCALE
    recipes = [(1711, 1)]

    def __init__(self, platform=0):
        super().__init__()
        self.neutral_attack_power_base += 6518
        self.neutral_critical_strike_base += 5527
        self.pve_addition_base += 51

    @property
    def extra_neutral_attack_power(self):
        return int(self.spirit * self.SPIRIT_TO_ATTACK_POWER)

    @property
    def extra_neutral_critical_strike(self):
        return int(self.spirit * self.SPIRIT_TO_CRITICAL_STRIKE)
