from base.constant import *


class Target:
    target_level: int = 124

    _physical_shield_base: int = 0
    _magical_shield_base: int = 0

    _physical_shield_gain: int = 0
    _magical_shield_gain: int = 0

    _all_vulnerable: float = 0
    _physical_vulnerable: float = 0
    _magical_vulnerable: float = 0

    @property
    def shield_base(self):
        raise NotImplementedError

    @property
    def physical_shield_base(self):
        return SHIELD_BASE_MAP[self.target_level] + self._physical_shield_base

    @physical_shield_base.setter
    def physical_shield_base(self, physical_shield_base):
        self._physical_shield_base = physical_shield_base

    @property
    def magical_shield_base(self):
        return SHIELD_BASE_MAP[self.target_level] + self._magical_shield_base

    @magical_shield_base.setter
    def magical_shield_base(self, magical_shield_base):
        self._magical_shield_base = magical_shield_base

    @property
    def shield_gain(self):
        raise NotImplementedError

    @property
    def physical_shield_gain(self):
        return self._physical_shield_gain / BINARY_SCALE

    @physical_shield_gain.setter
    def physical_shield_gain(self, physical_shield_gain):
        self._physical_shield_gain = physical_shield_gain

    @property
    def magical_shield_gain(self):
        return self._magical_shield_gain / BINARY_SCALE

    @magical_shield_gain.setter
    def magical_shield_gain(self, magical_shield_gain):
        self._magical_shield_gain = magical_shield_gain

    @property
    def vulnerable(self):
        raise NotImplementedError

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
    def physical_vulnerable(self):
        return self._physical_vulnerable / BINARY_SCALE

    @physical_vulnerable.setter
    def physical_vulnerable(self, physical_vulnerable):
        self._physical_vulnerable = physical_vulnerable

    @property
    def magical_vulnerable(self):
        return self._magical_vulnerable / BINARY_SCALE

    @magical_vulnerable.setter
    def magical_vulnerable(self, magical_vulnerable):
        self._magical_vulnerable = magical_vulnerable

    @property
    def shield_constant(self):
        return SHIELD_SCALE * (LEVEL_SCALE * self.target_level - LEVEL_CONSTANT)


