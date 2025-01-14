from typing import Dict

from assets.attributes import ATTRIBUTES
from base.constant import *


class Shield:
    level: int = list(SHIELD_BASE_MAP)[-1]

    physical_shield_base: int = 0
    _magical_shield_base: int = 0
    solar_shield_base: int = 0
    lunar_shield_base: int = 0
    neutral_shield_base: int = 0
    poison_shield_base: int = 0

    physical_shield_gain: int = 0
    solar_shield_gain: int = 0
    lunar_shield_gain: int = 0
    neutral_shield_gain: int = 0
    poison_shield_gain: int = 0

    @property
    def level_shield_base(self):
        return SHIELD_BASE_MAP[self.level]

    @property
    def shield_constant(self):
        return SHIELD_CONSTANT_MAP[self.level]

    @property
    def magical_shield_base(self):
        return self._magical_shield_base

    @magical_shield_base.setter
    def magical_shield_base(self, magical_shield_base):
        residual = magical_shield_base - self._magical_shield_base
        self.solar_shield_base += residual
        self.lunar_shield_base += residual
        self.neutral_shield_base += residual
        self.poison_shield_base += residual
        self._magical_shield_base = magical_shield_base

    @property
    def physical_shield(self):
        shield_base = int(self.level_shield_base + self.physical_shield_base)
        return int(shield_base * (1 + self.physical_shield_gain / BINARY_SCALE))

    @property
    def solar_shield(self):
        shield_base = int(self.level_shield_base + self.solar_shield_base)
        return int(shield_base * (1 + self.solar_shield_gain / BINARY_SCALE))

    @property
    def lunar_shield(self):
        shield_base = int(self.level_shield_base + self.lunar_shield_base)
        return int(shield_base * (1 + self.lunar_shield_gain / BINARY_SCALE))

    @property
    def neutral_shield(self):
        shield_base = int(self.level_shield_base + self.neutral_shield_base)
        return int(shield_base * (1 + self.neutral_shield_gain / BINARY_SCALE))

    @property
    def poison_shield(self):
        shield_base = int(self.level_shield_base + self.poison_shield_base)
        return int(shield_base * (1 + self.poison_shield_gain / BINARY_SCALE))


class DamageCoefficient:
    _all_damage_cof: int = 0
    physical_damage_cof: int = 0
    solar_damage_cof: int = 0
    lunar_damage_cof: int = 0
    neutral_damage_cof: int = 0
    poison_damage_cof: int = 0

    @property
    def all_damage_cof(self):
        return self._all_damage_cof

    @all_damage_cof.setter
    def all_damage_cof(self, all_damage_cof):
        residual = all_damage_cof - self._all_damage_cof
        self.physical_damage_cof += residual
        self.solar_damage_cof += residual
        self.lunar_damage_cof += residual
        self.neutral_damage_cof += residual
        self.poison_damage_cof += residual
        self._all_damage_cof = all_damage_cof


class BaseMajor:
    _all_major_base: int = 0
    agility_base: int = 0
    agility_gain: int = 0
    strength_base: int = 0
    strength_gain: int = 0
    spirit_base: int = 0
    spirit_gain: int = 0
    spunk_base: int = 0
    spunk_gain: int = 0

    @property
    def all_major_base(self):
        return self._all_major_base

    @all_major_base.setter
    def all_major_base(self, all_major_base):
        residual = all_major_base - self._all_major_base
        self.agility_base += residual
        self.strength_base += residual
        self.spirit_base += residual
        self.spunk_base += residual
        self._all_major_base = all_major_base

    @property
    def agility(self):
        return int(self.agility_base * (1 + self.agility_gain / BINARY_SCALE))

    @property
    def strength(self):
        return int(self.strength_base * (1 + self.strength_gain / BINARY_SCALE))

    @property
    def spirit(self):
        return int(self.spirit_base * (1 + self.spirit_gain / BINARY_SCALE))

    @property
    def spunk(self):
        return int(self.spunk_base * (1 + self.spunk_gain / BINARY_SCALE))

    @property
    def agility_critical_strike_base(self):
        return int(self.agility * AGILITY_TO_CRITICAL_STRIKE)

    @property
    def strength_attack_power_base(self):
        return int(self.strength * STRENGTH_TO_ATTACK_POWER)

    @property
    def strength_overcome_base(self):
        return int(self.strength * STRENGTH_TO_OVERCOME)

    @property
    def spirit_critical_strike_base(self):
        return int(self.spirit * SPIRIT_TO_CRITICAL_STRIKE)

    @property
    def spunk_attack_power_base(self):
        return int(self.spunk * SPUNK_TO_ATTACK_POWER)

    @property
    def spunk_overcome_base(self):
        return int(self.spunk * SPUNK_TO_OVERCOME)


