from typing import Dict, Union, Tuple, List

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from base.skill import Skill


class EquipmentGain(Gain):
    buff_ids: List[int] = None
    skill_ids: List[int] = None

    def __init__(self):
        super().__init__(type(self).__name__)

    def add_buffs(self, buffs: Dict[int, Buff]):
        if self.buff_ids:
            for buff_id in self.buff_ids:
                buffs[buff_id].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        if self.buff_ids:
            for buff_id in self.buff_ids:
                buffs[buff_id].activate = False

    def add_skills(self, skills: Dict[int, Skill]):
        if self.skill_ids:
            for skill_id in self.skill_ids:
                skills[skill_id].activate = True

    def sub_skills(self, skills: Dict[int, Skill]):
        if self.skill_ids:
            for skill_id in self.skill_ids:
                skills[skill_id].activate = False


class CriticalSet(EquipmentGain):
    def __init__(self, buff_id):
        self.buff_ids = [buff_id]
        super().__init__()


class DivineEffect(EquipmentGain):
    skill_ids = []


class DivineSubSkill(EquipmentGain):
    skill_ids = []


class WaterWeapon(EquipmentGain):
    buff_ids = [4761]


class WindPendant(EquipmentGain):
    buff_ids = [6360]


class HatSpecialEnchant(EquipmentGain):
    overcome_base = [0] * 8 + [822, 999, 1098, 1218]

    def __init__(self, level):
        super().__init__()
        self.level = level

    def add_attribute(self, attribute: Attribute):
        attribute.physical_overcome_base += self.overcome_base[self.level - 1]
        attribute.magical_overcome_base += self.overcome_base[self.level - 1]

    def sub_attribute(self, attribute: Attribute):
        attribute.physical_overcome_base -= self.overcome_base[self.level - 1]
        attribute.magical_overcome_base -= self.overcome_base[self.level - 1]


class JacketSpecialEnchant(Gain):
    physical_ap = [0] * 8 + [371, 450, 495, 549]
    magical_ap = [0] * 8 + [442, 538, 591, 655]

    def __init__(self, level):
        self.level = level
        super().__init__(type(self).__name__)

    def add_attribute(self, attribute: Attribute):
        attribute.physical_attack_power_base += self.physical_ap[self.level - 1]
        attribute.magical_attack_power_base += self.magical_ap[self.level - 1]

    def sub_attribute(self, attribute: Attribute):
        attribute.physical_attack_power_base -= self.physical_ap[self.level - 1]
        attribute.magical_attack_power_base -= self.magical_ap[self.level - 1]


class BeltSpecialEnchant(EquipmentGain):
    buff_ids = [15455]


class WristSpecialEnchant(EquipmentGain):
    skill_ids = [22160, 22164, 37562]


class ShoesSpecialEnchant(EquipmentGain):
    skill_ids = [33257, 33261, 37561]


EQUIPMENT_GAINS: Dict[Union[Tuple[int, int], int], Gain] = {
    **{
        k: WaterWeapon()
        for k in (2400, 2401, 2497, 2498, 2539, 2540, 2604, 2605)
    },
    **{
        (6800, i): WindPendant()
        for i in range(100, 127 + 1)
    },
    **{
        (15436, i): HatSpecialEnchant(i)
        for i in range(13)
    },
    **{
        (22151, i): JacketSpecialEnchant(i)
        for i in range(13)
    },
    22169: BeltSpecialEnchant(),
    22166: WristSpecialEnchant(),
    33247: ShoesSpecialEnchant()
}
