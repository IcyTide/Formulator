from base.attribute import MixingAttribute
from base.constant import *


class TianLuoGuiDao(MixingAttribute):
    SPUNK_TO_ATTACK_POWER = 1792 / BINARY_SCALE
    SPUNK_TO_CRITICAL_STRIKE = 584 / BINARY_SCALE

    def __init__(self):
        super().__init__()
        self.magical_attack_power_base += 3725
        self.physical_critical_strike_base += 1279
        self.pve_addition += 41

    @property
    def extra_magical_attack_power(self):
        return int(self.spunk * self.SPUNK_TO_ATTACK_POWER)

    @property
    def extra_physical_critical_strike(self):
        return int(self.spunk * self.SPUNK_TO_CRITICAL_STRIKE)