class Major:
    _all_major_base: int = 0
    _all_major_gain: int = 0
    _agility_base: int = 0
    _agility_gain: int = 0
    _agility: int = 0
    _strength_base: int = 0
    _strength_gain: int = 0
    _strength: int = 0
    _spirit_base: int = 0
    _spirit_gain: int = 0
    _spirit: int = 0
    _spunk_base: int = 0
    _spunk_gain: int = 0
    _spunk: int = 0

    _physical_attack_power_base: int = 0
    _base_physical_attack_power: int = 0
    _physical_attack_power_gain: int = 0
    _extra_physical_attack_power: int = 0
    _physical_attack_power: int = 0
    _magical_attack_power_base: int = 0
    _base_magical_attack_power: int = 0
    _magical_attack_power_gain: int = 0
    _extra_magical_attack_power: int = 0
    _magical_attack_power: int = 0

    _all_critical_strike_base: int = 0
    _all_critical_strike_gain: int = 0

    _physical_critical_strike_base: int = 0
    _base_physical_critical_strike: int = 0
    _extra_physical_critical_strike: int = 0
    _physical_critical_strike_percent: float = 0
    _physical_critical_strike_gain: int = 0
    _physical_critical_strike: float = 0
    _magical_critical_strike_base: int = 0
    _base_magical_critical_strike: int = 0
    _extra_magical_critical_strike: int = 0
    _magical_critical_strike_percent: float = 0
    _magical_critical_strike_gain: int = 0
    _magical_critical_strike: float = 0

    _physical_overcome_base: int = 0
    _base_physical_overcome: int = 0
    _final_physical_overcome: int = 0
    _physical_overcome_gain: int = 0
    _extra_physical_overcome: int = 0
    _physical_overcome: float = 0
    _magical_overcome_base: int = 0
    _base_magical_overcome: int = 0
    _final_magical_overcome: int = 0
    _magical_overcome_gain: int = 0
    _extra_magical_overcome: int = 0
    _magical_overcome: float = 0

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
    def agility_base(self):
        return self._agility_base

    @agility_base.setter
    def agility_base(self, agility_base):
        self._agility_base = agility_base
        self.agility = agility_base * (1 + self.agility_gain)

    @property
    def agility_gain(self):
        return self._agility_gain / BINARY_SCALE

    @agility_gain.setter
    def agility_gain(self, agility_gain):
        self._agility_gain = agility_gain
        self.agility = self.agility_base * (1 + self.agility_gain)

    @property
    def agility(self):
        return self._agility

    @agility.setter
    def agility(self, agility):
        agility = int(agility)
        self._agility = agility
        self.base_physical_critical_strike = (self.physical_critical_strike_base + self.extra_physical_critical_strike
                                              + agility * AGILITY_TO_CRITICAL_STRIKE)

    @property
    def strength_base(self):
        return self._strength_base

    @strength_base.setter
    def strength_base(self, strength_base):
        self._strength_base = strength_base
        self.strength = strength_base * (1 + self.strength_gain)

    @property
    def strength_gain(self):
        return self._strength_gain / BINARY_SCALE

    @strength_gain.setter
    def strength_gain(self, strength_gain):
        self._strength_gain = strength_gain
        self.strength = self.strength_base * (1 + self.strength_gain)

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        strength = int(strength)
        self._strength = strength
        self.base_physical_attack_power = self.physical_attack_power_base + strength * STRENGTH_TO_ATTACK_POWER
        self.base_physical_overcome = self.physical_overcome_base + strength * STRENGTH_TO_OVERCOME

    @property
    def spirit_base(self):
        return self._spirit_base

    @spirit_base.setter
    def spirit_base(self, spirit_base):
        self._spirit_base = spirit_base
        self.spirit = spirit_base * (1 + self.spirit_gain)

    @property
    def spirit_gain(self):
        return self._spirit_gain / BINARY_SCALE

    @spirit_gain.setter
    def spirit_gain(self, spirit_gain):
        self._spirit_gain = spirit_gain
        self.spirit = self.spirit_base * (1 + self.spirit_gain)

    @property
    def spirit(self):
        return self._spirit

    @spirit.setter
    def spirit(self, spirit):
        spirit = int(spirit)
        self._spirit = spirit
        self.base_magical_critical_strike = (self.magical_critical_strike_base + self.extra_magical_critical_strike
                                             + spirit * SPIRIT_TO_CRITICAL_STRIKE)

    @property
    def spunk_base(self):
        return self._spunk_base

    @spunk_base.setter
    def spunk_base(self, spunk_base):
        self._spunk_base = spunk_base
        self.spunk = spunk_base * (1 + self.spunk_gain)

    @property
    def spunk_gain(self):
        return self._spunk_gain / BINARY_SCALE

    @spunk_gain.setter
    def spunk_gain(self, spunk_gain):
        self._spunk_gain = spunk_gain
        self.spunk = self.spunk_base * (1 + self.spunk_gain)

    @property
    def spunk(self):
        return self._spunk

    @spunk.setter
    def spunk(self, spunk):
        spunk = int(spunk)
        self._spunk = spunk
        self.base_magical_attack_power = self.magical_attack_power_base + spunk * SPUNK_TO_ATTACK_POWER
        self.base_magical_overcome = self.magical_overcome_base + spunk * SPUNK_TO_OVERCOME

    """ Attack Power Function """

    @property
    def attack_power(self):
        raise NotImplementedError

    @property
    def physical_attack_power_base(self):
        return self._physical_attack_power_base

    @physical_attack_power_base.setter
    def physical_attack_power_base(self, physical_attack_power_base):
        self._physical_attack_power_base = physical_attack_power_base
        self.base_physical_attack_power = physical_attack_power_base + self.strength * STRENGTH_TO_ATTACK_POWER

    @property
    def base_physical_attack_power(self):
        return self._base_physical_attack_power

    @base_physical_attack_power.setter
    def base_physical_attack_power(self, base_physical_attack_power):
        base_physical_attack_power = int(base_physical_attack_power)
        self._base_physical_attack_power = base_physical_attack_power
        self.physical_attack_power = (self.base_physical_attack_power +
                                      self.base_physical_attack_power * self.physical_attack_power_gain +
                                      self.extra_physical_attack_power)

    @property
    def physical_attack_power_gain(self):
        return self._physical_attack_power_gain / BINARY_SCALE

    @physical_attack_power_gain.setter
    def physical_attack_power_gain(self, physical_attack_power_gain):
        self._physical_attack_power_gain = physical_attack_power_gain
        self.physical_attack_power = (self.base_physical_attack_power +
                                      self.base_physical_attack_power * self.physical_attack_power_gain +
                                      self.extra_physical_attack_power)

    @property
    def extra_physical_attack_power(self):
        return self._extra_physical_attack_power

    @extra_physical_attack_power.setter
    def extra_physical_attack_power(self, extra_physical_attack_power):
        extra_physical_attack_power = int(extra_physical_attack_power)
        self._extra_physical_attack_power = extra_physical_attack_power
        self.physical_attack_power = (self.base_physical_attack_power +
                                      self.base_physical_attack_power * self.physical_attack_power_gain +
                                      self.extra_physical_attack_power)

    @property
    def physical_attack_power(self):
        return self._physical_attack_power

    @physical_attack_power.setter
    def physical_attack_power(self, physical_attack_power):
        self._physical_attack_power = int(physical_attack_power)

    @property
    def magical_attack_power_base(self):
        return self._magical_attack_power_base

    @magical_attack_power_base.setter
    def magical_attack_power_base(self, magical_attack_power_base):
        self._magical_attack_power_base = magical_attack_power_base
        self.base_magical_attack_power = magical_attack_power_base + self.spunk_base * SPUNK_TO_ATTACK_POWER

    @property
    def base_magical_attack_power(self):
        return self._base_magical_attack_power

    @base_magical_attack_power.setter
    def base_magical_attack_power(self, base_magical_attack_power):
        base_magical_attack_power = int(base_magical_attack_power)
        self._base_magical_attack_power = base_magical_attack_power
        self.magical_attack_power = (self.base_magical_attack_power +
                                     self.base_magical_attack_power * self.magical_attack_power_gain +
                                     self.extra_magical_attack_power)

    @property
    def magical_attack_power_gain(self):
        return self._magical_attack_power_gain / BINARY_SCALE

    @magical_attack_power_gain.setter
    def magical_attack_power_gain(self, magical_attack_power_gain):
        self._magical_attack_power_gain = magical_attack_power_gain
        self.magical_attack_power = (self.base_magical_attack_power +
                                     self.base_magical_attack_power * self.magical_attack_power_gain +
                                     self.extra_magical_attack_power)

    @property
    def extra_magical_attack_power(self):
        return self._extra_magical_attack_power

    @extra_magical_attack_power.setter
    def extra_magical_attack_power(self, extra_magical_attack_power):
        extra_magical_attack_power = int(extra_magical_attack_power)
        self._extra_magical_attack_power = extra_magical_attack_power
        self.magical_attack_power = (self.base_magical_attack_power +
                                     self.base_magical_attack_power * self.magical_attack_power_gain +
                                     self.extra_magical_attack_power)

    @property
    def magical_attack_power(self):
        return self._magical_attack_power

    @magical_attack_power.setter
    def magical_attack_power(self, magical_attack_power):
        self._magical_attack_power = int(magical_attack_power)

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
    def all_critical_strike_gain(self):
        return self._all_critical_strike_gain

    @all_critical_strike_gain.setter
    def all_critical_strike_gain(self, all_critical_strike_gain):
        residual = all_critical_strike_gain - self._all_critical_strike_gain
        self.physical_critical_strike_gain += residual
        self.magical_critical_strike_gain += residual
        self._all_critical_strike_gain = all_critical_strike_gain

    @property
    def physical_critical_strike_base(self):
        return self._physical_critical_strike_base

    @physical_critical_strike_base.setter
    def physical_critical_strike_base(self, physical_critical_strike_base):
        self._physical_critical_strike_base = physical_critical_strike_base
        self.base_physical_critical_strike = (self.physical_critical_strike_base + self.extra_physical_critical_strike
                                              + self.agility * AGILITY_TO_CRITICAL_STRIKE)

    @property
    def extra_physical_critical_strike(self):
        return self._extra_physical_critical_strike

    @extra_physical_critical_strike.setter
    def extra_physical_critical_strike(self, extra_physical_critical_strike):
        extra_physical_critical_strike = int(extra_physical_critical_strike)
        self._extra_physical_critical_strike = extra_physical_critical_strike
        self.base_physical_critical_strike = (self.physical_critical_strike_base + self.extra_physical_critical_strike
                                              + self.agility * AGILITY_TO_CRITICAL_STRIKE)

    @property
    def base_physical_critical_strike(self):
        return self._base_physical_critical_strike

    @base_physical_critical_strike.setter
    def base_physical_critical_strike(self, base_physical_critical_strike):
        base_physical_critical_strike = int(base_physical_critical_strike)
        self._base_physical_critical_strike = base_physical_critical_strike
        self.physical_critical_strike_percent = self.base_physical_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def physical_critical_strike_percent(self):
        return self._physical_critical_strike_percent

    @physical_critical_strike_percent.setter
    def physical_critical_strike_percent(self, physical_critical_strike_percent):
        self._physical_critical_strike_percent = physical_critical_strike_percent
        self.physical_critical_strike = self.physical_critical_strike_percent + self.physical_critical_strike_gain

    @property
    def physical_critical_strike_gain(self):
        return self._physical_critical_strike_gain / DECIMAL_SCALE

    @physical_critical_strike_gain.setter
    def physical_critical_strike_gain(self, physical_critical_strike_gain):
        self._physical_critical_strike_gain = physical_critical_strike_gain
        self.physical_critical_strike = self.physical_critical_strike_percent + self.physical_critical_strike_gain

    @property
    def physical_critical_strike(self):
        return self._physical_critical_strike

    @physical_critical_strike.setter
    def physical_critical_strike(self, physical_critical_strike):
        self._physical_critical_strike = physical_critical_strike

    @property
    def magical_critical_strike_base(self):
        return self._magical_critical_strike_base

    @magical_critical_strike_base.setter
    def magical_critical_strike_base(self, magical_critical_strike_base):
        self._magical_critical_strike_base = magical_critical_strike_base
        self.base_magical_critical_strike = (self.magical_critical_strike_base + self.extra_magical_critical_strike
                                             + self.spirit * SPIRIT_TO_CRITICAL_STRIKE)

    @property
    def extra_magical_critical_strike(self):
        return self._extra_magical_critical_strike

    @extra_magical_critical_strike.setter
    def extra_magical_critical_strike(self, extra_magical_critical_strike):
        extra_magical_critical_strike = int(extra_magical_critical_strike)
        self._extra_magical_critical_strike = extra_magical_critical_strike
        self.base_magical_critical_strike = (self.magical_critical_strike_base + self.extra_magical_critical_strike
                                             + self.spirit * SPIRIT_TO_CRITICAL_STRIKE)

    @property
    def base_magical_critical_strike(self):
        return self._base_magical_critical_strike

    @base_magical_critical_strike.setter
    def base_magical_critical_strike(self, base_magical_critical_strike):
        base_magical_critical_strike = int(base_magical_critical_strike)
        self._base_magical_critical_strike = base_magical_critical_strike
        self.magical_critical_strike_percent = self.base_magical_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def magical_critical_strike_percent(self):
        return self._magical_critical_strike_percent

    @magical_critical_strike_percent.setter
    def magical_critical_strike_percent(self, magical_critical_strike_percent):
        self._magical_critical_strike_percent = magical_critical_strike_percent
        self.magical_critical_strike = self.magical_critical_strike_percent + self.magical_critical_strike_gain

    @property
    def magical_critical_strike_gain(self):
        return self._magical_critical_strike_gain / DECIMAL_SCALE

    @magical_critical_strike_gain.setter
    def magical_critical_strike_gain(self, magical_critical_strike_gain):
        self._magical_critical_strike_gain = magical_critical_strike_gain
        self.magical_critical_strike = self.magical_critical_strike_percent + self.magical_critical_strike_gain

    @property
    def magical_critical_strike(self):
        return self._magical_critical_strike

    @magical_critical_strike.setter
    def magical_critical_strike(self, magical_critical_strike):
        self._magical_critical_strike = magical_critical_strike

    """ Overcome Function"""

    @property
    def overcome(self):
        raise NotImplementedError

    @property
    def physical_overcome_base(self):
        return self._physical_overcome_base

    @physical_overcome_base.setter
    def physical_overcome_base(self, physical_overcome_base):
        self._physical_overcome_base = physical_overcome_base
        self.base_physical_overcome = self.physical_overcome_base + self.strength * STRENGTH_TO_OVERCOME

    @property
    def base_physical_overcome(self):
        return self._base_physical_overcome

    @base_physical_overcome.setter
    def base_physical_overcome(self, base_physical_overcome):
        base_physical_overcome = int(base_physical_overcome)
        self._base_physical_overcome = base_physical_overcome
        self.final_physical_overcome = (self.base_physical_overcome * (1 + self.physical_overcome_gain)
                                        + self.extra_physical_overcome)

    @property
    def physical_overcome_gain(self):
        return self._physical_overcome_gain / BINARY_SCALE

    @physical_overcome_gain.setter
    def physical_overcome_gain(self, physical_overcome_gain):
        self._physical_overcome_gain = physical_overcome_gain
        self.final_physical_overcome = (self.base_physical_overcome * (1 + self.physical_overcome_gain)
                                        + self.extra_physical_overcome)

    @property
    def extra_physical_overcome(self):
        return self._extra_physical_overcome

    @extra_physical_overcome.setter
    def extra_physical_overcome(self, extra_physical_overcome):
        extra_physical_overcome = int(extra_physical_overcome)
        self._extra_physical_overcome = extra_physical_overcome
        self.final_physical_overcome = (self.base_physical_overcome * (1 + self.physical_overcome_gain)
                                        + self.extra_physical_overcome)

    @property
    def final_physical_overcome(self):
        return self._final_physical_overcome

    @final_physical_overcome.setter
    def final_physical_overcome(self, final_physical_overcome):
        final_physical_overcome = int(final_physical_overcome)
        self._final_physical_overcome = final_physical_overcome
        self.physical_overcome = final_physical_overcome / OVERCOME_SCALE

    @property
    def physical_overcome(self):
        return self._physical_overcome

    @physical_overcome.setter
    def physical_overcome(self, physical_overcome):
        self._physical_overcome = physical_overcome

    @property
    def magical_overcome_base(self):
        return self._magical_overcome_base

    @magical_overcome_base.setter
    def magical_overcome_base(self, magical_overcome_base):
        self._magical_overcome_base = magical_overcome_base
        self.base_magical_overcome = self.magical_overcome_base + self.spunk * SPUNK_TO_OVERCOME

    @property
    def base_magical_overcome(self):
        return self._base_magical_overcome

    @base_magical_overcome.setter
    def base_magical_overcome(self, base_magical_overcome):
        base_magical_overcome = int(base_magical_overcome)
        self._base_magical_overcome = base_magical_overcome
        self.final_magical_overcome = (self.base_magical_overcome * (1 + self.magical_overcome_gain)
                                       + self.extra_magical_overcome)

    @property
    def magical_overcome_gain(self):
        return self._magical_overcome_gain / BINARY_SCALE

    @magical_overcome_gain.setter
    def magical_overcome_gain(self, magical_overcome_gain):
        self._magical_overcome_gain = magical_overcome_gain
        self.final_magical_overcome = (self.base_magical_overcome * (1 + self.magical_overcome_gain)
                                       + self.extra_magical_overcome)

    @property
    def extra_magical_overcome(self):
        return self._extra_magical_overcome

    @extra_magical_overcome.setter
    def extra_magical_overcome(self, extra_magical_overcome):
        extra_magical_overcome = int(extra_magical_overcome)
        self._extra_magical_overcome = extra_magical_overcome
        self.final_magical_overcome = (self.base_magical_overcome * (1 + self.magical_overcome_gain)
                                       + self.extra_magical_overcome)

    @property
    def final_magical_overcome(self):
        return self._final_magical_overcome

    @final_magical_overcome.setter
    def final_magical_overcome(self, final_magical_overcome):
        final_magical_overcome = int(final_magical_overcome)
        self._final_magical_overcome = final_magical_overcome
        self.magical_overcome = final_magical_overcome / OVERCOME_SCALE

    @property
    def magical_overcome(self):
        return self._magical_overcome

    @magical_overcome.setter
    def magical_overcome(self, magical_overcome):
        self._magical_overcome = magical_overcome


