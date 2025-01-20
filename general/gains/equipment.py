from typing import Dict, Union, List

from assets.constant import SPECIAL_ENCHANT_MAP
from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from base.skill import Skill, PureSkill
from general.buffs import GENERAL_BUFFS
from general.skills import GENERAL_SKILLS


class EquipmentGain(Gain):
    _attributes: List[dict] = None
    _damage_base: List[int] = None

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

    @property
    def damage_base(self):
        if not self._damage_base:
            return 0
        elif self.level > len(self._damage_base):
            return self._damage_base[-1]
        else:
            return self._damage_base[self.level - 1]

    def add_buffs(self, buffs: Dict[int, Buff]):
        if self.real_formulation:
            super().add_buffs(buffs)

    def sub_buffs(self, buffs: Dict[int, Buff]):
        if self.real_formulation:
            super().sub_buffs(buffs)

    def add_skills(self, skills: Dict[int, Union[PureSkill, Skill]]):
        super().add_skills(skills)
        if damage_base := self.damage_base:
            for skill_id in self.skill_ids:
                skills[skill_id].damage_base = damage_base

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

    def __init__(self, buff: Buff):
        self.buff_ids = [buff.buff_id]
        self._attributes = [buff.attributes]
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


class DivineGain(EquipmentGain):
    buff_ids = [29608]
    _attributes = GENERAL_BUFFS[29608].all_attributes
    rate = 5


class WaterWeapon(EquipmentGain):
    buff_ids = [4761]
    _attributes = GENERAL_BUFFS[4761].all_attributes
    rate = 10


class WindPendant(EquipmentGain):
    buff_ids = [29268]
    _attributes = GENERAL_BUFFS[29268].all_attributes
    rate = 15 / 180


class TankPendant(EquipmentGain):
    skill_ids = [38787]


class 大附魔帽(EquipmentGain):
    # buff_ids = [15436]
    _attributes = GENERAL_BUFFS[15436].all_attributes


class 大附魔衣(EquipmentGain):
    _attributes = [
        dict(physical_attack_power_base=physical_attack_power_base, magical_attack_power_base=magical_attack_power_base)
        for physical_attack_power_base, magical_attack_power_base in
        zip(GENERAL_SKILLS[22151].physical_attack_power_base, GENERAL_SKILLS[22151].magical_attack_power_base)
    ]


class 大附魔腰(EquipmentGain):
    buff_ids = [15455]
    _attributes = [GENERAL_BUFFS[15455].get_attributes(weights=[3, 7])]
    rate = 8 / 30


class 大附魔腕(EquipmentGain):
    skill_ids = [37562]
    _damage_base = [244355, 281280]


class 大附魔鞋(EquipmentGain):
    skill_ids = [37561]
    _damage_base = [162903, 187520]


class TertiaryWeaponGain(EquipmentGain):
    skill_ids = [38966]
    _damage_base = [86500, 90000]


class HatGain(EquipmentGain):
    attr_level: int

    buff_ids = [29519]
    _attributes = GENERAL_BUFFS[29519].all_attributes

    @property
    def attributes(self):
        level = self.level * 3 + self.attr_level
        return self._attributes[level - 1]

    def add_attribute(self, attribute: Attribute):
        max_value = max(attribute.max_overcome_base, attribute.max_critical_strike_base, attribute.surplus)
        if attribute.max_overcome_base == max_value:
            self.attr_level = -2
        elif attribute.max_critical_strike_base == max_value:
            self.attr_level = -1
        else:
            self.attr_level = 0
        super().add_attribute(attribute)


class PendantGain(EquipmentGain):
    rate = 5


class OvercomePendantGain(PendantGain):
    buff_ids = [29536]
    _attributes = GENERAL_BUFFS[29536].all_attributes


class CriticalPendantGain(PendantGain):
    buff_ids = [29537]
    _attributes = GENERAL_BUFFS[29537].all_attributes


class NecklaceGain(EquipmentGain):
    scales: List[int]

    @property
    def scale(self):
        return self.scales[self.level - 1]


class OvercomeNecklaceGain(NecklaceGain):
    scales = [5427, 5648]
    buff_ids = [29529]

    def add_attribute(self, attribute: Attribute):
        self.rate = min(int(attribute.max_overcome_base / self.scale), GENERAL_BUFFS[29529].max_stack)
        super().add_attribute(attribute)


class CriticalNecklaceGain(NecklaceGain):
    scales = [4748, 4942]
    buff_ids = [29528]

    def add_attribute(self, attribute: Attribute):
        self.rate = min(int(attribute.max_critical_strike_base / self.scale), GENERAL_BUFFS[29528].max_stack)
        super().add_attribute(attribute)


class ShoesGain(EquipmentGain):
    rate = 10 / 20


class OvercomeShoesGain(ShoesGain):
    buff_ids = [29526]
    _attributes = GENERAL_BUFFS[29526].all_attributes


class CriticalShoesGain(ShoesGain):
    buff_ids = [29524]
    _attributes = GENERAL_BUFFS[29524].all_attributes


class WinterWeaponGain(EquipmentGain):
    buff_ids = [18792]
    _attributes = GENERAL_BUFFS[18792].all_attributes
    rate = 6 / 30


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
        for i in range(GENERAL_BUFFS[29268].max_level)
    },
    (38786, 1): TankPendant(),
    **{
        (15436, i + 1): 大附魔帽(i + 1)
        for i in range(GENERAL_BUFFS[15436].max_level)
    },
    **{
        (22151, i + 1): 大附魔衣(i + 1)
        for i in range(GENERAL_SKILLS[22151].max_level)
    },
    **{
        tuple(gain_key): 大附魔腰()
        for gain_key in SPECIAL_ENCHANT_MAP[6].values()
    },
    **{
        tuple(gain_key): 大附魔腕(i + 1)
        for i, gain_key in enumerate(SPECIAL_ENCHANT_MAP[10].values())
    },
    **{
        tuple(gain_key): 大附魔鞋(i + 1)
        for i, gain_key in enumerate(SPECIAL_ENCHANT_MAP[9].values())
    },
    **{
        (gain_id,): TertiaryWeaponGain(i + 1)
        for i, gain_id in enumerate((2701, 2706))
    },
    **{
        (gain_id,): HatGain(i + 1)
        for i, gain_id in enumerate((2698, 2703))
    },
    **{
        (gain_id,): OvercomePendantGain(i + 1)
        for i, gain_id in enumerate((2700, 2705))
    },
    **{
        (gain_id,): CriticalPendantGain(i + 1)
        for i, gain_id in enumerate((2711, 2712))
    },
    **{
        (gain_id,): OvercomeNecklaceGain(i + 1)
        for i, gain_id in enumerate((2699, 2704))
    },
    **{
        (gain_id,): CriticalNecklaceGain(i + 1)
        for i, gain_id in enumerate((2707, 2708))
    },
    **{
        (gain_id,): OvercomeShoesGain(i + 1)
        for i, gain_id in enumerate((2697, 2702))
    },
    **{
        (gain_id,): CriticalShoesGain(i + 1)
        for i, gain_id in enumerate((2709, 2710))
    },
    **{
        (gain_id,): Gain()
        for gain_id in (1194, 2727)
    },
    **{
        (gain_id,): DivineGain(i + 1)
        for i, gain_id in enumerate((2763, 2764, 2765, 2766, 2732))
    },
    (2770,): WinterWeaponGain(),
    (26060, 5): Gain(),
}
