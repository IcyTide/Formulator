from base.constant import *


class Target:
    level: int = list(SHIELD_BASE_MAP)[-1]

    physical_shield_base: int = 0
    magical_shield_base: int = 0
    physical_shield_gain: int = 0
    magical_shield_gain: int = 0

    _all_vulnerable: int = 0
    physical_vulnerable: int = 0
    magical_vulnerable: int = 0

    _all_damage_cof: int = 0
    physical_damage_cof: int = 0
    magical_damage_cof: int = 0

    @property
    def level_shield_base(self):
        return SHIELD_BASE_MAP[self.level]

    @property
    def all_vulnerable(self):
        return self._all_vulnerable

    @all_vulnerable.setter
    def all_vulnerable(self, all_vulnerable):
        residual = all_vulnerable - self._all_vulnerable
        self.physical_vulnerable += residual
        self.magical_vulnerable += residual
        self._all_vulnerable = all_vulnerable

    @property
    def all_damage_cof(self):
        return self._all_damage_cof

    @all_damage_cof.setter
    def all_damage_cof(self, all_damage_cof):
        residual = all_damage_cof - self._all_damage_cof
        self.physical_damage_cof += residual
        self.magical_damage_cof += residual
        self._all_damage_cof = all_damage_cof

    @property
    def shield_constant(self):
        return SHIELD_CONSTANT_MAP[self.level]


class Major:
    _all_major_base: int = 0
    _all_major_gain: int = 0
    agility_base: int = 0
    agility_gain: int = 0
    strength_base: int = 0
    strength_gain: int = 0
    spirit_base: int = 0
    spirit_gain: int = 0
    spunk_base: int = 0
    spunk_gain: int = 0

    physical_attack_power_base: int = 0
    physical_attack_power_gain: int = 0
    magical_attack_power_base: int = 0
    magical_attack_power_gain: int = 0

    _all_critical_strike_base: int = 0
    _all_critical_strike_rate: int = 0

    physical_critical_strike_base: int = 0
    physical_critical_strike_rate: int = 0
    magical_critical_strike_base: int = 0
    magical_critical_strike_rate: int = 0

    physical_overcome_base: int = 0
    physical_overcome_gain: int = 0
    magical_overcome_base: int = 0
    magical_overcome_gain: int = 0

    """ Major Attr Function"""

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
    def all_major_gain(self):
        return self._all_major_gain

    @all_major_gain.setter
    def all_major_gain(self, all_major_gain):
        residual = all_major_gain - self._all_major_gain
        self.agility_gain += residual
        self.strength_gain += residual
        self.spirit_gain += residual
        self.spunk_gain += residual
        self._all_major_gain = all_major_gain

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

    """ Attack Power Function """

    @property
    def attack_power(self):
        raise NotImplementedError

    @property
    def base_physical_attack_power(self):
        return int(self.physical_attack_power_base + self.strength * STRENGTH_TO_ATTACK_POWER)

    @property
    def extra_physical_attack_power(self):
        return 0

    @property
    def physical_attack_power(self):
        return int(self.base_physical_attack_power * (1 + self.physical_attack_power_gain / BINARY_SCALE) +
                   self.extra_physical_attack_power)

    @property
    def base_magical_attack_power(self):
        return int(self.magical_attack_power_base + self.spunk_base * SPUNK_TO_ATTACK_POWER)

    @property
    def extra_magical_attack_power(self):
        return 0

    @property
    def magical_attack_power(self):
        return int(self.base_magical_attack_power * (1 + self.magical_attack_power_gain / BINARY_SCALE) +
                   self.extra_magical_attack_power)

    """ Critical Strike Function"""

    @property
    def critical_strike(self):
        raise NotImplementedError

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
    def all_critical_strike_rate(self):
        return self._all_critical_strike_rate

    @all_critical_strike_rate.setter
    def all_critical_strike_rate(self, all_critical_strike_rate):
        residual = all_critical_strike_rate - self._all_critical_strike_rate
        self.physical_critical_strike_rate += residual
        self.magical_critical_strike_rate += residual
        self._all_critical_strike_rate = all_critical_strike_rate

    @property
    def extra_physical_critical_strike(self):
        return 0

    @property
    def base_physical_critical_strike(self):
        return int(self.physical_critical_strike_base + self.agility * AGILITY_TO_CRITICAL_STRIKE +
                   self.extra_physical_critical_strike)

    @property
    def physical_critical_strike_percent(self):
        return self.base_physical_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def physical_critical_strike(self):
        return self.physical_critical_strike_percent + self.physical_critical_strike_rate / DECIMAL_SCALE

    @property
    def extra_magical_critical_strike(self):
        return 0

    @property
    def base_magical_critical_strike(self):
        return int(self.magical_critical_strike_base + self.extra_magical_critical_strike +
                   self.spirit * SPIRIT_TO_CRITICAL_STRIKE)

    @property
    def magical_critical_strike_percent(self):
        return self.base_magical_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def magical_critical_strike(self):
        return self.magical_critical_strike_percent + self.magical_critical_strike_rate / DECIMAL_SCALE

    """ Overcome Function"""

    @property
    def overcome(self):
        raise NotImplementedError

    @property
    def base_physical_overcome(self):
        return int(self.physical_overcome_base + self.strength * STRENGTH_TO_OVERCOME)

    @property
    def extra_physical_overcome(self):
        return 0

    @property
    def final_physical_overcome(self):
        return int(self.base_physical_overcome * (1 + self.physical_overcome_gain / BINARY_SCALE) +
                   self.extra_physical_overcome)

    @property
    def physical_overcome(self):
        return self.final_physical_overcome / OVERCOME_SCALE

    @property
    def base_magical_overcome(self):
        return int(self.magical_overcome_base + self.spunk * SPUNK_TO_OVERCOME)

    @property
    def extra_magical_overcome(self):
        return 0

    @property
    def final_magical_overcome(self):
        return int(self.base_magical_overcome * (1 + self.magical_overcome_gain / BINARY_SCALE) +
                   self.extra_magical_overcome)

    @property
    def magical_overcome(self):
        return self.final_magical_overcome / OVERCOME_SCALE


