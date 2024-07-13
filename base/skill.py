from dataclasses import dataclass
from typing import List

from base.attribute import Attribute, PhysicalAttribute
from base.constant import *
from utils.damage import *


class BaseSkill:
    skill_id: int = 0
    _skill_name: List[str] = None
    skill_level: int = 0

    @property
    def display_name(self):
        return f"{self.skill_name}#{self.skill_id}-{self.skill_level}"

    @property
    def skill_name(self):
        if not self._skill_name:
            return ""
        if self.skill_level > len(self._skill_name):
            return self._skill_name[-1]
        else:
            return self._skill_name[self.skill_level - 1]

    @skill_name.setter
    def skill_name(self, skill_name):
        if isinstance(skill_name, list):
            self._skill_name = skill_name
        else:
            self._skill_name = [skill_name]


class BaseDamage(BaseSkill):
    PHYSICAL_KINDS = ["Physics"]
    MAGICAL_KINDS = ["SolarMagic", "LunarMagic", "NeutralMagic", "Poison"]
    platform: int

    kind_type: str = ""
    _physical_damage_call: List[int] = []
    _magical_damage_call: List[int] = []
    _adaptive_damage_call: List[int] = []
    _physical_surplus_call: List[int] = []
    _magical_surplus_call: List[int] = []

    _physical_damage_base: List[int] = []
    _physical_damage_rand: List[int] = []
    _magical_damage_base: List[int] = []
    _magical_damage_rand: List[int] = []

    _prepare_frame: List[int] = []
    _channel_interval: List[int] = []
    _weapon_damage_cof: List[int] = []
    _global_damage_cof: List[float] = []

    skill_cof: int = 0
    dot_cof: int = 0
    _surplus_cof: int = 0

    prepare_frame_extra: int = 0
    channel_interval_extra: float = 1.
    global_damage_cof_extra: float = 1.

    _damage_addition: List[int] = []
    damage_addition_extra: int = 0
    move_state_damage_addition: int = 0

    physical_attack_power_base: List[int] = []
    magical_attack_power_base: List[int] = []
    _physical_attack_power_gain: List[int] = []
    physical_attack_power_gain_extra: int = 0
    _magical_attack_power_gain: List[int] = []
    magical_attack_power_gain_extra: int = 0
    _physical_critical_strike_rate: List[int] = []
    physical_critical_strike_rate_extra: int = 0
    _physical_critical_power_rate: List[int] = []
    physical_critical_power_rate_extra: int = 0
    _physical_shield_gain: List[int] = []
    physical_shield_gain_extra: int = 0
    _magical_critical_strike_rate: List[int] = []
    magical_critical_strike_rate_extra: int = 0
    _magical_critical_power_rate: List[int] = []
    magical_critical_power_rate_extra: int = 0
    _magical_shield_gain: List[int] = []
    magical_shield_gain_extra: int = 0
    _pve_addition: List[int] = []
    pve_addition_extra: int = 0

    @property
    def attack_power_call(self):
        return self.physical_damage_call or self.magical_damage_call or self.adaptive_damage_call

    @property
    def surplus_call(self):
        return self.physical_surplus_call or self.magical_surplus_call

    @property
    def damage_call(self):
        return self.surplus_call or self.attack_power_call

    @property
    def physical_damage_call(self):
        if not self._physical_damage_call:
            return 0
        if self.skill_level > len(self._physical_damage_call):
            return self._physical_damage_call[-1]
        else:
            return self._physical_damage_call[self.skill_level - 1]

    @physical_damage_call.setter
    def physical_damage_call(self, physical_damage_call):
        if isinstance(physical_damage_call, list):
            self._physical_damage_call = physical_damage_call
        else:
            self._physical_damage_call = [physical_damage_call]

    @property
    def magical_damage_call(self):
        if not self._magical_damage_call:
            return 0
        if self.skill_level > len(self._magical_damage_call):
            return self._magical_damage_call[-1]
        else:
            return self._magical_damage_call[self.skill_level - 1]

    @magical_damage_call.setter
    def magical_damage_call(self, magical_damage_call):
        if isinstance(magical_damage_call, list):
            self._magical_damage_call = magical_damage_call
        else:
            self._magical_damage_call = [magical_damage_call]

    @property
    def adaptive_damage_call(self):
        if not self._adaptive_damage_call:
            return 0
        if self.skill_level > len(self._adaptive_damage_call):
            return self._adaptive_damage_call[-1]
        else:
            return self._adaptive_damage_call[self.skill_level - 1]

    @adaptive_damage_call.setter
    def adaptive_damage_call(self, adaptive_damage_call):
        if isinstance(adaptive_damage_call, list):
            self._adaptive_damage_call = adaptive_damage_call
        else:
            self._adaptive_damage_call = [adaptive_damage_call]

    @property
    def physical_surplus_call(self):
        if not self._physical_surplus_call:
            return 0
        if self.skill_level > len(self._physical_surplus_call):
            return self._physical_surplus_call[-1]
        else:
            return self._physical_surplus_call[self.skill_level - 1]

    @physical_surplus_call.setter
    def physical_surplus_call(self, physical_surplus_call):
        if isinstance(physical_surplus_call, list):
            self._physical_surplus_call = physical_surplus_call
        else:
            self._physical_surplus_call = [physical_surplus_call]

    @property
    def magical_surplus_call(self):
        if not self._magical_surplus_call:
            return 0
        if self.skill_level > len(self._magical_surplus_call):
            return self._magical_surplus_call[-1]
        else:
            return self._magical_surplus_call[self.skill_level - 1]

    @magical_surplus_call.setter
    def magical_surplus_call(self, magical_surplus_call):
        if isinstance(magical_surplus_call, list):
            self._magical_surplus_call = magical_surplus_call
        else:
            self._magical_surplus_call = [magical_surplus_call]

    @property
    def physical_damage_base(self):
        if not self._physical_damage_base:
            return 0
        if self.skill_level > len(self._physical_damage_base):
            return self._physical_damage_base[-1]
        else:
            return self._physical_damage_base[self.skill_level - 1]

    @physical_damage_base.setter
    def physical_damage_base(self, physical_damage_base):
        if isinstance(physical_damage_base, list):
            self._physical_damage_base = physical_damage_base
        else:
            self._physical_damage_base = [physical_damage_base]

    @property
    def physical_damage_rand(self):
        if not self._physical_damage_rand:
            return 0
        if self.skill_level > len(self._physical_damage_rand):
            return self._physical_damage_rand[-1]
        else:
            return self._physical_damage_rand[self.skill_level - 1]

    @physical_damage_rand.setter
    def physical_damage_rand(self, physical_damage_rand):
        if isinstance(physical_damage_rand, list):
            self._physical_damage_rand = physical_damage_rand
        else:
            self._physical_damage_rand = [physical_damage_rand]

    @property
    def magical_damage_base(self):
        if not self._magical_damage_base:
            return 0
        if self.skill_level > len(self._magical_damage_base):
            return self._magical_damage_base[-1]
        else:
            return self._magical_damage_base[self.skill_level - 1]

    @magical_damage_base.setter
    def magical_damage_base(self, magical_damage_base):
        if isinstance(magical_damage_base, list):
            self._magical_damage_base = magical_damage_base
        else:
            self._magical_damage_base = [magical_damage_base]

    @property
    def magical_damage_rand(self):
        if not self._magical_damage_rand:
            return 0
        if self.skill_level > len(self._magical_damage_rand):
            return self._magical_damage_rand[-1]
        else:
            return self._magical_damage_rand[self.skill_level - 1]

    @magical_damage_rand.setter
    def magical_damage_rand(self, magical_damage_rand):
        if isinstance(magical_damage_rand, list):
            self._magical_damage_rand = magical_damage_rand
        else:
            self._magical_damage_rand = [magical_damage_rand]

    @property
    def prepare_frame(self):
        if not self._prepare_frame:
            return 0
        if self.skill_level > len(self._prepare_frame):
            return self._prepare_frame[-1] + self.prepare_frame_extra
        else:
            return self._prepare_frame[self.skill_level - 1] + self.prepare_frame_extra

    @prepare_frame.setter
    def prepare_frame(self, prepare_frame):
        if isinstance(prepare_frame, list):
            self._prepare_frame = prepare_frame
        else:
            self._prepare_frame = [prepare_frame]

    @property
    def channel_interval(self):
        if not self._channel_interval:
            return 0
        if self.skill_level > len(self._channel_interval):
            channel_interval = self._channel_interval[-1] * self.channel_interval_extra
        else:
            channel_interval = self._channel_interval[self.skill_level - 1] * self.channel_interval_extra

        return int(channel_interval)

    @channel_interval.setter
    def channel_interval(self, channel_interval):
        if isinstance(channel_interval, list):
            self._channel_interval = channel_interval
        else:
            self._channel_interval = [channel_interval]

    @property
    def surplus_cof(self):
        if not self.platform:
            return DEFAULT_SURPLUS_COF
        else:
            return self._surplus_cof / BINARY_SCALE

    @surplus_cof.setter
    def surplus_cof(self, surplus_cof):
        self._surplus_cof = surplus_cof

    @property
    def weapon_damage_cof(self):
        if not self._weapon_damage_cof:
            return 0
        if self.skill_level > len(self._weapon_damage_cof):
            weapon_damage_cof = self._weapon_damage_cof[-1]
        else:
            weapon_damage_cof = self._weapon_damage_cof[self.skill_level - 1]
        return WEAPON_DAMAGE_COF(weapon_damage_cof)

    @weapon_damage_cof.setter
    def weapon_damage_cof(self, weapon_damage_cof):
        if isinstance(weapon_damage_cof, list):
            self._weapon_damage_cof = weapon_damage_cof
        else:
            self._weapon_damage_cof = [weapon_damage_cof]

    @property
    def global_damage_cof(self):
        if not self._global_damage_cof:
            return self.global_damage_cof_extra
        elif self.skill_level > len(self._global_damage_cof):
            return GLOBAL_DAMAGE_COF(self._global_damage_cof[-1]) * self.global_damage_cof_extra
        else:
            return GLOBAL_DAMAGE_COF(self._global_damage_cof[self.skill_level - 1]) * self.global_damage_cof_extra

    @global_damage_cof.setter
    def global_damage_cof(self, global_damage_cof):
        if isinstance(global_damage_cof, list):
            self._global_damage_cof = global_damage_cof
        else:
            self._global_damage_cof = [global_damage_cof]

    @property
    def damage_addition(self):
        if not self._damage_addition:
            return self.damage_addition_extra
        elif self.skill_level > len(self._damage_addition):
            return self._damage_addition[-1] + self.damage_addition_extra
        else:
            return self._damage_addition[self.skill_level - 1] + self.damage_addition_extra

    @damage_addition.setter
    def damage_addition(self, damage_addition):
        if isinstance(damage_addition, list):
            self._damage_addition = damage_addition
        else:
            self._damage_addition = [damage_addition]

    @property
    def physical_attack_power_gain(self):
        if not self._physical_attack_power_gain:
            return self.physical_attack_power_gain_extra
        elif self.skill_level > len(self._physical_attack_power_gain):
            return self._physical_attack_power_gain[-1] + self.physical_attack_power_gain_extra
        else:
            return self._physical_attack_power_gain[self.skill_level - 1] + self.physical_attack_power_gain_extra

    @physical_attack_power_gain.setter
    def physical_attack_power_gain(self, physical_attack_power_gain):
        if isinstance(physical_attack_power_gain, list):
            self._physical_attack_power_gain = physical_attack_power_gain
        else:
            self._physical_attack_power_gain = [physical_attack_power_gain]

    @property
    def physical_critical_strike_rate(self):
        if not self._physical_critical_strike_rate:
            return self.physical_critical_strike_rate_extra
        elif self.skill_level > len(self._physical_critical_strike_rate):
            return self._physical_critical_strike_rate[-1] + self.physical_critical_strike_rate_extra
        else:
            return self._physical_critical_strike_rate[self.skill_level - 1] + self.physical_critical_strike_rate_extra

    @physical_critical_strike_rate.setter
    def physical_critical_strike_rate(self, physical_critical_strike_rate):
        if isinstance(physical_critical_strike_rate, list):
            self._physical_critical_strike_rate = physical_critical_strike_rate
        else:
            self._physical_critical_strike_rate = [physical_critical_strike_rate]

    @property
    def physical_critical_power_rate(self):
        if not self._physical_critical_power_rate:
            return self.physical_critical_power_rate_extra
        elif self.skill_level > len(self._physical_critical_power_rate):
            return self._physical_critical_power_rate[-1] + self.physical_critical_power_rate_extra
        else:
            return self._physical_critical_power_rate[self.skill_level - 1] + self.physical_critical_power_rate_extra

    @physical_critical_power_rate.setter
    def physical_critical_power_rate(self, physical_critical_power_rate):
        if isinstance(physical_critical_power_rate, list):
            self._physical_critical_power_rate = physical_critical_power_rate
        else:
            self._physical_critical_power_rate = [physical_critical_power_rate]

    @property
    def physical_shield_gain(self):
        if not self._physical_shield_gain:
            return self.physical_shield_gain_extra
        elif self.skill_level > len(self._physical_shield_gain):
            return self._physical_shield_gain[-1] + self.physical_shield_gain_extra
        else:
            return self._physical_shield_gain[self.skill_level - 1] + self.physical_shield_gain_extra

    @physical_shield_gain.setter
    def physical_shield_gain(self, physical_shield_gain):
        if isinstance(physical_shield_gain, list):
            self._physical_shield_gain = physical_shield_gain
        else:
            self._physical_shield_gain = [physical_shield_gain]

    @property
    def magical_attack_power_gain(self):
        if not self._magical_attack_power_gain:
            return self.magical_attack_power_gain_extra
        elif self.skill_level > len(self._magical_attack_power_gain):
            return self._magical_attack_power_gain[-1] + self.magical_attack_power_gain_extra
        else:
            return self._magical_attack_power_gain[self.skill_level - 1] + self.magical_attack_power_gain_extra

    @magical_attack_power_gain.setter
    def magical_attack_power_gain(self, magical_attack_power_gain):
        if isinstance(magical_attack_power_gain, list):
            self._magical_attack_power_gain = magical_attack_power_gain
        else:
            self._magical_attack_power_gain = [magical_attack_power_gain]

    @property
    def magical_critical_strike_rate(self):
        if not self._magical_critical_strike_rate:
            return self.magical_critical_strike_rate_extra
        elif self.skill_level > len(self._magical_critical_strike_rate):
            return self._magical_critical_strike_rate[-1] + self.magical_critical_strike_rate_extra
        else:
            return self._magical_critical_strike_rate[self.skill_level - 1] + self.magical_critical_strike_rate_extra

    @magical_critical_strike_rate.setter
    def magical_critical_strike_rate(self, magical_critical_strike_rate):
        if isinstance(magical_critical_strike_rate, list):
            self._magical_critical_strike_rate = magical_critical_strike_rate
        else:
            self._magical_critical_strike_rate = [magical_critical_strike_rate]

    @property
    def magical_critical_power_rate(self):
        if not self._magical_critical_power_rate:
            return self.magical_critical_power_rate_extra
        elif self.skill_level > len(self._magical_critical_power_rate):
            return self._magical_critical_power_rate[-1] + self.magical_critical_power_rate_extra
        else:
            return self._magical_critical_power_rate[self.skill_level - 1] + self.magical_critical_power_rate_extra

    @magical_critical_power_rate.setter
    def magical_critical_power_rate(self, magical_critical_power_rate):
        if isinstance(magical_critical_power_rate, list):
            self._magical_critical_power_rate = magical_critical_power_rate
        else:
            self._magical_critical_power_rate = [magical_critical_power_rate]

    @property
    def magical_shield_gain(self):
        if not self._magical_shield_gain:
            return self.magical_shield_gain_extra
        if self.skill_level > len(self._magical_shield_gain):
            return self._magical_shield_gain[-1] + self.magical_shield_gain_extra
        else:
            return self._magical_shield_gain[self.skill_level - 1] + self.magical_shield_gain_extra

    @magical_shield_gain.setter
    def magical_shield_gain(self, magical_shield_gain):
        if isinstance(magical_shield_gain, list):
            self._magical_shield_gain = magical_shield_gain
        else:
            self._magical_shield_gain = [magical_shield_gain]

    @property
    def pve_addition(self):
        if not self._pve_addition:
            return self.pve_addition_extra
        if self.skill_level > len(self._pve_addition):
            return self._pve_addition[-1] + self.pve_addition_extra
        else:
            return self._pve_addition[self.skill_level - 1] + self.pve_addition_extra

    @pve_addition.setter
    def pve_addition(self, pve_addition):
        if isinstance(pve_addition, list):
            self._pve_addition = pve_addition
        else:
            self._pve_addition = [pve_addition]

    @property
    def physical_attack_power_cof(self):
        if not self.platform:
            return PHYSICAL_ATTACK_POWER_COF(self.channel_interval + self.prepare_frame)
        else:
            return PHYSICAL_ATTACK_POWER_COF(self.skill_cof)

    @property
    def magical_attack_power_cof(self):
        if not self.platform:
            return MAGICAL_ATTACK_POWER_COF(self.channel_interval + self.prepare_frame)
        else:
            return MAGICAL_ATTACK_POWER_COF(self.skill_cof)

    def pre_damage(self, attribute: Attribute):
        attribute.global_damage_cof *= self.global_damage_cof
        attribute.physical_attack_power_gain += self.physical_attack_power_gain
        attribute.magical_attack_power_gain += self.magical_attack_power_gain
        attribute.physical_critical_strike_rate += self.physical_critical_strike_rate
        attribute.magical_critical_strike_rate += self.magical_critical_strike_rate
        attribute.physical_critical_power_rate += self.physical_critical_power_rate
        attribute.magical_critical_power_rate += self.magical_critical_power_rate
        attribute.target.physical_shield_gain += self.physical_shield_gain
        attribute.target.magical_shield_gain += self.magical_shield_gain
        attribute.all_damage_addition += self.damage_addition
        attribute.pve_addition += self.pve_addition

    def post_damage(self, attribute: Attribute):
        attribute.global_damage_cof /= self.global_damage_cof
        attribute.physical_attack_power_gain -= self.physical_attack_power_gain
        attribute.magical_attack_power_gain -= self.magical_attack_power_gain
        attribute.physical_critical_strike_rate -= self.physical_critical_strike_rate
        attribute.magical_critical_strike_rate -= self.magical_critical_strike_rate
        attribute.physical_critical_power_rate -= self.physical_critical_power_rate
        attribute.magical_critical_power_rate -= self.magical_critical_power_rate
        attribute.target.physical_shield_gain -= self.physical_shield_gain
        attribute.target.magical_shield_gain -= self.magical_shield_gain
        attribute.all_damage_addition -= self.damage_addition
        attribute.pve_addition -= self.pve_addition

    def critical_strike(self, attribute: Attribute):
        if self.kind_type in self.PHYSICAL_KINDS:
            return attribute.physical_critical_strike
        elif self.kind_type in self.MAGICAL_KINDS:
            return attribute.magical_critical_strike
        else:
            return attribute.critical_strike

    def critical_power(self, attribute: Attribute):
        if self.kind_type in self.PHYSICAL_KINDS:
            return attribute.physical_critical_power
        elif self.kind_type in self.MAGICAL_KINDS:
            return attribute.magical_critical_power
        else:
            return attribute.critical_power

    def physical_damage_chain(self, damage: int, attribute: Attribute):
        damage = damage_addition_result(
            damage, attribute.physical_damage_addition, self.move_state_damage_addition
        )
        damage = overcome_result(
            damage, attribute.physical_overcome, attribute.physical_shield_ignore,
            attribute.target.level_shield_base + attribute.target.physical_shield_base,
            attribute.target.physical_shield_gain, attribute.target.shield_constant
        )
        critical_damage = critical_result(damage, self.critical_power(attribute))
        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.strain)
        critical_damage = strain_result(critical_damage, attribute.strain)
        damage = pve_addition_result(damage, attribute.pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition)
        damage = damage_cof_result(damage, attribute.target.physical_damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.target.physical_damage_cof)
        return damage, critical_damage

    def magical_damage_chain(self, damage: int, attribute: Attribute):
        damage = damage_addition_result(
            damage, attribute.magical_damage_addition, self.move_state_damage_addition
        )
        damage = overcome_result(
            damage, attribute.magical_overcome, attribute.magical_shield_ignore,
            attribute.target.level_shield_base + attribute.target.magical_shield_base,
            attribute.target.magical_shield_gain, attribute.target.shield_constant
        )
        critical_damage = critical_result(damage, self.critical_power(attribute))
        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.strain)
        critical_damage = strain_result(critical_damage, attribute.strain)
        damage = pve_addition_result(damage, attribute.pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition)
        damage = damage_cof_result(damage, attribute.target.magical_damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.target.magical_damage_cof)
        return damage, critical_damage

    def adaptive_damage_chain(self, damage: int, attribute: Attribute):
        damage = damage_addition_result(
            damage, attribute.damage_addition, self.move_state_damage_addition
        )
        damage = overcome_result(
            damage, attribute.overcome, attribute.shield_ignore,
            attribute.target.level_shield_base + attribute.target_shield_base,
            attribute.target_shield_gain, attribute.target.shield_constant
        )
        critical_damage = critical_result(damage, self.critical_power(attribute))
        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.strain)
        critical_damage = strain_result(critical_damage, attribute.strain)
        damage = pve_addition_result(damage, attribute.pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition)
        damage = damage_cof_result(damage, attribute.target_damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.target_damage_cof)
        return damage, critical_damage

    def call_physical_damage(self, attribute: Attribute):
        damage = init_result(
            self.physical_damage_base, self.physical_damage_rand, attribute.damage_gain,
            self.physical_attack_power_cof, attribute.physical_attack_power,
            self.weapon_damage_cof, attribute.weapon_damage,
            0, 0, attribute.global_damage_cof
        )
        if damage:
            return self.physical_damage_chain(damage, attribute)
        return 0, 0

    def call_adaptive_damage(self, attribute: Attribute):
        if isinstance(attribute, PhysicalAttribute):
            damage_base = self.physical_damage_base
            damage_rand = self.physical_damage_rand
            attack_power_cof = self.physical_attack_power_cof
        else:
            damage_base = self.magical_damage_base
            damage_rand = self.magical_damage_rand
            attack_power_cof = self.magical_attack_power_cof

        damage = init_result(
            damage_base, damage_rand, attribute.damage_gain,
            attack_power_cof, attribute.attack_power,
            self.weapon_damage_cof, attribute.weapon_damage,
            0, 0, attribute.global_damage_cof
        )
        if damage:
            return self.adaptive_damage_chain(damage, attribute)
        return 0, 0

    def call_magical_damage(self, attribute: Attribute):
        damage = init_result(
            self.magical_damage_base, self.magical_damage_rand, attribute.damage_gain,
            self.magical_attack_power_cof, attribute.magical_attack_power,
            0, 0, 0, 0, attribute.global_damage_cof
        )
        if damage:
            return self.magical_damage_chain(damage, attribute)
        return 0, 0

    def call_physical_surplus(self, attribute: Attribute):
        damage = init_result(
            0, 0, 0, 0, 0, 0, 0, self.surplus_cof, attribute.surplus, attribute.global_damage_cof
        )
        if damage:
            return self.physical_damage_chain(damage, attribute)
        return 0, 0

    def call_magical_surplus(self, attribute: Attribute):
        damage = init_result(
            0, 0, 0, 0, 0, 0, 0, self.surplus_cof, attribute.surplus, attribute.global_damage_cof
        )
        if damage:
            return self.magical_damage_chain(damage, attribute)
        return 0, 0

    def __call__(self, attribute: Attribute):
        self.pre_damage(attribute)
        total_damage, total_critical_damage = 0, 0
        if self.physical_damage_call:
            damage, critical_damage = self.call_physical_damage(attribute)
            total_damage += damage * self.physical_damage_call
            total_critical_damage += critical_damage * self.physical_damage_call
        if self.magical_damage_call:
            damage, critical_damage = self.call_magical_damage(attribute)
            total_damage += damage * self.magical_damage_call
            total_critical_damage += critical_damage * self.magical_damage_call
        if self.adaptive_damage_call:
            damage, critical_damage = self.call_adaptive_damage(attribute)
            total_damage += damage * self.adaptive_damage_call
            total_critical_damage += critical_damage * self.adaptive_damage_call
        if self.physical_surplus_call:
            damage, critical_damage = self.call_physical_surplus(attribute)
            total_damage += damage * self.physical_surplus_call
            total_critical_damage += critical_damage * self.physical_surplus_call
        if self.magical_surplus_call:
            damage, critical_damage = self.call_magical_surplus(attribute)
            total_damage += damage * self.magical_surplus_call
            total_critical_damage += critical_damage * self.magical_surplus_call

        critical_strike = min(self.critical_strike(attribute), 1)
        expected_damage = total_damage * (1 - critical_strike) + total_critical_damage * critical_strike
        self.post_damage(attribute)
        return int(total_damage), int(total_critical_damage), critical_strike, expected_damage