class Therapy(BaseMajor):
    therapy_base: int = 0


class AttackPower(BaseMajor):
    physical_attack_power_base: int = 0
    _magical_attack_power_base: int = 0
    _solar_and_lunar_attack_power_base: int = 0
    solar_attack_power_base: int = 0
    lunar_attack_power_base: int = 0
    neutral_attack_power_base: int = 0
    poison_attack_power_base: int = 0

    physical_attack_power_gain: int = 0
    _magical_attack_power_gain: int = 0
    solar_attack_power_gain: int = 0
    lunar_attack_power_gain: int = 0
    neutral_attack_power_gain: int = 0
    poison_attack_power_gain: int = 0

    @property
    def attack_power(self):
        raise NotImplementedError

    @property
    def base_physical_attack_power(self):
        return int(self.physical_attack_power_base + self.strength_attack_power_base)

    @property
    def extra_physical_attack_power(self):
        return 0

    @property
    def physical_attack_power(self):
        attack_power = int(self.base_physical_attack_power * (1 + self.physical_attack_power_gain / BINARY_SCALE))
        return int(attack_power + self.extra_physical_attack_power)

    @property
    def magical_attack_power_base(self):
        return self._magical_attack_power_base

    @magical_attack_power_base.setter
    def magical_attack_power_base(self, magical_attack_power_base):
        residual = magical_attack_power_base - self._magical_attack_power_base
        self.solar_attack_power_base += residual
        self.lunar_attack_power_base += residual
        self.neutral_attack_power_base += residual
        self.poison_attack_power_base += residual
        self._magical_attack_power_base = magical_attack_power_base

    @property
    def magical_attack_power_gain(self):
        return self._magical_attack_power_gain

    @magical_attack_power_gain.setter
    def magical_attack_power_gain(self, magical_attack_power_gain):
        residual = magical_attack_power_gain - self._magical_attack_power_gain
        self.solar_attack_power_gain += residual
        self.lunar_attack_power_gain += residual
        self.neutral_attack_power_gain += residual
        self.poison_attack_power_gain += residual
        self._magical_attack_power_gain = magical_attack_power_gain

    @property
    def solar_and_lunar_attack_power_base(self):
        return self._solar_and_lunar_attack_power_base

    @solar_and_lunar_attack_power_base.setter
    def solar_and_lunar_attack_power_base(self, solar_and_lunar_attack_power_base):
        residual = solar_and_lunar_attack_power_base - self._solar_and_lunar_attack_power_base
        self.solar_attack_power_base += residual
        self.lunar_attack_power_base += residual
        self._solar_and_lunar_attack_power_base = solar_and_lunar_attack_power_base

    @property
    def base_solar_attack_power(self):
        return int(self.solar_attack_power_base + self.spunk_attack_power_base)

    @property
    def extra_solar_attack_power(self):
        return 0

    @property
    def solar_attack_power(self):
        attack_power = int(self.base_solar_attack_power * (1 + self.solar_attack_power_gain / BINARY_SCALE))
        return int(attack_power + self.extra_solar_attack_power)

    @property
    def base_lunar_attack_power(self):
        return int(self.lunar_attack_power_base + self.spunk_attack_power_base)

    @property
    def extra_lunar_attack_power(self):
        return 0

    @property
    def lunar_attack_power(self):
        attack_power = int(self.base_lunar_attack_power * (1 + self.lunar_attack_power_gain / BINARY_SCALE))
        return int(attack_power + self.extra_lunar_attack_power)

    @property
    def base_neutral_attack_power(self):
        return int(self.neutral_attack_power_base + self.spunk_attack_power_base)

    @property
    def extra_neutral_attack_power(self):
        return 0

    @property
    def neutral_attack_power(self):
        attack_power = int(self.base_neutral_attack_power * (1 + self.neutral_attack_power_gain / BINARY_SCALE))
        return int(attack_power + self.extra_neutral_attack_power)

    @property
    def base_poison_attack_power(self):
        return int(self.poison_attack_power_base + self.spunk_attack_power_base)

    @property
    def extra_poison_attack_power(self):
        return 0

    @property
    def poison_attack_power(self):
        attack_power = int(self.base_poison_attack_power * (1 + self.poison_attack_power_gain / BINARY_SCALE))
        return int(attack_power + self.extra_poison_attack_power)


