from typing import Dict, Union, Tuple

from base.attribute import Attribute
from base.gain import Gain


class WaterWeapon(Gain):
    attr: str
    max_stack = 10

    def __init__(self, value):
        super().__init__(f"{value} 攻击")
        self.value = value

    def add(self, other):
        if isinstance(other, Attribute):
            setattr(other, self.attr, getattr(other, self.attr) + self.value * self.max_stack)

    def sub(self, other):
        if isinstance(other, Attribute):
            setattr(other, self.attr, getattr(other, self.attr) - self.value * self.max_stack)


class PhysicalWaterWeapon(WaterWeapon):
    attr = "physical_attack_power_base"


class MagicalWaterWeapon(WaterWeapon):
    attr = "magical_attack_power_base"


class WindPendant(Gain):
    physical_overcome = [0] * 101 + sum([[0, v] + [0] * 5 for v in [6408, 8330, 9291]], [])
    magical_overcome = [0] * 101 + sum([[v, 0] + [0] * 5 for v in [6408, 8330, 9291]], [])

    def __init__(self, level):
        self.level = level
        super().__init__(f"{self.physical_overcome[self.level] | self.magical_overcome[self.level]} 破防")

    def add(self, other):
        if isinstance(other, Attribute):
            other.physical_overcome_base += self.physical_overcome[self.level]
            other.magical_overcome_base += self.magical_overcome[self.level]

    def sub(self, other):
        if isinstance(other, Attribute):
            other.physical_overcome_base -= self.physical_overcome[self.level]
            other.magical_overcome_base -= self.magical_overcome[self.level]


class CriticalSet(Gain):
    critical_strike_value = 400
    critical_power_value = 41
    critical_strike_attr: str
    critical_power_attr: str

    def __init__(self, gain_name, rate):
        super().__init__(gain_name)
        self.rate = rate

    def add(self, other):
        if isinstance(other, Attribute):
            setattr(
                other, self.critical_strike_attr,
                getattr(other, self.critical_strike_attr) + int(self.critical_strike_value * self.rate)
            )
            setattr(
                other, self.critical_power_attr,
                getattr(other, self.critical_power_attr) + int(self.critical_power_value * self.rate)
            )

    def sub(self, other):
        if isinstance(other, Attribute):
            setattr(
                other, self.critical_strike_attr,
                getattr(other, self.critical_strike_attr) - int(self.critical_strike_value * self.rate)
            )
            setattr(
                other, self.critical_power_attr,
                getattr(other, self.critical_power_attr) - int(self.critical_power_value * self.rate)
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
    overcome = [0] * 9 + [822, 999, 1098]

    def __init__(self, level):
        self.level = level
        super().__init__(f"{self.overcome[self.level]} 破防")

    def add(self, other):
        if isinstance(other, Attribute):
            other.physical_overcome_base += self.overcome[self.level]

    def sub(self, other):
        if isinstance(other, Attribute):
            other.physical_overcome_base -= self.overcome[self.level]


class JacketSpecialEnchant(Gain):
    physical_ap = [0] * 9 + [371, 450, 495]
    magical_ap = [0] * 9 + [442, 538, 591]

    def __init__(self, level):
        self.level = level
        super().__init__(f"{self.physical_ap[self.level]}/{self.magical_ap[self.level]} 外攻/内攻")

    def add(self, other):
        if isinstance(other, Attribute):
            other.physical_attack_power_base += self.physical_ap[self.level]
            other.magical_attack_power_base += self.magical_ap[self.level]

    def sub(self, other):
        if isinstance(other, Attribute):
            other.physical_attack_power_base -= self.physical_ap[self.level]
            other.magical_attack_power_base -= self.magical_ap[self.level]


class BeltSpecialEnchant(Gain):
    damage_addition = {
        51: 0.7,
        10: 0.3
    }
    duration = 128
    cooldown = 480

    def __init__(self):
        self.all_damage_addition = sum(k * v for k, v in self.damage_addition.items()) * self.duration / self.cooldown
        super().__init__(f"{round(self.all_damage_addition, 2)} 伤害增加")

    def add(self, other):
        if isinstance(other, Attribute):
            other.all_damage_addition += self.all_damage_addition

    def sub(self, other):
        if isinstance(other, Attribute):
            other.all_damage_addition -= self.all_damage_addition


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
        for i in range(12)
    },
    **{
        (22151, i): JacketSpecialEnchant(i)
        for i in range(12)
    },
    22169: BeltSpecialEnchant(),

}
