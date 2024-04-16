from typing import Dict, Union, Tuple

from base.attribute import Attribute
from base.gain import Gain


class WaterWeapon(Gain):
    attr: str
    max_stack = 10

    def __init__(self, value):
        super().__init__(f"{value} 水特效")
        self.value = value

    def add_attribute(self, attribute: Attribute):
        setattr(attribute, self.attr, getattr(attribute, self.attr) + self.value * self.max_stack)

    def sub_attribute(self, attribute: Attribute):
        setattr(attribute, self.attr, getattr(attribute, self.attr) - self.value * self.max_stack)


class PhysicalWaterWeapon(WaterWeapon):
    attr = "physical_attack_power_base"


class MagicalWaterWeapon(WaterWeapon):
    attr = "magical_attack_power_base"


class WindPendant(Gain):
    duration = 15
    cooldown = 180
    rate = duration / cooldown
    physical_overcome = [0] * 101 + sum([[0, v] + [0] * 5 for v in [6408, 8330, 9291]], [])
    magical_overcome = [0] * 101 + sum([[v, 0] + [0] * 5 for v in [6408, 8330, 9291]], [])

    def __init__(self, level):
        self.level = level
        super().__init__(f"{self.physical_overcome[self.level] | self.magical_overcome[self.level]} 风特效")

    def add_attribute(self, attribute: Attribute):
        attribute.physical_overcome_base += int(self.physical_overcome[self.level] * self.rate)
        attribute.magical_overcome_base += int(self.magical_overcome[self.level] * self.rate)

    def sub_attribute(self, attribute: Attribute):
        attribute.physical_overcome_base -= self.physical_overcome[self.level] * self.rate
        attribute.magical_overcome_base -= int(self.magical_overcome[self.level] * self.rate)


class CriticalSet(Gain):
    critical_strike_value = 400
    critical_power_value = 41
    critical_strike_attr: str
    critical_power_attr: str

    def __init__(self, gain_name, rate):
        super().__init__(gain_name)
        self.rate = rate

    def add_attribute(self, attribute: Attribute):
        setattr(
            attribute, self.critical_strike_attr,
            getattr(attribute, self.critical_strike_attr) + int(self.critical_strike_value * self.rate)
        )
        setattr(
            attribute, self.critical_power_attr,
            getattr(attribute, self.critical_power_attr) + int(self.critical_power_value * self.rate)
        )

    def sub_attribute(self, attribute: Attribute):
        setattr(
            attribute, self.critical_strike_attr,
            getattr(attribute, self.critical_strike_attr) - int(self.critical_strike_value * self.rate)
        )
        setattr(
            attribute, self.critical_power_attr,
            getattr(attribute, self.critical_power_attr) - int(self.critical_power_value * self.rate)
        )


class PhysicalCriticalSet(CriticalSet):
    critical_strike_attr = "physical_critical_strike_gain"
    critical_power_attr = "physical_critical_power_gain"

    def __init__(self, rate):
        super().__init__("外功双会套装", rate)


class MagicalCriticalSet(CriticalSet):
    critical_strike_attr = "magical_critical_strike_gain"
    critical_power_attr = "magical_critical_power_gain"

    def __init__(self, rate):
        super().__init__("内功双会套装", rate)


class HatSpecialEnchant(Gain):
    overcome = [0] * 9 + [822, 999, 1098, 1218]

    def __init__(self, level):
        self.level = level
        super().__init__(f"{self.overcome[self.level]} 破防")

    def add_attribute(self, attribute: Attribute):
        attribute.physical_overcome_base += self.overcome[self.level]

    def sub_attribute(self, attribute: Attribute):
        attribute.physical_overcome_base -= self.overcome[self.level]


class JacketSpecialEnchant(Gain):
    physical_ap = [0] * 9 + [371, 450, 495, 549]
    magical_ap = [0] * 9 + [442, 538, 591, 655]

    def __init__(self, level):
        self.level = level
        super().__init__(f"{self.physical_ap[self.level]}/{self.magical_ap[self.level]} 外攻/内攻")

    def add_attribute(self, attribute: Attribute):
        attribute.physical_attack_power_base += self.physical_ap[self.level]
        attribute.magical_attack_power_base += self.magical_ap[self.level]

    def sub_attribute(self, attribute: Attribute):
        attribute.physical_attack_power_base -= self.physical_ap[self.level]
        attribute.magical_attack_power_base -= self.magical_ap[self.level]


EQUIPMENT_GAINS: Dict[Union[Tuple[int, int], int], Gain] = {
    2400: MagicalWaterWeapon(81),
    2401: PhysicalWaterWeapon(67),
    2497: MagicalWaterWeapon(105),
    2498: PhysicalWaterWeapon(88),
    2539: MagicalWaterWeapon(117),
    2540: PhysicalWaterWeapon(98),
    **{
        (6800, i): WindPendant(i)
        for i in range(101, 117)
    },
    **{
        (15436, i): HatSpecialEnchant(i)
        for i in range(13)
    },
    **{
        (22151, i): JacketSpecialEnchant(i)
        for i in range(13)
    },
}