class CriticalStrike(BaseMajor):
    _all_critical_strike_base: int = 0
    physical_critical_strike_base: int = 0
    _magical_critical_strike_base: int = 0
    _solar_and_lunar_critical_strike_base: int = 0
    solar_critical_strike_base: int = 0
    lunar_critical_strike_base: int = 0
    neutral_critical_strike_base: int = 0
    poison_critical_strike_base: int = 0

    physical_critical_strike_rate: int = 0
    solar_critical_strike_rate: int = 0
    lunar_critical_strike_rate: int = 0
    neutral_critical_strike_rate: int = 0
    poison_critical_strike_rate: int = 0

    @property
    def critical_strike(self):
        raise NotImplementedError

    @property
    def max_critical_strike_base(self):
        return max(
            self.physical_critical_strike_base,
            self.solar_critical_strike_base,
            self.lunar_critical_strike_base,
            self.neutral_critical_strike_base,
            self.poison_critical_strike_base
        )

    @property
    def all_critical_strike_base(self):
        return self._all_critical_strike_base

    @all_critical_strike_base.setter
    def all_critical_strike_base(self, all_critical_strike_base):
        residual = all_critical_strike_base - self._all_critical_strike_base
        self.physical_critical_strike_base += residual
        self.magical_critical_strike_base += residual
        self._all_critical_strike_base = all_critical_strike_base

    @property
    def base_physical_critical_strike(self):
        return int(self.physical_critical_strike_base + self.agility_critical_strike_base)

    @property
    def extra_physical_critical_strike(self):
        return 0

    @property
    def final_physical_critical_strike(self):
        return int(self.base_physical_critical_strike + self.extra_physical_critical_strike)

    @property
    def physical_critical_strike_percent(self):
        return self.final_physical_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def physical_critical_strike(self):
        return self.physical_critical_strike_percent + self.physical_critical_strike_rate / DECIMAL_SCALE

    @property
    def magical_critical_strike_base(self):
        return self._magical_critical_strike_base

    @magical_critical_strike_base.setter
    def magical_critical_strike_base(self, magical_critical_strike_base):
        residual = magical_critical_strike_base - self._magical_critical_strike_base
        self.solar_critical_strike_base += residual
        self.lunar_critical_strike_base += residual
        self.neutral_critical_strike_base += residual
        self.poison_critical_strike_base += residual
        self._magical_critical_strike_base = magical_critical_strike_base

    @property
    def solar_and_lunar_critical_strike_base(self):
        return self._solar_and_lunar_critical_strike_base

    @solar_and_lunar_critical_strike_base.setter
    def solar_and_lunar_critical_strike_base(self, solar_and_lunar_critical_strike_base):
        residual = solar_and_lunar_critical_strike_base - self._solar_and_lunar_critical_strike_base
        self.solar_critical_strike_base += residual
        self.lunar_critical_strike_base += residual
        self._solar_and_lunar_critical_strike_base = solar_and_lunar_critical_strike_base

    @property
    def base_solar_critical_strike(self):
        return int(self.solar_critical_strike_base + self.spirit_critical_strike_base)

    @property
    def extra_solar_critical_strike(self):
        return 0

    @property
    def final_solar_critical_strike(self):
        return int(self.base_solar_critical_strike + self.extra_solar_critical_strike)

    @property
    def solar_critical_strike_percent(self):
        return self.final_solar_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def solar_critical_strike(self):
        return self.solar_critical_strike_percent + self.solar_critical_strike_rate / DECIMAL_SCALE

    @property
    def base_lunar_critical_strike(self):
        return int(self.lunar_critical_strike_base + self.spirit_critical_strike_base)

    @property
    def extra_lunar_critical_strike(self):
        return 0

    @property
    def final_lunar_critical_strike(self):
        return int(self.base_lunar_critical_strike + self.extra_lunar_critical_strike)

    @property
    def lunar_critical_strike_percent(self):
        return self.final_lunar_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def lunar_critical_strike(self):
        return self.lunar_critical_strike_percent + self.lunar_critical_strike_rate / DECIMAL_SCALE

    @property
    def base_neutral_critical_strike(self):
        return int(self.neutral_critical_strike_base + self.spirit_critical_strike_base)

    @property
    def extra_neutral_critical_strike(self):
        return 0

    @property
    def final_neutral_critical_strike(self):
        return int(self.base_neutral_critical_strike + self.extra_neutral_critical_strike)

    @property
    def neutral_critical_strike_percent(self):
        return self.final_neutral_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def neutral_critical_strike(self):
        return self.neutral_critical_strike_percent + self.neutral_critical_strike_rate / DECIMAL_SCALE

    @property
    def base_poison_critical_strike(self):
        return int(self.poison_critical_strike_base + self.spirit_critical_strike_base)

    @property
    def extra_poison_critical_strike(self):
        return 0

    @property
    def final_poison_critical_strike(self):
        return int(self.base_poison_critical_strike + self.extra_poison_critical_strike)

    @property
    def poison_critical_strike_percent(self):
        return self.final_poison_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def poison_critical_strike(self):
        return self.poison_critical_strike_percent + self.poison_critical_strike_rate / DECIMAL_SCALE


