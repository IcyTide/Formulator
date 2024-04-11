from typing import Dict, Union, Tuple

from base.attribute import Attribute
from base.gain import Gain


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
        super().__init__(f"{self.all_damage_addition} 伤害增加")

    def add(self, other):
        if isinstance(other, Attribute):
            other.all_damage_addition += self.all_damage_addition

    def sub(self, other):
        if isinstance(other, Attribute):
            other.all_damage_addition -= self.all_damage_addition


EQUIPMENT_GAINS: Dict[Union[Tuple[int, int], int], Gain] = {
    **{
        (15436, i): HatSpecialEnchant(i)
        for i in range(12)
    },
    **{
        (22151, i): JacketSpecialEnchant(i)
        for i in range(12)
    },
    15455: BeltSpecialEnchant()
}
