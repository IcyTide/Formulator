from base.attribute import NeutralAttribute
from base.constant import BINARY_SCALE


class ZiXiaGong(NeutralAttribute):
    SPIRIT_TO_ATTACK_POWER = 1792 / BINARY_SCALE
    SPIRIT_TO_CRITICAL_STRIKE = 573 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.neutral_attack_power_base += 3725
        self.neutral_critical_strike_base += 1788
        self.pve_addition_base += 51

    @property
    def extra_neutral_attack_power(self):
        return int(self.spirit * self.SPIRIT_TO_ATTACK_POWER)

    @property
    def extra_neutral_critical_strike(self):
        return int(self.spirit * self.SPIRIT_TO_CRITICAL_STRIKE)