class Overcome(BaseMajor):
    physical_overcome_base: int = 0
    _magical_overcome_base: int = 0
    _solar_and_lunar_overcome_base: int = 0
    solar_overcome_base: int = 0
    lunar_overcome_base: int = 0
    neutral_overcome_base: int = 0
    poison_overcome_base: int = 0

    physical_overcome_gain: int = 0
    solar_overcome_gain: int = 0
    lunar_overcome_gain: int = 0
    neutral_overcome_gain: int = 0
    poison_overcome_gain: int = 0

    @property
    def overcome(self):
        raise NotImplementedError

    @property
    def max_overcome_base(self):
        return max(
            self.physical_overcome_base,
            self.solar_overcome_base,
            self.lunar_overcome_base,
            self.neutral_overcome_base,
            self.poison_overcome_base
        )

    @property
    def base_physical_overcome(self):
        return int(self.physical_overcome_base + self.strength_overcome_base)

    @property
    def extra_physical_overcome(self):
        return 0

    @property
    def final_physical_overcome(self):
        overcome = int(self.base_physical_overcome * (1 + self.physical_overcome_gain / BINARY_SCALE))
        return int(overcome + self.extra_physical_overcome)

    @property
    def physical_overcome(self):
        return self.final_physical_overcome / OVERCOME_SCALE

    @property
    def magical_overcome_base(self):
        return self._magical_overcome_base

    @magical_overcome_base.setter
    def magical_overcome_base(self, magical_overcome_base):
        residual = magical_overcome_base - self._magical_overcome_base
        self.solar_overcome_base += residual
        self.lunar_overcome_base += residual
        self.neutral_overcome_base += residual
        self.poison_overcome_base += residual
        self._magical_overcome_base = magical_overcome_base

    @property
    def solar_and_lunar_overcome_base(self):
        return self._solar_and_lunar_overcome_base

    @solar_and_lunar_overcome_base.setter
    def solar_and_lunar_overcome_base(self, solar_and_lunar_overcome_base):
        residual = solar_and_lunar_overcome_base - self._solar_and_lunar_overcome_base
        self.solar_overcome_base += residual
        self.lunar_overcome_base += residual
        self._solar_and_lunar_overcome_base = solar_and_lunar_overcome_base

    @property
    def base_solar_overcome(self):
        return int(self.solar_overcome_base + self.spunk_overcome_base)

    @property
    def extra_solar_overcome(self):
        return 0

    @property
    def final_solar_overcome(self):
        overcome = int(self.base_solar_overcome * (1 + self.solar_overcome_gain / BINARY_SCALE))
        return int(overcome + self.extra_solar_overcome)

    @property
    def solar_overcome(self):
        return self.final_solar_overcome / OVERCOME_SCALE

    @property
    def base_lunar_overcome(self):
        return int(self.lunar_overcome_base + self.spunk_overcome_base)

    @property
    def extra_lunar_overcome(self):
        return 0

    @property
    def final_lunar_overcome(self):
        overcome = int(self.base_lunar_overcome * (1 + self.lunar_overcome_gain / BINARY_SCALE))
        return int(overcome + self.extra_lunar_overcome)

    @property
    def lunar_overcome(self):
        return self.final_lunar_overcome / OVERCOME_SCALE

    @property
    def base_neutral_overcome(self):
        return int(self.neutral_overcome_base + self.spunk_overcome_base)

    @property
    def extra_neutral_overcome(self):
        return 0

    @property
    def final_neutral_overcome(self):
        overcome = int(self.base_neutral_overcome * (1 + self.neutral_overcome_gain / BINARY_SCALE))
        return int(overcome + self.extra_neutral_overcome)

    @property
    def neutral_overcome(self):
        return self.final_neutral_overcome / OVERCOME_SCALE

    @property
    def base_poison_overcome(self):
        return int(self.poison_overcome_base + self.spunk_overcome_base)

    @property
    def extra_poison_overcome(self):
        return 0

    @property
    def final_poison_overcome(self):
        overcome = int(self.base_poison_overcome * (1 + self.poison_overcome_gain / BINARY_SCALE))
        return int(overcome + self.extra_poison_overcome)

    @property
    def poison_overcome(self):
        return self.final_poison_overcome / OVERCOME_SCALE