class Minor:
    surplus_base: int = 0
    surplus_gain: int = 0

    strain_base: int = 0
    strain_gain: int = 0
    strain_rate: int = 0

    haste_base: int = 0  # Not Apply

    _all_critical_power_base: int = 0
    _all_critical_power_rate: int = 0

    physical_critical_power_base: int = 0
    physical_critical_power_rate: int = 0
    magical_critical_power_base: int = 0
    magical_critical_power_rate: int = 0

    weapon_damage_rand: int = 0
    weapon_damage_base: int = 0
    weapon_damage_gain: int = 0

    _all_shield_ignore: int = 0

    physical_shield_ignore: int = 0
    magical_shield_ignore: int = 0

    _all_damage_addition: int = 0
    physical_damage_addition: int = 0
    magical_damage_addition: int = 0

    pve_addition: int = 0
    damage_gain: int = 0
    global_damage_cof: float = 1.

    """ Minor Function """

    @property
    def surplus(self):
        return int(self.surplus_base * (1 + self.surplus_gain / BINARY_SCALE))

    @property
    def final_strain(self):
        return int(self.strain_base * (1 + self.strain_gain / BINARY_SCALE))

    @property
    def strain(self):
        return self.final_strain / STRAIN_SCALE + self.strain_rate / BINARY_SCALE

    """ Critical Power Function"""

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
    def all_critical_power_rate(self):
        return self._all_critical_power_rate

    @all_critical_power_rate.setter
    def all_critical_power_rate(self, all_critical_power_rate):
        residual = all_critical_power_rate - self._all_critical_power_rate
        self.physical_critical_power_rate += residual
        self.magical_critical_power_rate += residual
        self._all_critical_power_rate = all_critical_power_rate

    @property
    def base_physical_critical_power(self):
        return self.physical_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def physical_critical_power_percent(self):
        return BASE_CRITICAL_POWER + self.base_physical_critical_power

    @property
    def physical_critical_power(self):
        return self.physical_critical_power_percent + self.physical_critical_power_rate / BINARY_SCALE

    @property
    def base_magical_critical_power(self):
        return self.magical_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def magical_critical_power_percent(self):
        return BASE_CRITICAL_POWER + self.magical_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def magical_critical_power(self):
        return self.magical_critical_power_percent + self.magical_critical_power_rate / BINARY_SCALE

    """ Weapon Skill Function """

    @property
    def base_weapon_damage(self):
        return int(self.weapon_damage_base * (1 + self.weapon_damage_gain / BINARY_SCALE))

    @property
    def weapon_damage(self):
        return self.base_weapon_damage + int(self.weapon_damage_rand / 2)

    """ Others """

    @property
    def shield_ignore(self):
        raise NotImplementedError

    @property
    def all_shield_ignore(self):
        return self._all_shield_ignore

    @all_shield_ignore.setter
    def all_shield_ignore(self, all_shield_ignore):
        residual = all_shield_ignore - self._all_shield_ignore
        self.physical_shield_ignore += residual
        self.magical_shield_ignore += residual
        self._all_shield_ignore = all_shield_ignore

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