@dataclass
class Skill(BaseDamage):
    skill_id: int

    activate: bool = True

    recipe_type: int = 0
    recipe_mask: int = 0
    event_mask_1: int = 0
    event_mask_2: int = 0

    bind_dot: int = 0
    bind_stack: int = 1
    consume_dot: int = 0
    consume_tick: int = 0

    pet_count: int = 1
    pet_buffs: dict = None

    pre_effects: list = None
    pre_buffs: dict = None
    pre_target_buffs: dict = None
    post_effects: list = None
    post_buffs: dict = None
    post_target_buffs: dict = None

    def __post_init__(self):
        if not self.pet_buffs:
            self.pet_buffs = {}

        if not self.pre_effects:
            self.pre_effects = []
        if not self.pre_buffs:
            self.pre_buffs = {}
        if not self.pre_target_buffs:
            self.pre_target_buffs = {}
        if not self.post_effects:
            self.post_effects = []
        if not self.post_buffs:
            self.post_buffs = {}
        if not self.post_target_buffs:
            self.post_target_buffs = {}

    def pre_record(self, parser):
        for (buff_id, buff_level), buff_stack in self.pre_buffs.items():
            buff_level = buff_level if buff_level else self.skill_level
            parser.refresh_buff(buff_id, buff_level, buff_stack)
        for (buff_id, buff_level), buff_stack in self.pre_target_buffs.items():
            buff_level = buff_level if buff_level else self.skill_level
            parser.refresh_target_buff(buff_id, buff_level, buff_stack)
        for effect in self.pre_effects:
            effect(parser)

    def record(self, actual_critical_strike, actual_damage, parser):
        if self.damage_call:
            self.damage(actual_critical_strike, actual_damage, parser)
        if self.bind_dot:
            self.dot_add(parser)
        if self.consume_dot:
            self.dot_consume(parser)
        if self.pet_buffs:
            self.pet_create(parser)

    def post_record(self, parser):
        for (buff_id, buff_level), buff_stack in self.post_buffs.items():
            buff_level = buff_level if buff_level else self.skill_level
            parser.refresh_buff(buff_id, buff_level, buff_stack)
        for (buff_id, buff_level), buff_stack in self.post_target_buffs.items():
            buff_level = buff_level if buff_level else self.skill_level
            parser.refresh_target_buff(buff_id, buff_level, buff_stack)
        for effect in self.post_effects:
            effect(parser)

    def parse(self, actual_critical_strike, actual_damage, parser):
        self.pre_record(parser)
        self.record(actual_critical_strike, actual_damage, parser)
        self.post_record(parser)

    def damage(self, actual_critical_strike, actual_damage, parser):
        damage_tuple = ((self.skill_id, self.skill_level), tuple())
        status_tuple = parser.status
        parser.current_records[damage_tuple][status_tuple].append(
            (parser.current_frame - parser.start_frame, actual_critical_strike, actual_damage)
        )

    def pet_create(self, parser):
        pet_buffs = {}
        for (buff_id, buff_level), buff_stack in self.pet_buffs.items():
            buff_level = buff_level if buff_level else self.skill_level
            pet_buffs[(buff_id, buff_level)] = buff_stack
        for _ in range(self.pet_count):
            parser.current_next_pet_buff_stacks.append(pet_buffs.copy())

    def dot_add(self, parser):
        bind_dot = parser.current_school.dots[self.bind_dot]
        if not parser.current_dot_ticks.get(self.bind_dot):
            parser.current_dot_stacks[self.bind_dot] = 0
        parser.current_dot_ticks[self.bind_dot] = bind_dot.tick
        parser.current_dot_stacks[self.bind_dot] = parser.current_dot_stacks.get(self.bind_dot, 0) + self.bind_stack
        parser.current_dot_skills[self.bind_dot] = (self.skill_id, self.skill_level)
        parser.current_dot_snapshot[self.bind_dot] = parser.current_buff_stacks.copy()

    def dot_consume(self, parser):
        if not (last_dot := parser.current_last_dot.pop(self.consume_dot, None)):
            return
        damage_tuple, status_tuple = last_dot
        (dot_id, dot_level, dot_stack), (dot_skill_id, dot_skill_level) = damage_tuple
        parser.current_dot_ticks[dot_id] += 1
        if not self.consume_tick:
            tick = parser.current_dot_ticks[dot_id]
        else:
            tick = min(parser.current_dot_ticks[dot_id], self.consume_tick)
        new_damage_tuple = ((dot_id, dot_level, dot_stack * tick), (dot_skill_id, dot_skill_level))
        parser.current_damage = dot_id
        new_status_tuple = parser.dot_status
        parser.current_damage = self.skill_id
        parser.current_records[new_damage_tuple][new_status_tuple].append(
            parser.current_records[damage_tuple][status_tuple].pop()
        )
        parser.current_dot_ticks[dot_id] -= tick