class Minor:
    surplus: int = 0

    _strain_base: int = 0
    _strain_percent: float = 0
    _strain_gain: int = 0
    _strain: float = 0

    _all_critical_power_base: int = 0
    _all_critical_power_gain: int = 0

    _physical_critical_power_base: int = 0
    _physical_critical_power_percent: float = 0
    _physical_critical_power_gain: int = 0
    _physical_critical_power: float = 0
    _magical_critical_power_base: int = 0
    _magical_critical_power_percent: float = 0
    _magical_critical_power_gain: int = 0
    _magical_critical_power: float = 0

    _weapon_damage_rand: int = 0
    _weapon_damage_base: int = 0
    _weapon_damage_gain: int = 0
    _weapon_damage: int = 0

    _all_shield_ignore: float = 0

    _physical_shield_ignore: float = 0
    _magical_shield_ignore: float = 0

    _all_damage_addition: float = 0
    _physical_damage_addition: float = 0
    _magical_damage_addition: float = 0

    _pve_addition: float = 0

    """ Minor Function """

    @property
    def strain_base(self):
        return self._strain_base

    @strain_base.setter
    def strain_base(self, strain_base):
        self._strain_base = strain_base
        self.strain_percent = strain_base / STRAIN_SCALE

    @property
    def strain_percent(self):
        return self._strain_percent

    @strain_percent.setter
    def strain_percent(self, strain_percent):
        self._strain_percent = strain_percent
        self.strain = strain_percent + self.strain_gain

    @property
    def strain_gain(self):
        return self._strain_gain / BINARY_SCALE

    @strain_gain.setter
    def strain_gain(self, strain_gain):
        self._strain_gain = strain_gain
        self.strain = self.strain_percent + self.strain_gain

    @property
    def strain(self):
        return self._strain

    @strain.setter
    def strain(self, strain):
        self._strain = strain

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
    def all_critical_power_gain(self):
        return self._all_critical_power_gain

    @all_critical_power_gain.setter
    def all_critical_power_gain(self, all_critical_power_gain):
        residual = all_critical_power_gain - self._all_critical_power_gain
        self.physical_critical_power_gain += residual
        self.magical_critical_power_gain += residual
        self._all_critical_power_gain = all_critical_power_gain

    @property
    def physical_critical_power_base(self):
        return self._physical_critical_power_base

    @physical_critical_power_base.setter
    def physical_critical_power_base(self, physical_critical_power_base):
        self._physical_critical_power_base = physical_critical_power_base
        self.physical_critical_power_percent = self.physical_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def physical_critical_power_percent(self):
        return BASE_CRITICAL_POWER + self._physical_critical_power_percent

    @physical_critical_power_percent.setter
    def physical_critical_power_percent(self, physical_critical_power_percent):
        self._physical_critical_power_percent = physical_critical_power_percent
        self.physical_critical_power = self.physical_critical_power_percent + self.physical_critical_power_gain

    @property
    def physical_critical_power_gain(self):
        return self._physical_critical_power_gain / BINARY_SCALE

    @physical_critical_power_gain.setter
    def physical_critical_power_gain(self, physical_critical_power_gain):
        self._physical_critical_power_gain = physical_critical_power_gain
        self.physical_critical_power = self.physical_critical_power_percent + self.physical_critical_power_gain

    @property
    def physical_critical_power(self):
        return self._physical_critical_power

    @physical_critical_power.setter
    def physical_critical_power(self, physical_critical_power):
        self._physical_critical_power = physical_critical_power

    @property
    def magical_critical_power_base(self):
        return self._magical_critical_power_base

    @magical_critical_power_base.setter
    def magical_critical_power_base(self, magical_critical_power_base):
        self._magical_critical_power_base = magical_critical_power_base
        self.magical_critical_power_percent = self.magical_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def magical_critical_power_percent(self):
        return BASE_CRITICAL_POWER + self._magical_critical_power_percent

    @magical_critical_power_percent.setter
    def magical_critical_power_percent(self, magical_critical_power_percent):
        self._magical_critical_power_percent = magical_critical_power_percent
        self.magical_critical_power = self.magical_critical_power_percent + self.magical_critical_power_gain

    @property
    def magical_critical_power_gain(self):
        return self._magical_critical_power_gain / BINARY_SCALE

    @magical_critical_power_gain.setter
    def magical_critical_power_gain(self, magical_critical_power_gain):
        self._magical_critical_power_gain = magical_critical_power_gain
        self.magical_critical_power = self.magical_critical_power_percent + self.magical_critical_power_gain

    @property
    def magical_critical_power(self):
        return self._magical_critical_power

    @magical_critical_power.setter
    def magical_critical_power(self, magical_critical_power):
        self._magical_critical_power = magical_critical_power

    """ Weapon Damage Function """

    @property
    def weapon_damage_rand(self):
        return self._weapon_damage_rand

    @weapon_damage_rand.setter
    def weapon_damage_rand(self, weapon_damage_rand):
        self._weapon_damage_rand = weapon_damage_rand
        self.weapon_damage = self.weapon_damage_base * (1 + self.weapon_damage_gain) + self.weapon_damage_rand / 2

    @property
    def weapon_damage_base(self):
        return self._weapon_damage_base

    @weapon_damage_base.setter
    def weapon_damage_base(self, weapon_damage_base):
        self._weapon_damage_base = weapon_damage_base
        self.weapon_damage = self.weapon_damage_base * (1 + self.weapon_damage_gain) + self.weapon_damage_rand / 2

    @property
    def weapon_damage_gain(self):
        return self._weapon_damage_gain / BINARY_SCALE

    @weapon_damage_gain.setter
    def weapon_damage_gain(self, weapon_damage_gain):
        self._weapon_damage_gain = weapon_damage_gain
        self.weapon_damage = self.weapon_damage_base * (1 + self.weapon_damage_gain) + self.weapon_damage_rand / 2

    @property
    def weapon_damage(self):
        return self._weapon_damage

    @weapon_damage.setter
    def weapon_damage(self, weapon_damage):
        self._weapon_damage = int(weapon_damage)

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
    def physical_shield_ignore(self):
        return self._physical_shield_ignore / BINARY_SCALE

    @physical_shield_ignore.setter
    def physical_shield_ignore(self, physical_shield_ignore):
        self._physical_shield_ignore = physical_shield_ignore

    @property
    def magical_shield_ignore(self):
        return self._magical_shield_ignore / BINARY_SCALE

    @magical_shield_ignore.setter
    def magical_shield_ignore(self, magical_shield_ignore):
        self._magical_shield_ignore = magical_shield_ignore

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

    @property
    def physical_damage_addition(self):
        return self._physical_damage_addition / BINARY_SCALE

    @physical_damage_addition.setter
    def physical_damage_addition(self, physical_damage_addition):
        self._physical_damage_addition = physical_damage_addition

    @property
    def magical_damage_addition(self):
        return self._magical_damage_addition / BINARY_SCALE

    @magical_damage_addition.setter
    def magical_damage_addition(self, magical_damage_addition):
        self._magical_damage_addition = magical_damage_addition

    @property
    def pve_addition(self):
        return self._pve_addition / BINARY_SCALE

    @pve_addition.setter
    def pve_addition(self, pve_addition):
        self._pve_addition = pve_addition


class Attribute(Major, Minor, Target):
    level: int = 120
    grad_attrs: dict = None

    def __init__(self):
        self.all_major_base += MAJOR_BASE
        self.all_critical_power_base = 0  # init critical power attr

    @property
    def level_reduction(self):
        return LEVEL_REDUCTION * (self.target_level - self.level)


class PhysicalAttribute(Attribute):
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
    def shield_ignore(self):
        return self.physical_shield_ignore

    @property
    def damage_addition(self):
        return self.physical_damage_addition

    @property
    def shield_base(self):
        return self.physical_shield_base

    @property
    def shield_gain(self):
        return self.physical_shield_gain

    @property
    def vulnerable(self):
        return self.physical_vulnerable


class MagicalAttribute(Attribute):
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
    def shield_base(self):
        return self.magical_shield_base

    @property
    def shield_gain(self):
        return self.magical_shield_gain

    @property
    def vulnerable(self):
        return self.magical_vulnerable
