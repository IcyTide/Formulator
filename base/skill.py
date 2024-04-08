from base.attribute import Attribute
from base.constant import *
from base.damage import *

from typing import List, Union
from dataclasses import dataclass


@dataclass
class Skill:
    skill_id: int
    skill_name: str
    skill_level: int = 0
    
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

    _skill_damage_addition: int = 0
    _skill_shield_gain: Union[List[int], int] = 0
    _skill_critical_strike: int = 0
    _skill_critical_power: int = 0

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
            return self._attack_power_cof[self.skill_level - 1]
        else:
            return self._attack_power_cof

    @attack_power_cof.setter
    def attack_power_cof(self, attack_power_cof):
        self._attack_power_cof = attack_power_cof

    @property
    def surplus_cof(self):
        if isinstance(self._surplus_cof, list):
            cof = self._surplus_cof[self.skill_level - 1]
        else:
            cof = self._surplus_cof
        return ((cof + int(cof < 0)) / BINARY_SCALE + BINARY_SCALE) / BINARY_SCALE * SURPLUS_SCALE

    @surplus_cof.setter
    def surplus_cof(self, surplus_cof):
        self._surplus_cof = surplus_cof

    @property
    def weapon_damage_cof(self):
        if isinstance(self._weapon_damage_cof, list):
            return self._weapon_damage_cof[self.skill_level - 1] / BINARY_SCALE
        else:
            return self._weapon_damage_cof / BINARY_SCALE

    @weapon_damage_cof.setter
    def weapon_damage_cof(self, weapon_damage_cof):
        self._weapon_damage_cof = weapon_damage_cof

    @property
    def skill_damage_addition(self):
        return self._skill_damage_addition / BINARY_SCALE

    @skill_damage_addition.setter
    def skill_damage_addition(self, skill_damage_addition):
        self._skill_damage_addition = skill_damage_addition

    @property
    def skill_shield_gain(self):
        if isinstance(self._skill_shield_gain, list):
            return self._skill_shield_gain[self.skill_level - 1] / BINARY_SCALE
        else:
            return self._skill_shield_gain / BINARY_SCALE

    @skill_shield_gain.setter
    def skill_shield_gain(self, skill_shield_gain):
        self._skill_shield_gain = skill_shield_gain

    @property
    def skill_critical_strike(self):
        return self._skill_critical_strike / DECIMAL_SCALE

    @skill_critical_strike.setter
    def skill_critical_strike(self, skill_critical_strike):
        self._skill_critical_strike = skill_critical_strike

    @property
    def skill_critical_power(self):
        return self._skill_critical_power / BINARY_SCALE

    @skill_critical_power.setter
    def skill_critical_power(self, skill_critical_power):
        self._skill_critical_power = skill_critical_power

    def __call__(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, self.damage_rand, self.damage_gain,
            self.attack_power_cof, self.attack_power_cof_gain, attribute.attack_power,
            self.weapon_damage_cof, self.weapon_damage_cof_gain, attribute.weapon_damage,
            self.surplus_cof, self.surplus_cof_gain, attribute.surplus
        )

        damage = damage_addition_result(damage, attribute.damage_addition + self.skill_damage_addition)
        damage = overcome_result(damage, attribute.overcome,
                                 attribute.shield_base,
                                 attribute.shield_gain + self.skill_shield_gain,
                                 attribute.shield_ignore,
                                 attribute.shield_constant)

        critical_damage = critical_result(damage, attribute.critical_power + self.skill_critical_power)

        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.strain)
        critical_damage = strain_result(critical_damage, attribute.strain)
        damage = pve_addition_result(damage, attribute.pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition)
        damage = vulnerable_result(damage, attribute.vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.vulnerable)
        critical_strike = min(1, attribute.critical_strike + self.skill_critical_strike)

        expected_damage = critical_strike * critical_damage + (1 - critical_strike) * damage

        return damage, critical_damage, expected_damage
    
    
class PhysicalDamage(Skill):
    @property
    def attack_power_cof(self):
        return PHYSICAL_ATTACK_POWER_COF(super().attack_power_cof + self.interval)

    @attack_power_cof.setter
    def attack_power_cof(self, attack_power_cof):
        self._attack_power_cof = attack_power_cof


class MagicalDamage(Skill):
    @property
    def attack_power_cof(self):
        return MAGICAL_ATTACK_POWER_COF(super().attack_power_cof + self.interval)


class PhysicalDotDamage(Skill):
    @property
    def attack_power_cof(self):
        return PHYSICAL_DOT_ATTACK_POWER_COF(super().attack_power_cof, self.interval)

    @attack_power_cof.setter
    def attack_power_cof(self, attack_power_cof):
        self._attack_power_cof = attack_power_cof


class MagicalDotDamage(Skill):
    @property
    def attack_power_cof(self):
        return MAGICAL_DOT_ATTACK_POWER_COF(super().attack_power_cof, self.interval)
