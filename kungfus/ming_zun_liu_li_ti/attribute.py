from base.attribute import LunarAttribute, TankAttribute
from base.constant import BINARY_SCALE


class Attribute(LunarAttribute, TankAttribute):
    attribute_id = 10243

    _tank_buff_level = 4

    vitality_to_solar_attack_power: int = 0
    vitality_to_lunar_attack_power: int = 0
    vitality_to_magical_overcome: int = 0
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
