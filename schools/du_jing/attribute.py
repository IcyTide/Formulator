from base.attribute import PoisonAttribute
from base.constant import *


class Attribute(PoisonAttribute):
    SPIRIT_TO_ATTACK_POWER = 1997 / BINARY_SCALE
    SPIRIT_TO_OVERCOME = 195 / BINARY_SCALE
    recipes = [(1711, 1)]

    def __init__(self, platform=0):
        super().__init__()
        self.poison_attack_power_base += 4139
        self.pve_addition_base += 104

    @property
    def extra_poison_attack_power(self):
        return int(self.spirit * self.SPIRIT_TO_ATTACK_POWER)

    @property
    def extra_poison_overcome(self):
        return int(self.spirit * self.SPIRIT_TO_OVERCOME)