class NpcSkill(Skill):
    def call_physical_damage(self, attribute: Attribute):
        damage = init_result(
            self.physical_damage_base, self.physical_damage_rand, attribute.damage_gain,
            self.physical_attack_power_cof, attribute.physical_attack_power,
            0, 0, 0, 0, attribute.global_damage_cof
        )
        if damage:
            return self.physical_damage_chain(damage, attribute)
        return 0, 0


class PetSkill(Skill):
    def call_magical_damage(self, attribute: Attribute):
        attack_power = int(attribute.magical_attack_power * 0.87 + attribute.surplus * DEFAULT_SURPLUS_COF * 59 / 1664)
        damage = init_result(
            self.magical_damage_base, self.magical_damage_rand, attribute.damage_gain,
            self.magical_attack_power_cof, attack_power,
            0, 0, 0, 0, attribute.global_damage_cof
        )
        if damage:
            return self.magical_damage_chain(damage, attribute)
        return 0, 0


class PureSkill(Skill):
    damage_base: int = 0

    def __call__(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, 0, 0,
            0, 0, 0, 0, 0, 0, attribute.global_damage_cof
        )

        damage = level_reduction_result(damage, attribute.level_reduction)
        damage = damage_cof_result(damage, attribute.target_damage_cof)

        return damage, damage, 0, damage
