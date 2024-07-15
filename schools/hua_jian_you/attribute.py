from base.attribute import NeutralAttribute
from base.constant import *


class HuaJianYou(NeutralAttribute):
    SPUNK_TO_ATTACK_POWER = 1997 / BINARY_SCALE
    SPUNK_TO_OVERCOME = 195 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.neutral_attack_power_base += 4139
        self.pve_addition += 113

    @property
    def extra_neutral_attack_power(self):
        return int(self.spunk * self.SPUNK_TO_ATTACK_POWER)

    @property
    def extra_neutral_overcome(self):
        return int(self.spunk * self.SPUNK_TO_OVERCOME)