class Major(Therapy, AttackPower, CriticalStrike, Overcome):
    @property
    def major(self):
        raise NotImplementedError


class Vitality:
    vitality_base: int = 0
    max_life_base: int = 0
    max_life_add: int = 0


class CriticalPower:
    _all_critical_power_base: int = 0
    physical_critical_power_base: int = 0
    _magical_critical_power_base: int = 0
    _solar_and_lunar_critical_power_base: int = 0
    solar_critical_power_base: int = 0
    lunar_critical_power_base: int = 0
    neutral_critical_power_base: int = 0
    poison_critical_power_base: int = 0

    physical_critical_power_rate: int = 0
    _magical_critical_power_rate: int = 0
    solar_critical_power_rate: int = 0
    lunar_critical_power_rate: int = 0
    neutral_critical_power_rate: int = 0
    poison_critical_power_rate: int = 0

    @property
    def critical_power(self):
        raise NotImplementedError

    @property
    def all_critical_power_base(self):
        return self._all_critical_power_base

    @all_critical_power_base.setter
    def all_critical_power_base(self, all_critical_power_base):
        residual = all_critical_power_base - self._all_critical_power_base
        self.physical_critical_power_base += residual
        self.magical_critical_power_base += residual
        self._all_critical_power_base = all_critical_power_base

    @property
    def extra_physical_critical_power(self):
        return self.physical_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def physical_critical_power_percent(self):
        return BASE_CRITICAL_POWER + self.extra_physical_critical_power

    @property
    def physical_critical_power(self):
        return self.physical_critical_power_percent + self.physical_critical_power_rate / BINARY_SCALE

    @property
    def magical_critical_power_base(self):
        return self._magical_critical_power_base

    @magical_critical_power_base.setter
    def magical_critical_power_base(self, magical_critical_power_base):
        residual = magical_critical_power_base - self._magical_critical_power_base
        self.solar_critical_power_base += residual
        self.lunar_critical_power_base += residual
        self.neutral_critical_power_base += residual
        self.poison_critical_power_base += residual
        self._magical_critical_power_base = magical_critical_power_base

    @property
    def magical_critical_power_rate(self):
        return self._magical_critical_power_rate

    @magical_critical_power_rate.setter
    def magical_critical_power_rate(self, magical_critical_power_rate):
        residual = magical_critical_power_rate - self._magical_critical_power_rate
        self.solar_critical_power_rate += residual
        self.lunar_critical_power_rate += residual
        self.neutral_critical_power_rate += residual
        self.poison_critical_power_rate += residual
        self._magical_critical_power_rate = magical_critical_power_rate

    @property
    def solar_and_lunar_critical_power_base(self):
        return self._solar_and_lunar_critical_power_base

    @solar_and_lunar_critical_power_base.setter
    def solar_and_lunar_critical_power_base(self, solar_and_lunar_critical_power_base):
        residual = solar_and_lunar_critical_power_base - self._solar_and_lunar_critical_power_base
        self.solar_critical_power_base += residual
        self.lunar_critical_power_base += residual
        self._solar_and_lunar_critical_power_base = solar_and_lunar_critical_power_base

    @property
    def extra_solar_critical_power(self):
        return self.solar_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def solar_critical_power_percent(self):
        return BASE_CRITICAL_POWER + self.extra_solar_critical_power

    @property
    def solar_critical_power(self):
        return self.solar_critical_power_percent + self.solar_critical_power_rate / BINARY_SCALE

    @property
    def extra_lunar_critical_power(self):
        return self.lunar_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def lunar_critical_power_percent(self):
        return BASE_CRITICAL_POWER + self.extra_lunar_critical_power

    @property
    def lunar_critical_power(self):
        return self.lunar_critical_power_percent + self.lunar_critical_power_rate / BINARY_SCALE

    @property
    def extra_neutral_critical_power(self):
        return self.neutral_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def neutral_critical_power_percent(self):
        return BASE_CRITICAL_POWER + self.extra_neutral_critical_power

    @property
    def neutral_critical_power(self):
        return self.neutral_critical_power_percent + self.neutral_critical_power_rate / BINARY_SCALE

    @property
    def extra_poison_critical_power(self):
        return self.poison_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def poison_critical_power_percent(self):
        return BASE_CRITICAL_POWER + self.extra_poison_critical_power

    @property
    def poison_critical_power(self):
        return self.poison_critical_power_percent + self.poison_critical_power_rate / BINARY_SCALE


