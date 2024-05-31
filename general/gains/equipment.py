from typing import Dict, Union, Tuple, List

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from base.skill import Skill
from general.buffs.equipment import GENERAL_BUFFS


class EquipmentGain(Gain):
    buff_ids: List[int] = None
    skill_ids: List[int] = None
    gain_attributes: Dict[str, List[int]] = {}
    rate: Union[int, float] = 1
    level: int = 0
    real_formulation: bool = True

    def __init__(self, level=0):
        super().__init__(type(self).__name__)
        self.level = level

    def add_buffs(self, buffs: Dict[int, Buff]):
        if self.buff_ids and self.real_formulation:
            for buff_id in self.buff_ids:
                buffs[buff_id].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        if self.buff_ids and self.real_formulation:
            for buff_id in self.buff_ids:
                buffs[buff_id].activate = False

    def add_skills(self, skills: Dict[int, Skill]):
        if self.skill_ids and self.real_formulation:
            for skill_id in self.skill_ids:
                skills[skill_id].activate = True

    def sub_skills(self, skills: Dict[int, Skill]):
        if self.skill_ids and self.real_formulation:
            for skill_id in self.skill_ids:
                skills[skill_id].activate = False

    def add_attribute(self, attribute: Attribute):
        if (self.skill_ids or self.buff_ids) and self.real_formulation:
            return
        for attr, values in self.gain_attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) + int(values[self.level - 1] * self.rate))

    def sub_attribute(self, attribute: Attribute):
        if (self.skill_ids or self.buff_ids) and self.real_formulation:
            return
        for attr, values in self.gain_attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) - int(values[self.level - 1] * self.rate))


class CriticalSet(EquipmentGain):
    rate = 0.7

    def __init__(self, buff_id, gain_attributes):
        self.buff_ids = [buff_id]
        self.gain_attributes = {attr: [value] for attr, value in gain_attributes.items()}
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
    gain_attributes = GENERAL_BUFFS[4761].gain_attributes
    rate = 10


class WindPendant(EquipmentGain):
    buff_ids = [6360]
    gain_attributes = GENERAL_BUFFS[6360].gain_attributes
    rate = 15 / 180


class 大附魔帽(EquipmentGain):
    gain_attributes = {
        "physical_overcome_base": [0] * 8 + [822, 999, 1098, 1218],
        "magical_overcome_base": [0] * 8 + [822, 999, 1098, 1218]
    }


class 大附魔衣(EquipmentGain):
    gain_attributes = {
        "physical_attack_power_base": [0] * 8 + [371, 450, 495, 549],
        "magical_attack_power_base": [0] * 8 + [442, 538, 591, 655]
    }


class 大附魔腰(EquipmentGain):
    buff_ids = [15455]
    gain_attributes = {
        attr: [sum(value * prob for value, prob in zip(values, [0.3, 0.7]))]
        for attr, values in GENERAL_BUFFS[15455].gain_attributes.items()
    }
    rate = 8 / 30


class 大附魔腕(EquipmentGain):
    skill_ids = [22160, 22161, 22162, 22163, 22164, 37562]


class 大附魔鞋(EquipmentGain):
    skill_ids = [33257, 33258, 33259, 33260, 33261, 37561]


def set_real_formulation(tag):
    for gain in EQUIPMENT_GAINS.values():
        gain.real_formulation = tag
    CriticalSet.real_formulation = tag


def set_critical_set_rate(rate):
    CriticalSet.rate = rate


EQUIPMENT_GAINS: Dict[Union[Tuple[int, int], int], Gain] = {
    **{
        k: WaterWeapon(i)
        for k, i in {
            2400: 55, 2401: 56,
            2497: 59, 2498: 60,
            2539: 63, 2540: 64,
            2604: 67, 2605: 68
        }.items()
    },
    **{
        (6800, i): WindPendant(i)
        for i in range(100, 127 + 1)
    },
    **{
        (15436, i): 大附魔帽(i)
        for i in range(13)
    },
    **{
        (22151, i): 大附魔衣(i)
        for i in range(13)
    },
    22169: 大附魔腰(),
    22166: 大附魔腕(),
    33247: 大附魔鞋(),

    17250: Gain(),
    17239: Gain(),
}
