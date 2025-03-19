from base.attribute import NeutralAttribute
from base.constant import BINARY_SCALE


class Attribute(NeutralAttribute):
    attribute_id = 10014

    spirit_to_neutral_attack_power: int = 0
    spirit_to_neutral_critical_strike: int = 0
    recipes = [(1711, 1)]

    @property
    def extra_neutral_attack_power(self):
        return int(self.spirit * self.spirit_to_neutral_attack_power / BINARY_SCALE)

    @property
    def extra_neutral_critical_strike(self):
        return int(self.spirit * self.spirit_to_neutral_critical_strike / BINARY_SCALE)