class DamageAddition:
    _all_damage_addition: int = 0
    physical_damage_addition: int = 0
    magical_damage_addition: int = 0

    @property
    def damage_addition(self):
        raise NotImplementedError

    @property
    def all_damage_addition(self):
        return self._all_damage_addition

    @all_damage_addition.setter
    def all_damage_addition(self, all_damage_addition):
        residual = all_damage_addition - self._all_damage_addition
        self.physical_damage_addition += residual
        self.magical_damage_addition += residual
        self._all_damage_addition = all_damage_addition


class Minor(Vitality, CriticalPower, DamageAddition):
    surplus_base: int = 0
    surplus_gain: int = 0

    strain_base: int = 0
    strain_gain: int = 0
    strain_rate: int = 0

    _pvx_round: int = 0

    haste_base: int = 0  # Not Apply

    weapon_damage_rand: int = 0
    weapon_damage_base: int = 0
    weapon_damage_gain: int = 0

    all_shield_ignore: int = 0

    pve_addition_base: int = 0
    damage_gain: int = 0
    global_damage_factor: float = 1.

    @property
    def surplus(self):
        return int(self.surplus_base * (1 + self.surplus_gain / BINARY_SCALE))

    @property
    def final_strain(self):
        return int(self.strain_base * (1 + self.strain_gain / BINARY_SCALE))

    @property
    def strain(self):
        return self.final_strain / STRAIN_SCALE + self.strain_rate / BINARY_SCALE

    @property
    def haste(self):
        return self.haste_base / HASTE_SCALE

    @property
    def pvx_round(self):
        return self._pvx_round

    @pvx_round.setter
    def pvx_round(self, pvx_round):
        self.surplus_base += int(pvx_round * PVX_TO_SURPLUS) - int(self._pvx_round * PVX_TO_SURPLUS)
        self.strain_base += int(pvx_round * PVX_TO_STRAIN) - int(self._pvx_round * PVX_TO_STRAIN)
        self._pvx_round = pvx_round

    @property
    def base_weapon_damage(self):
        return int(self.weapon_damage_base * (1 + self.weapon_damage_gain / BINARY_SCALE))

    @property
    def weapon_damage(self):
        return self.base_weapon_damage + self.weapon_damage_rand / 2

    @property
    def extra_pve_addition(self):
        return 0

    @property
    def pve_addition(self):
        return self.pve_addition_base + self.extra_pve_addition


