from base.attribute import PoisonAttribute
from base.constant import *


class Attribute(PoisonAttribute):
    SPIRIT_TO_ATTACK_POWER = 1976 / BINARY_SCALE
    SPIRIT_TO_OVERCOME = 512 / BINARY_SCALE
    recipes = [(1711, 1)]

    def __init__(self, platform=0):
        super().__init__()
        self.poison_attack_power_base += 6663
        self.poison_overcome_base += 5527
        self.platform = platform
        if not platform:
            self.pve_addition_base += 102
        else:
            self.pve_addition_base += 461
            self.all_shield_ignore += 614

    @property
    def extra_poison_attack_power(self):
        return int(self.spirit * self.SPIRIT_TO_ATTACK_POWER)

    @property
    def extra_poison_overcome(self):
        return int(self.spirit * self.SPIRIT_TO_OVERCOME)
