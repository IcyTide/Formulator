from base.attribute import NeutralAttribute
from base.constant import *


class Attribute(NeutralAttribute):
    SPUNK_TO_ATTACK_POWER = 2079 / BINARY_SCALE
    SPUNK_TO_OVERCOME = 205 / BINARY_SCALE
    recipes = [(1711, 1)]

    def __init__(self, platform=0):
        super().__init__()
        self.neutral_attack_power_base += 7242
        self.platform = platform
        if not platform:
            self.pve_addition_base += 113
        else:
            self.pve_addition_base += 430
            self.all_shield_ignore += 614

    @property
    def extra_neutral_attack_power(self):
        return int(self.spunk * self.SPUNK_TO_ATTACK_POWER)

    @property
    def extra_neutral_overcome(self):
        return int(self.spunk * self.SPUNK_TO_OVERCOME)