class Target(Shield, DamageCoefficient):
    resist_critical_strike_rate: int = 0

    @property
    def resist_critical_strike(self):
        return self.resist_critical_strike_rate / DECIMAL_SCALE

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)


class Attribute(Major, Minor, Target):
    level: int = LEVEL
    grad_attrs: dict = dict(
        surplus_base=MINOR_DELTA,
        strain_base=MINOR_DELTA,
        pvx_round=PVX_DELTA
    )
    display_attrs: list = ["strain_base", "strain", "haste_base", "haste", "surplus", "base_weapon_damage", "weapon_damage_rand"]
    recipes: list = []
    platform: int = 0

    attribute_id: Dict[int, int] = {}

    def __init__(self, platform: int = 0):
        self.all_major_base += MAJOR_BASE
        self.target = Target()
        self.platform = platform
        self.set_asset()

    def set_asset(self):
        for attr, value in ATTRIBUTES.get(self.attribute_id[self.platform]).items():
            if isinstance(value, list):
                value = value[-1]
            self[attr] = value

    @property
    def level_reduction(self):
        return LEVEL_REDUCTION_MAP[self.target.level]

    @property
    def target_shield(self):
        raise NotImplementedError

    @property
    def target_damage_cof(self):
        raise NotImplementedError


class PhysicalAttribute(Attribute):
    grad_attrs = dict(
        agility_base=MAJOR_DELTA,
        strength_base=MAJOR_DELTA,
        **Attribute.grad_attrs,
        physical_attack_power_base=PHYSICAL_DELTA,
        physical_critical_strike_base=MINOR_DELTA,
        physical_critical_power_base=MINOR_DELTA,
        physical_overcome_base=MINOR_DELTA,
        weapon_damage_base=WEAPON_DELTA
    )
    display_attrs: list = [
        "agility", "strength",
        "base_physical_attack_power", "physical_attack_power",
        "final_physical_critical_strike", "physical_critical_strike",
        "physical_critical_power_base", "physical_critical_power",
        "base_physical_overcome", "final_physical_overcome", "physical_overcome",
        *Attribute.display_attrs
    ]

    @property
    def attack_power(self):
        return self.physical_attack_power

    @property
    def critical_strike(self):
        return self.physical_critical_strike

    @property
    def overcome(self):
        return self.physical_overcome

    @property
    def critical_power(self):
        return self.physical_critical_power

    @property
    def damage_addition(self):
        return self.physical_damage_addition

    @property
    def target_shield(self):
        return self.target.physical_shield

    @property
    def target_damage_cof(self):
        return self.target.physical_damage_cof


class MagicalAttribute(Attribute):
    grad_attrs = dict(
        spirit_base=MAJOR_DELTA,
        spunk_base=MAJOR_DELTA,
        **Attribute.grad_attrs,
        magical_attack_power_base=MAGICAL_DELTA,
        all_critical_strike_base=MINOR_DELTA,
        all_critical_power_base=MINOR_DELTA,
        magical_overcome_base=MINOR_DELTA
    )
    display_attrs: list = ["spirit", "spunk"]

    @property
    def damage_addition(self):
        return self.magical_damage_addition


class SolarAttribute(MagicalAttribute):
    display_attrs: list = [
        *MagicalAttribute.display_attrs,
        "base_solar_attack_power", "solar_attack_power",
        "final_solar_critical_strike", "solar_critical_strike",
        "solar_critical_power_base", "solar_critical_power",
        "base_solar_overcome", "final_solar_overcome", "solar_overcome",
        *Attribute.display_attrs
    ]

    @property
    def attack_power(self):
        return self.solar_attack_power

    @property
    def critical_strike(self):
        return self.solar_critical_strike

    @property
    def overcome(self):
        return self.solar_overcome

    @property
    def critical_power(self):
        return self.solar_critical_power

    @property
    def target_shield(self):
        return self.target.solar_shield

    @property
    def target_damage_cof(self):
        return self.target.solar_damage_cof


