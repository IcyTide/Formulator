from base.attribute import Attribute
from base.constant import *
from utils.damage import *

from typing import List, Union
from dataclasses import dataclass


@dataclass
class Skill:
    skill_id: int
    skill_name: str
    skill_level: int = 0
    skill_stack: int = 1

    activate: bool = True

    bind_skill: int = None
    max_stack: int = 1
    tick: int = 1

    _damage_base: Union[List[int], int] = 0
    _damage_rand: Union[List[int], int] = 0

    _attack_power_cof: Union[List[float], float] = 0.
    _surplus_cof: Union[List[float], float] = 0.
    _weapon_damage_cof: Union[List[float], float] = 0.

    interval: int = 0

    damage_gain: float = 0.
    attack_power_cof_gain: float = 0.
    surplus_cof_gain: float = 0.
    weapon_damage_cof_gain: float = 0.

    skill_damage_addition: int = 0
    skill_pve_addition: int = 0
    _skill_shield_gain: Union[List[int], int] = 0
    skill_critical_strike: int = 0
    skill_critical_power: int = 0

    @property
    def display_name(self):
        return f"{self.skill_name}#{self.skill_id}-{self.skill_level}-{self.skill_stack}"

    @property
    def damage_base(self):
        if isinstance(self._damage_base, list):
            return self._damage_base[self.skill_level - 1]
        else:
            return self._damage_base

    @damage_base.setter
    def damage_base(self, damage_base):
        self._damage_base = damage_base

    @property
    def damage_rand(self):
        if isinstance(self._damage_rand, list):
            return self._damage_rand[self.skill_level - 1]
        else:
            return self._damage_rand

    @damage_rand.setter
    def damage_rand(self, damage_rand):
        self._damage_rand = damage_rand

    @property
    def attack_power_cof(self):
        if isinstance(self._attack_power_cof, list):
            return int(self._attack_power_cof[self.skill_level - 1] * (1 + self.attack_power_cof_gain))
        else:
            return int(self._attack_power_cof * (1 + self.attack_power_cof_gain))

    @attack_power_cof.setter
    def attack_power_cof(self, attack_power_cof):
        self._attack_power_cof = attack_power_cof

    @property
    def surplus_cof(self):
        if isinstance(self._surplus_cof, list):
            cof = self._surplus_cof[self.skill_level - 1] * (1 + self.surplus_cof_gain)
            return SURPLUS_COF(cof)
        else:
            cof = self._surplus_cof * (1 + self.surplus_cof_gain)
            return SURPLUS_COF(cof) if cof else 0

    @surplus_cof.setter
    def surplus_cof(self, surplus_cof):
        self._surplus_cof = surplus_cof

    @property
    def weapon_damage_cof(self):
        if isinstance(self._weapon_damage_cof, list):
            return self._weapon_damage_cof[self.skill_level - 1] * (1 + self.weapon_damage_cof_gain) / BINARY_SCALE
        else:
            return self._weapon_damage_cof * (1 + self.weapon_damage_cof_gain) / BINARY_SCALE

    @weapon_damage_cof.setter
    def weapon_damage_cof(self, weapon_damage_cof):
        self._weapon_damage_cof = weapon_damage_cof

    @property
    def skill_shield_gain(self):
        if isinstance(self._skill_shield_gain, list):
            return self._skill_shield_gain[self.skill_level - 1]
        else:
            return self._skill_shield_gain

    @skill_shield_gain.setter
    def skill_shield_gain(self, skill_shield_gain):
        self._skill_shield_gain = skill_shield_gain

    @property
    def skill_critical_strike_gain(self):
        return self.skill_critical_strike / DECIMAL_SCALE

    @property
    def skill_critical_power_gain(self):
        return self.skill_critical_power / BINARY_SCALE

    def __call__(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, self.damage_rand, self.damage_gain,
            self.attack_power_cof, attribute.attack_power,
            self.weapon_damage_cof, attribute.weapon_damage,
            self.surplus_cof, attribute.surplus
        ) * self.skill_stack

        damage = damage_addition_result(damage, attribute.damage_addition + self.skill_damage_addition)
        damage = overcome_result(damage, attribute.overcome,
                                 attribute.level_shield_base + attribute.shield_base,
                                 attribute.shield_gain + self.skill_shield_gain,
                                 attribute.shield_ignore,
                                 attribute.shield_constant)

        critical_damage = critical_result(damage, attribute.critical_power + self.skill_critical_power_gain)

        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.strain)
        critical_damage = strain_result(critical_damage, attribute.strain)
        damage = pve_addition_result(damage, attribute.pve_addition + self.skill_pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition + self.skill_pve_addition)
        damage = vulnerable_result(damage, attribute.vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.vulnerable)
        critical_strike = min(1, attribute.critical_strike + self.skill_critical_strike_gain)

        expected_damage = critical_strike * critical_damage + (1 - critical_strike) * damage

        return damage, critical_damage, expected_damage, critical_strike


class DotSkill(Skill):
    pass


class DotConsumeSkill(Skill):
    pass


class Damage(Skill):
    pass


class DotDamage(Damage):
    pass


class PetDamage(Damage):
    pass


class PhysicalDamage(Damage):
    @property
    def attack_power_cof(self):
        return PHYSICAL_ATTACK_POWER_COF(super().attack_power_cof + self.interval)

    @attack_power_cof.setter
    def attack_power_cof(self, attack_power_cof):
        self._attack_power_cof = attack_power_cof


class MagicalDamage(Damage):
    @property
    def attack_power_cof(self):
        return MAGICAL_ATTACK_POWER_COF(super().attack_power_cof + self.interval)


class PhysicalDotDamage(DotDamage):
    @property
    def attack_power_cof(self):
        return PHYSICAL_DOT_ATTACK_POWER_COF(super().attack_power_cof, self.interval)

    @attack_power_cof.setter
    def attack_power_cof(self, attack_power_cof):
        self._attack_power_cof = attack_power_cof


class MagicalDotDamage(DotDamage):
    @property
    def attack_power_cof(self):
        return MAGICAL_DOT_ATTACK_POWER_COF(super().attack_power_cof, self.interval)
