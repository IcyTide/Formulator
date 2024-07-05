from base.attribute import MagicalAttribute
from base.constant import *


class WuFang(MagicalAttribute):
    SPIRIT_TO_ATTACK_POWER = 1843 / BINARY_SCALE
    SPIRIT_TO_OVERCOME = 481 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.magical_attack_power_base += 3808
        self.magical_overcome_base += 1788
        if not platform:
            self.pve_addition += 51
        else:
            self.pve_addition += 461
            self.all_shield_ignore += 614

    @property
    def extra_magical_attack_power(self):
        return int(self.spirit * self.SPIRIT_TO_ATTACK_POWER)

    @property
    def extra_magical_overcome(self):
        return int(self.spirit * self.SPIRIT_TO_OVERCOME)