class LunarAttribute(MagicalAttribute):
    display_attrs: list = [
        *MagicalAttribute.display_attrs,
        "base_lunar_attack_power", "lunar_attack_power",
        "final_lunar_critical_strike", "lunar_critical_strike",
        "lunar_critical_power_base", "lunar_critical_power",
        "base_lunar_overcome", "final_lunar_overcome", "lunar_overcome",
        *Attribute.display_attrs
    ]

    @property
    def attack_power(self):
        return self.lunar_attack_power

    @property
    def critical_strike(self):
        return self.lunar_critical_strike

    @property
    def overcome(self):
        return self.lunar_overcome

    @property
    def critical_power(self):
        return self.lunar_critical_power

    @property
    def target_shield(self):
        return self.target.lunar_shield

    @property
    def target_damage_cof(self):
        return self.target.lunar_damage_cof


class NeutralAttribute(MagicalAttribute):
    display_attrs: list = [
        *MagicalAttribute.display_attrs,
        "base_neutral_attack_power", "neutral_attack_power",
        "final_neutral_critical_strike", "neutral_critical_strike",
        "neutral_critical_power_base", "neutral_critical_power",
        "base_neutral_overcome", "final_neutral_overcome", "neutral_overcome",
        *Attribute.display_attrs
    ]

    @property
    def attack_power(self):
        return self.neutral_attack_power

    @property
    def critical_strike(self):
        return self.neutral_critical_strike

    @property
    def overcome(self):
        return self.neutral_overcome

    @property
    def critical_power(self):
        return self.neutral_critical_power

    @property
    def target_shield(self):
        return self.target.neutral_shield

    @property
    def target_damage_cof(self):
        return self.target.neutral_damage_cof


class PoisonAttribute(MagicalAttribute):
    display_attrs: list = [
        *MagicalAttribute.display_attrs,
        "base_poison_attack_power", "poison_attack_power",
        "final_poison_critical_strike", "poison_critical_strike",
        "poison_critical_power_base", "poison_critical_power",
        "base_poison_overcome", "final_poison_overcome", "poison_overcome",
        *Attribute.display_attrs
    ]

    @property
    def attack_power(self):
        return self.poison_attack_power

    @property
    def critical_strike(self):
        return self.poison_critical_strike

    @property
    def overcome(self):
        return self.poison_overcome

    @property
    def critical_power(self):
        return self.poison_critical_power

    @property
    def target_shield(self):
        return self.target.poison_shield

    @property
    def target_damage_cof(self):
        return self.target.poison_damage_cof


class HybridAttribute(MagicalAttribute):
    grad_attrs = dict(
        agility_base=MAJOR_DELTA,
        spunk_base=MAJOR_DELTA,
        **Attribute.grad_attrs,
        magical_attack_power_base=MAGICAL_DELTA,
        all_critical_strike_base=MINOR_DELTA,
        all_critical_power_base=MINOR_DELTA,
        magical_overcome_base=MINOR_DELTA
    )
    display_attrs: list = [
        "agility", "spunk",
        "base_poison_attack_power", "poison_attack_power",
        "final_physical_critical_strike", "physical_critical_strike",
        "physical_critical_power_base", "physical_critical_power",
        "base_poison_overcome", "final_poison_overcome", "poison_overcome",
        *Attribute.display_attrs
    ]

    @property
    def attack_power(self):
        return self.poison_attack_power

    @property
    def critical_strike(self):
        return self.physical_critical_strike

    @property
    def overcome(self):
        return self.poison_overcome

    @property
    def critical_power(self):
        return self.physical_critical_power

    @property
    def damage_addition(self):
        return self.magical_damage_addition

    @property
    def target_shield(self):
        return self.target.poison_shield

    @property
    def target_damage_cof(self):
        return self.target.poison_damage_cof