class Attribute(Major, Minor, Target):
    level: int = LEVEL
    grad_attrs: dict = None

    def __init__(self):
        self.all_major_base += MAJOR_BASE
        self.all_critical_power_base = 0  # init critical power attr
        self.target = Target()

    @property
    def level_reduction(self):
        return LEVEL_REDUCTION_MAP[self.target.level]

    @property
    def target_shield_base(self):
        raise NotImplementedError

    @property
    def target_shield_gain(self):
        raise NotImplementedError

    @property
    def target_damage_cof(self):
        raise NotImplementedError


class PhysicalAttribute(Attribute):
    grad_attrs = {
        "agility_base": MAJOR_DELTA,
        "strength_base": MAJOR_DELTA,
        "surplus_base": MINOR_DELTA,
        "strain_base": MINOR_DELTA,
        "physical_attack_power_base": PHYSICAL_DELTA,
        "physical_critical_strike_base": MINOR_DELTA,
        "physical_critical_power_base": MINOR_DELTA,
        "physical_overcome_base": MINOR_DELTA,
        "weapon_damage_base": WEAPON_DELTA
    }

    @property
    def attack_power(self):
        return self.physical_attack_power

    @property
    def critical_strike(self):
        return self.physical_critical_strike

    @property
    def critical_power(self):
        return self.physical_critical_power

    @property
    def overcome(self):
        return self.physical_overcome

    @property
    def damage_addition(self):
        return self.physical_damage_addition

    @property
    def shield_ignore(self):
        return self.physical_shield_ignore

    @property
    def target_shield_base(self):
        return self.target.physical_shield_base

    @property
    def target_shield_gain(self):
        return self.target.physical_shield_gain

    @property
    def target_damage_cof(self):
        return self.target.physical_damage_cof


class MagicalAttribute(Attribute):
    grad_attrs = {
        "spirit_base": MAJOR_DELTA,
        "spunk_base": MAJOR_DELTA,
        "surplus_base": MINOR_DELTA,
        "strain_base": MINOR_DELTA,
        "magical_attack_power_base": MAGICAL_DELTA,
        "magical_critical_strike_base": MINOR_DELTA,
        "magical_critical_power_base": MINOR_DELTA,
        "magical_overcome_base": MINOR_DELTA
    }

    @property
    def attack_power(self):
        return self.magical_attack_power

    @property
    def critical_strike(self):
        return self.magical_critical_strike

    @property
    def critical_power(self):
        return self.magical_critical_power

    @property
    def overcome(self):
        return self.magical_overcome

    @property
    def shield_ignore(self):
        return self.magical_shield_ignore

    @property
    def damage_addition(self):
        return self.magical_damage_addition

    @property
    def target_shield_base(self):
        return self.target.magical_shield_base

    @property
    def target_shield_gain(self):
        return self.target.magical_shield_gain

    @property
    def target_damage_cof(self):
        return self.target.magical_damage_cof


class MixingAttribute(Attribute):
    grad_attrs = {
        "agility_base": MAJOR_DELTA,
        "spunk_base": MAJOR_DELTA,
        "surplus_base": MINOR_DELTA,
        "strain_base": MINOR_DELTA,
        "magical_attack_power_base": MAGICAL_DELTA,
        "physical_critical_strike_base": MINOR_DELTA,
        "physical_critical_power_base": MINOR_DELTA,
        "magical_overcome_base": MINOR_DELTA
    }

    @property
    def attack_power(self):
        return self.magical_attack_power

    @property
    def critical_strike(self):
        return self.physical_critical_strike

    @property
    def critical_power(self):
        return self.physical_critical_power

    @property
    def overcome(self):
        return self.magical_overcome

    @property
    def shield_ignore(self):
        return self.magical_shield_ignore

    @property
    def damage_addition(self):
        return self.magical_damage_addition

    @property
    def target_shield_base(self):
        return self.target.magical_shield_base

    @property
    def target_shield_gain(self):
        return self.target.magical_shield_gain

    @property
    def target_damage_cof(self):
        return self.target.magical_damage_cof
