from typing import Dict, Union, List

from assets.constant import SPECIAL_ENCHANT_MAP
from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from general.buffs.equipment import BUFFS
from general.skills.equipment import SKILLS


class EquipmentGain(Gain):
    _attributes: List[dict] = None
    rate: Union[int, float] = 1
    level: int = 1
    real_formulation: bool = True

    def __init__(self, level=0):
        super().__init__()
        self.level = level

    @property
    def attributes(self):
        if not self._attributes:
            return {}
        elif self.level > len(self._attributes):
            return self._attributes[-1]
        else:
            return self._attributes[self.level - 1]

    @attributes.setter
    def attributes(self, attributes):
        if isinstance(attributes, list):
            self._attributes = attributes
        else:
            self._attributes = [attributes]

    def add_buffs(self, buffs: Dict[int, Buff]):
        if self.real_formulation:
            super().add_buffs(buffs)

    def sub_buffs(self, buffs: Dict[int, Buff]):
        if self.real_formulation:
            super().sub_buffs(buffs)

    def add_attribute(self, attribute: Attribute):
        if self.buff_ids and self.real_formulation:
            return
        for attr, value in self.attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) + int(value * self.rate))

    def sub_attribute(self, attribute: Attribute):
        if self.buff_ids and self.real_formulation:
            return
        for attr, value in self.attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) - int(value * self.rate))


class CriticalSet(EquipmentGain):
    rate = 0.7

    def __init__(self, buff):
        self.buff_ids = [buff.buff_id]
        self.attributes = buff.attributes
        buff.activate = False
        super().__init__()


class DivineEffect(EquipmentGain):
    skill_ids = []

    def __init__(self, skill_id):
        super().__init__()
        self.skill_ids = [skill_id]


class DivineSubSkill(EquipmentGain):
    skill_ids = []

    def __init__(self, skill_id):
        super().__init__()
        self.skill_ids = [skill_id]


class WaterWeapon(EquipmentGain):
    buff_ids = [4761]
    _attributes = BUFFS[4761].all_attributes
    rate = 10


class WindPendant(EquipmentGain):
    buff_ids = [29268]
    _attributes = BUFFS[29268].all_attributes
    rate = 15 / 180


class 大附魔帽(EquipmentGain):
    # buff_ids = [15436]
    _attributes = BUFFS[15436].all_attributes


class 大附魔衣(EquipmentGain):
    _attributes = [
        dict(physical_attack_power_base=physical_attack_power_base, magical_attack_power_base=magical_attack_power_base)
        for physical_attack_power_base, magical_attack_power_base in
        zip(SKILLS[22151].physical_attack_power_base, SKILLS[22151].magical_attack_power_base)
    ]


class 大附魔腰(EquipmentGain):
    buff_ids = [15455]
    _attributes = BUFFS[15455].get_attributes(weights=[3, 7])
    rate = 8 / 30


class 大附魔腕(EquipmentGain):
    skill_ids = list(range(22160, 22164 + 1)) + [37562]


class 大附魔鞋(EquipmentGain):
    skill_ids = list(range(33257, 33261 + 1)) + [37561]


def set_real_formulation(tag):
    EquipmentGain.real_formulation = tag


def set_critical_set_rate(rate):
    CriticalSet.rate = rate


EQUIPMENT_GAINS: Dict[tuple, Gain] = {
    **{
        (k,): WaterWeapon(i)
        for k, i in {
            2400: 55, 2401: 56,
            2497: 59, 2498: 60,
            2539: 63, 2540: 64,
            2604: 67, 2605: 68,
            2655: 71, 2656: 72
        }.items()
    },
    **{
        (38578, i + 1): WindPendant(i + 1)
        for i in range(BUFFS[29268].max_level)
    },
    **{
        (15436, i + 1): 大附魔帽(i + 1)
        for i in range(BUFFS[15436].max_level)
    },
    **{
        (22151, i + 1): 大附魔衣(i + 1)
        for i in range(13)
    },
    **{
        tuple(gain): 大附魔腰()
        for gain in SPECIAL_ENCHANT_MAP[6].values()
    },
    **{
        tuple(gain): 大附魔腕()
        for gain in SPECIAL_ENCHANT_MAP[10].values()
    },
    **{
        tuple(gain): 大附魔鞋()
        for gain in SPECIAL_ENCHANT_MAP[9].values()
    },
}
