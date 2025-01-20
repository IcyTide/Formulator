from base.attribute import LunarAttribute
from base.constant import BINARY_SCALE


class Attribute(LunarAttribute):
    attribute_id = {
        0: 10243
    }

    # buff: 17885-4
    vitality_to_solar_attack_power: int = 572
    vitality_to_lunar_attack_power: int = 572
    vitality_to_magical_overcome: int = 549
    vitality_to_magical_critical_strike: int = 0

    recipes = [(1711, 1)]

    @property
    def extra_solar_attack_power(self):
        return int(self.vitality * self.vitality_to_solar_attack_power / BINARY_SCALE)

    @property
    def extra_lunar_attack_power(self):
        return int(self.vitality * self.vitality_to_lunar_attack_power / BINARY_SCALE)

    @property
    def extra_magical_overcome(self):
        return int(self.vitality * self.vitality_to_magical_overcome / BINARY_SCALE)

    @property
    def extra_magical_critical_strike(self):
        return int(self.vitality * self.vitality_to_magical_critical_strike / BINARY_SCALE)
