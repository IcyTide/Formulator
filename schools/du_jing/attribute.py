from base.attribute import MagicalAttribute
from base.constant import *


class DuJing(MagicalAttribute):
    SPIRIT_TO_ATTACK_POWER = 1997 / BINARY_SCALE
    SPIRIT_TO_OVERCOME = 195 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.magical_attack_power_base += 4139
        self.pve_addition += 104

    @property
    def extra_magical_attack_power(self):
        return int(self.spirit * self.SPIRIT_TO_ATTACK_POWER)

    @property
    def extra_magical_overcome(self):
        return int(self.spirit * self.SPIRIT_TO_OVERCOME)
