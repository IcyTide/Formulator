from base.attribute import MagicalAttribute
from base.constant import *


class HuaJianYou(MagicalAttribute):
    SPUNK_TO_ATTACK_POWER = 1997 / BINARY_SCALE
    SPUNK_TO_OVERCOME = 195 / BINARY_SCALE

    def __init__(self):
        super().__init__()
        self.magical_attack_power_base += 4139
        self.pve_addition += 102

    @property
    def extra_magical_attack_power(self):
        return int(self.spunk * self.SPUNK_TO_ATTACK_POWER)

    @property
    def extra_magical_overcome(self):
        return int(self.spunk * self.SPUNK_TO_OVERCOME)
