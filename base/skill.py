from dataclasses import dataclass
from typing import List

from assets.skills import SKILLS
from base.attribute import Attribute, PhysicalAttribute
from base.constant import *
from utils.damage import *


class BaseSkill:
    skill_id: int = 0
    _skill_name: List[str] = None
    skill_level: int = 0

    def set_asset(self):
        for attr, value in SKILLS.get(self.skill_id, {}).items():
            setattr(self, attr, value)

    @property
    def display_name(self):
        return f"{self.skill_name}#{self.skill_id}-{self.skill_level}"

    @property
    def skill_name(self):
        if not self._skill_name:
            return ""
        elif self.skill_level > len(self._skill_name):
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
    kind_type: str = ""
    platform: int

    _prepare_frame: List[int] = []
    _channel_interval: List[int] = []
    _weapon_damage_cof: List[int] = []
    _global_damage_factor: List[float] = []

    skill_cof: int = 0
    dot_cof: int = 0
    _surplus_cof: int = 0

    prepare_frame_extra: int = 0
    channel_interval_extra: float = 1.
    global_damage_factor_extra: float = 1.

    _damage_addition: List[int] = []
    damage_addition_extra: int = 0
    move_state_damage_addition: int = 0

    _pve_addition: List[int] = []
    pve_addition_extra: int = 0

    physical_attack_power_base: List[int] = []
    magical_attack_power_base: List[int] = []

    @property
    def prepare_frame(self):
        if not self._prepare_frame:
            return 0
        elif self.skill_level > len(self._prepare_frame):
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
    def global_damage_factor(self):
        if not self._global_damage_factor:
            return self.global_damage_factor_extra
        elif self.skill_level > len(self._global_damage_factor):
            return GLOBAL_DAMAGE_COF(self._global_damage_factor[-1]) * self.global_damage_factor_extra
        else:
            return GLOBAL_DAMAGE_COF(self._global_damage_factor[self.skill_level - 1]) * self.global_damage_factor_extra

    @global_damage_factor.setter
    def global_damage_factor(self, global_damage_factor):
        if isinstance(global_damage_factor, list):
            self._global_damage_factor = global_damage_factor
        else:
            self._global_damage_factor = [global_damage_factor]

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
    def pve_addition(self):
        if not self._pve_addition:
            return self.pve_addition_extra
        elif self.skill_level > len(self._pve_addition):
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

    def call_surplus(self, attribute):
        return init_result(
            0, 0, 0, 0, 0, 0, 0, self.surplus_cof, attribute.surplus, attribute.global_damage_factor
        )

    def critical_strike(self, attribute: Attribute):
        if self.kind_type == "Physics":
            return attribute.physical_critical_strike
        elif self.kind_type == "SolarMagic":
            return attribute.solar_critical_strike
        elif self.kind_type == "LunarMagic":
            return attribute.lunar_critical_strike
        elif self.kind_type == "NeutralMagic":
            return attribute.neutral_critical_strike
        elif self.kind_type == "Poison":
            return attribute.poison_critical_strike
        else:
            return attribute.critical_strike

    def critical_power(self, attribute: Attribute):
        if self.kind_type == "Physics":
            return attribute.physical_critical_power
        elif self.kind_type == "SolarMagic":
            return attribute.solar_critical_power
        elif self.kind_type == "LunarMagic":
            return attribute.lunar_critical_power
        elif self.kind_type == "NeutralMagic":
            return attribute.neutral_critical_power
        elif self.kind_type == "Poison":
            return attribute.poison_critical_power
        else:
            return attribute.critical_power

    def general_damage_chain(self, damage: int, attribute: Attribute):
        critical_damage = critical_result(damage, self.critical_power(attribute))
        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.strain)
        critical_damage = strain_result(critical_damage, attribute.strain)
        damage = pve_addition_result(damage, attribute.pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition)
        return damage, critical_damage

    def pre_damage(self, attribute):
        attribute.global_damage_factor *= self.global_damage_factor
        attribute.all_damage_addition += self.damage_addition
        attribute.pve_addition_base += self.pve_addition

    def post_damage(self, attribute):
        attribute.global_damage_factor /= self.global_damage_factor
        attribute.all_damage_addition -= self.damage_addition
        attribute.pve_addition_base -= self.pve_addition


class PhysicalDamage(BaseDamage):
    _physical_damage_call: List[int] = []
    _physical_surplus_call: List[int] = []

    _physical_damage_base: List[int] = []
    _physical_damage_rand: List[int] = []

    _physical_attack_power_gain: List[int] = []

    _physical_critical_strike_rate: List[int] = []
    physical_critical_strike_rate_extra: int = 0
    _physical_critical_power_rate: List[int] = []
    physical_critical_power_rate_extra: int = 0
    _physical_shield_gain: List[int] = []
    physical_shield_gain_extra: int = 0

    @property
    def physical_damage_call(self):
        if not self._physical_damage_call:
            return 0
        elif self.skill_level > len(self._physical_damage_call):
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
    def physical_surplus_call(self):
        if not self._physical_surplus_call:
            return 0
        elif self.skill_level > len(self._physical_surplus_call):
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
    def physical_damage_base(self):
        if not self._physical_damage_base:
            return 0
        elif self.skill_level > len(self._physical_damage_base):
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
        elif self.skill_level > len(self._physical_damage_rand):
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
    def physical_attack_power_gain(self):
        if not self._physical_attack_power_gain:
            return 0
        elif self.skill_level > len(self._physical_attack_power_gain):
            return self._physical_attack_power_gain[-1]
        else:
            return self._physical_attack_power_gain[self.skill_level - 1]

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

    def physical_damage_chain(self, damage: int, attribute: Attribute):
        damage = damage_addition_result(damage, attribute.physical_damage_addition, self.move_state_damage_addition)
        damage = overcome_result(
            damage, attribute.physical_overcome, attribute.all_shield_ignore,
            attribute.target.physical_shield, attribute.target.shield_constant
        )
        damage, critical_damage = self.general_damage_chain(damage, attribute)
        damage = damage_cof_result(damage, attribute.target.physical_damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.target.physical_damage_cof)
        return damage, critical_damage

    def call_physical_damage(self, attribute: Attribute):
        damage = init_result(
            self.physical_damage_base, self.physical_damage_rand, attribute.damage_gain,
            self.physical_attack_power_cof, attribute.physical_attack_power,
            self.weapon_damage_cof, attribute.weapon_damage,
            0, 0, attribute.global_damage_factor
        )
        if damage:
            return self.physical_damage_chain(damage, attribute)
        return 0, 0

    def call_physical_surplus(self, attribute: Attribute):
        if damage := self.call_surplus(attribute):
            return self.physical_damage_chain(damage, attribute)
        return 0, 0

    def pre_damage(self, attribute):
        attribute.physical_attack_power_gain += self.physical_attack_power_gain
        attribute.physical_critical_strike_rate += self.physical_critical_strike_rate
        attribute.physical_critical_power_rate += self.physical_critical_power_rate
        attribute.target.physical_shield_gain += self.physical_shield_gain

    def post_damage(self, attribute):
        attribute.physical_attack_power_gain -= self.physical_attack_power_gain
        attribute.physical_critical_strike_rate -= self.physical_critical_strike_rate
        attribute.physical_critical_power_rate -= self.physical_critical_power_rate
        attribute.target.physical_shield_gain -= self.physical_shield_gain


class SolarDamage(BaseDamage):
    _solar_damage_call: List[int] = []
    _solar_surplus_call: List[int] = []

    _solar_damage_base: List[int] = []
    _solar_damage_rand: List[int] = []

    _solar_attack_power_gain: List[int] = []
    solar_attack_power_gain_extra: int = 0
    _solar_critical_strike_rate: List[int] = []
    solar_critical_strike_rate_extra: int = 0
    _solar_critical_power_rate: List[int] = []
    solar_critical_power_rate_extra: int = 0
    _solar_shield_gain: List[int] = []
    solar_shield_gain_extra: int = 0

    @property
    def solar_damage_call(self):
        if not self._solar_damage_call:
            return 0
        elif self.skill_level > len(self._solar_damage_call):
            return self._solar_damage_call[-1]
        else:
            return self._solar_damage_call[self.skill_level - 1]

    @solar_damage_call.setter
    def solar_damage_call(self, solar_damage_call):
        if isinstance(solar_damage_call, list):
            self._solar_damage_call = solar_damage_call
        else:
            self._solar_damage_call = [solar_damage_call]

    @property
    def solar_surplus_call(self):
        if not self._solar_surplus_call:
            return 0
        elif self.skill_level > len(self._solar_surplus_call):
            return self._solar_surplus_call[-1]
        else:
            return self._solar_surplus_call[self.skill_level - 1]

    @solar_surplus_call.setter
    def solar_surplus_call(self, solar_surplus_call):
        if isinstance(solar_surplus_call, list):
            self._solar_surplus_call = solar_surplus_call
        else:
            self._solar_surplus_call = [solar_surplus_call]

    @property
    def solar_damage_base(self):
        if not self._solar_damage_base:
            return 0
        elif self.skill_level > len(self._solar_damage_base):
            return self._solar_damage_base[-1]
        else:
            return self._solar_damage_base[self.skill_level - 1]

    @solar_damage_base.setter
    def solar_damage_base(self, solar_damage_base):
        if isinstance(solar_damage_base, list):
            self._solar_damage_base = solar_damage_base
        else:
            self._solar_damage_base = [solar_damage_base]

    @property
    def solar_damage_rand(self):
        if not self._solar_damage_rand:
            return 0
        elif self.skill_level > len(self._solar_damage_rand):
            return self._solar_damage_rand[-1]
        else:
            return self._solar_damage_rand[self.skill_level - 1]

    @solar_damage_rand.setter
    def solar_damage_rand(self, solar_damage_rand):
        if isinstance(solar_damage_rand, list):
            self._solar_damage_rand = solar_damage_rand
        else:
            self._solar_damage_rand = [solar_damage_rand]

    @property
    def solar_attack_power_gain(self):
        if not self._solar_attack_power_gain:
            return self.solar_attack_power_gain_extra
        elif self.skill_level > len(self._solar_attack_power_gain):
            return self._solar_attack_power_gain[-1] + self.solar_attack_power_gain_extra
        else:
            return self._solar_attack_power_gain[self.skill_level - 1] + self.solar_attack_power_gain_extra

    @solar_attack_power_gain.setter
    def solar_attack_power_gain(self, solar_attack_power_gain):
        if isinstance(solar_attack_power_gain, list):
            self._solar_attack_power_gain = solar_attack_power_gain
        else:
            self._solar_attack_power_gain = [solar_attack_power_gain]

    @property
    def solar_critical_strike_rate(self):
        if not self._solar_critical_strike_rate:
            return self.solar_critical_strike_rate_extra
        elif self.skill_level > len(self._solar_critical_strike_rate):
            return self._solar_critical_strike_rate[-1] + self.solar_critical_strike_rate_extra
        else:
            return self._solar_critical_strike_rate[self.skill_level - 1] + self.solar_critical_strike_rate_extra

    @solar_critical_strike_rate.setter
    def solar_critical_strike_rate(self, solar_critical_strike_rate):
        if isinstance(solar_critical_strike_rate, list):
            self._solar_critical_strike_rate = solar_critical_strike_rate
        else:
            self._solar_critical_strike_rate = [solar_critical_strike_rate]

    @property
    def solar_critical_power_rate(self):
        if not self._solar_critical_power_rate:
            return self.solar_critical_power_rate_extra
        elif self.skill_level > len(self._solar_critical_power_rate):
            return self._solar_critical_power_rate[-1] + self.solar_critical_power_rate_extra
        else:
            return self._solar_critical_power_rate[self.skill_level - 1] + self.solar_critical_power_rate_extra

    @solar_critical_power_rate.setter
    def solar_critical_power_rate(self, solar_critical_power_rate):
        if isinstance(solar_critical_power_rate, list):
            self._solar_critical_power_rate = solar_critical_power_rate
        else:
            self._solar_critical_power_rate = [solar_critical_power_rate]

    @property
    def solar_shield_gain(self):
        if not self._solar_shield_gain:
            return self.solar_shield_gain_extra
        elif self.skill_level > len(self._solar_shield_gain):
            return self._solar_shield_gain[-1] + self.solar_shield_gain_extra
        else:
            return self._solar_shield_gain[self.skill_level - 1] + self.solar_shield_gain_extra

    @solar_shield_gain.setter
    def solar_shield_gain(self, solar_shield_gain):
        if isinstance(solar_shield_gain, list):
            self._solar_shield_gain = solar_shield_gain
        else:
            self._solar_shield_gain = [solar_shield_gain]

    def solar_damage_chain(self, damage: int, attribute: Attribute):
        damage = damage_addition_result(damage, attribute.magical_damage_addition, self.move_state_damage_addition)
        damage = overcome_result(
            damage, attribute.solar_overcome, attribute.all_shield_ignore,
            attribute.target.solar_shield, attribute.target.shield_constant
        )
        damage, critical_damage = self.general_damage_chain(damage, attribute)
        damage = damage_cof_result(damage, attribute.target.solar_damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.target.solar_damage_cof)
        return damage, critical_damage

    def call_solar_damage(self, attribute: Attribute):
        damage = init_result(
            self.solar_damage_base, self.solar_damage_rand, attribute.damage_gain,
            self.magical_attack_power_cof, attribute.solar_attack_power,
            0, 0, 0, 0, attribute.global_damage_factor
        )
        if damage:
            return self.solar_damage_chain(damage, attribute)
        return 0, 0

    def call_solar_surplus(self, attribute: Attribute):
        if damage := self.call_surplus(attribute):
            return self.solar_damage_chain(damage, attribute)
        return 0, 0

    def pre_damage(self, attribute):
        attribute.solar_attack_power_gain += self.solar_attack_power_gain
        attribute.solar_critical_strike_rate += self.solar_critical_strike_rate
        attribute.solar_critical_power_rate += self.solar_critical_power_rate
        attribute.target.solar_shield_gain += self.solar_shield_gain

    def post_damage(self, attribute):
        attribute.solar_attack_power_gain -= self.solar_attack_power_gain
        attribute.solar_critical_strike_rate -= self.solar_critical_strike_rate
        attribute.solar_critical_power_rate -= self.solar_critical_power_rate
        attribute.target.solar_shield_gain -= self.solar_shield_gain


class LunarDamage(BaseDamage):
    _lunar_damage_call: List[int] = []
    _lunar_surplus_call: List[int] = []

    _lunar_damage_base: List[int] = []
    _lunar_damage_rand: List[int] = []

    _lunar_attack_power_gain: List[int] = []
    lunar_attack_power_gain_extra: int = 0
    _lunar_critical_strike_rate: List[int] = []
    lunar_critical_strike_rate_extra: int = 0
    _lunar_critical_power_rate: List[int] = []
    lunar_critical_power_rate_extra: int = 0
    _lunar_shield_gain: List[int] = []
    lunar_shield_gain_extra: int = 0

    @property
    def lunar_damage_call(self):
        if not self._lunar_damage_call:
            return 0
        elif self.skill_level > len(self._lunar_damage_call):
            return self._lunar_damage_call[-1]
        else:
            return self._lunar_damage_call[self.skill_level - 1]

    @lunar_damage_call.setter
    def lunar_damage_call(self, lunar_damage_call):
        if isinstance(lunar_damage_call, list):
            self._lunar_damage_call = lunar_damage_call
        else:
            self._lunar_damage_call = [lunar_damage_call]

    @property
    def lunar_surplus_call(self):
        if not self._lunar_surplus_call:
            return 0
        elif self.skill_level > len(self._lunar_surplus_call):
            return self._lunar_surplus_call[-1]
        else:
            return self._lunar_surplus_call[self.skill_level - 1]

    @lunar_surplus_call.setter
    def lunar_surplus_call(self, lunar_surplus_call):
        if isinstance(lunar_surplus_call, list):
            self._lunar_surplus_call = lunar_surplus_call
        else:
            self._lunar_surplus_call = [lunar_surplus_call]

    @property
    def lunar_damage_base(self):
        if not self._lunar_damage_base:
            return 0
        elif self.skill_level > len(self._lunar_damage_base):
            return self._lunar_damage_base[-1]
        else:
            return self._lunar_damage_base[self.skill_level - 1]

    @lunar_damage_base.setter
    def lunar_damage_base(self, lunar_damage_base):
        if isinstance(lunar_damage_base, list):
            self._lunar_damage_base = lunar_damage_base
        else:
            self._lunar_damage_base = [lunar_damage_base]

    @property
    def lunar_damage_rand(self):
        if not self._lunar_damage_rand:
            return 0
        elif self.skill_level > len(self._lunar_damage_rand):
            return self._lunar_damage_rand[-1]
        else:
            return self._lunar_damage_rand[self.skill_level - 1]

    @lunar_damage_rand.setter
    def lunar_damage_rand(self, lunar_damage_rand):
        if isinstance(lunar_damage_rand, list):
            self._lunar_damage_rand = lunar_damage_rand
        else:
            self._lunar_damage_rand = [lunar_damage_rand]

    @property
    def lunar_attack_power_gain(self):
        if not self._lunar_attack_power_gain:
            return self.lunar_attack_power_gain_extra
        elif self.skill_level > len(self._lunar_attack_power_gain):
            return self._lunar_attack_power_gain[-1] + self.lunar_attack_power_gain_extra
        else:
            return self._lunar_attack_power_gain[self.skill_level - 1] + self.lunar_attack_power_gain_extra

    @lunar_attack_power_gain.setter
    def lunar_attack_power_gain(self, lunar_attack_power_gain):
        if isinstance(lunar_attack_power_gain, list):
            self._lunar_attack_power_gain = lunar_attack_power_gain
        else:
            self._lunar_attack_power_gain = [lunar_attack_power_gain]

    @property
    def lunar_critical_strike_rate(self):
        if not self._lunar_critical_strike_rate:
            return self.lunar_critical_strike_rate_extra
        elif self.skill_level > len(self._lunar_critical_strike_rate):
            return self._lunar_critical_strike_rate[-1] + self.lunar_critical_strike_rate_extra
        else:
            return self._lunar_critical_strike_rate[self.skill_level - 1] + self.lunar_critical_strike_rate_extra

    @lunar_critical_strike_rate.setter
    def lunar_critical_strike_rate(self, lunar_critical_strike_rate):
        if isinstance(lunar_critical_strike_rate, list):
            self._lunar_critical_strike_rate = lunar_critical_strike_rate
        else:
            self._lunar_critical_strike_rate = [lunar_critical_strike_rate]

    @property
    def lunar_critical_power_rate(self):
        if not self._lunar_critical_power_rate:
            return self.lunar_critical_power_rate_extra
        elif self.skill_level > len(self._lunar_critical_power_rate):
            return self._lunar_critical_power_rate[-1] + self.lunar_critical_power_rate_extra
        else:
            return self._lunar_critical_power_rate[self.skill_level - 1] + self.lunar_critical_power_rate_extra

    @lunar_critical_power_rate.setter
    def lunar_critical_power_rate(self, lunar_critical_power_rate):
        if isinstance(lunar_critical_power_rate, list):
            self._lunar_critical_power_rate = lunar_critical_power_rate
        else:
            self._lunar_critical_power_rate = [lunar_critical_power_rate]

    @property
    def lunar_shield_gain(self):
        if not self._lunar_shield_gain:
            return self.lunar_shield_gain_extra
        elif self.skill_level > len(self._lunar_shield_gain):
            return self._lunar_shield_gain[-1] + self.lunar_shield_gain_extra
        else:
            return self._lunar_shield_gain[self.skill_level - 1] + self.lunar_shield_gain_extra

    @lunar_shield_gain.setter
    def lunar_shield_gain(self, lunar_shield_gain):
        if isinstance(lunar_shield_gain, list):
            self._lunar_shield_gain = lunar_shield_gain
        else:
            self._lunar_shield_gain = [lunar_shield_gain]

    def lunar_damage_chain(self, damage: int, attribute: Attribute):
        damage = damage_addition_result(damage, attribute.magical_damage_addition, self.move_state_damage_addition)
        damage = overcome_result(
            damage, attribute.lunar_overcome, attribute.all_shield_ignore,
            attribute.target.lunar_shield, attribute.target.shield_constant
        )
        damage, critical_damage = self.general_damage_chain(damage, attribute)
        damage = damage_cof_result(damage, attribute.target.lunar_damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.target.lunar_damage_cof)
        return damage, critical_damage

    def call_lunar_damage(self, attribute: Attribute):
        damage = init_result(
            self.lunar_damage_base, self.lunar_damage_rand, attribute.damage_gain,
            self.magical_attack_power_cof, attribute.lunar_attack_power,
            0, 0, 0, 0, attribute.global_damage_factor
        )
        if damage:
            return self.lunar_damage_chain(damage, attribute)
        return 0, 0

    def call_lunar_surplus(self, attribute: Attribute):
        if damage := self.call_surplus(attribute):
            return self.lunar_damage_chain(damage, attribute)
        return 0, 0

    def pre_damage(self, attribute):
        attribute.lunar_attack_power_gain += self.lunar_attack_power_gain
        attribute.lunar_critical_strike_rate += self.lunar_critical_strike_rate
        attribute.lunar_critical_power_rate += self.lunar_critical_power_rate
        attribute.target.lunar_shield_gain += self.lunar_shield_gain

    def post_damage(self, attribute):
        attribute.lunar_attack_power_gain -= self.lunar_attack_power_gain
        attribute.lunar_critical_strike_rate -= self.lunar_critical_strike_rate
        attribute.lunar_critical_power_rate -= self.lunar_critical_power_rate
        attribute.target.lunar_shield_gain -= self.lunar_shield_gain


class NeutralDamage(BaseDamage):
    _neutral_damage_call: List[int] = []
    _neutral_surplus_call: List[int] = []

    _neutral_damage_base: List[int] = []
    _neutral_damage_rand: List[int] = []

    _neutral_attack_power_gain: List[int] = []
    _neutral_critical_strike_rate: List[int] = []
    neutral_critical_strike_rate_extra: int = 0
    _neutral_critical_power_rate: List[int] = []
    neutral_critical_power_rate_extra: int = 0
    _neutral_shield_gain: List[int] = []
    neutral_shield_gain_extra: int = 0

    @property
    def neutral_damage_call(self):
        if not self._neutral_damage_call:
            return 0
        elif self.skill_level > len(self._neutral_damage_call):
            return self._neutral_damage_call[-1]
        else:
            return self._neutral_damage_call[self.skill_level - 1]

    @neutral_damage_call.setter
    def neutral_damage_call(self, neutral_damage_call):
        if isinstance(neutral_damage_call, list):
            self._neutral_damage_call = neutral_damage_call
        else:
            self._neutral_damage_call = [neutral_damage_call]

    @property
    def neutral_surplus_call(self):
        if not self._neutral_surplus_call:
            return 0
        elif self.skill_level > len(self._neutral_surplus_call):
            return self._neutral_surplus_call[-1]
        else:
            return self._neutral_surplus_call[self.skill_level - 1]

    @neutral_surplus_call.setter
    def neutral_surplus_call(self, neutral_surplus_call):
        if isinstance(neutral_surplus_call, list):
            self._neutral_surplus_call = neutral_surplus_call
        else:
            self._neutral_surplus_call = [neutral_surplus_call]

    @property
    def neutral_damage_base(self):
        if not self._neutral_damage_base:
            return 0
        elif self.skill_level > len(self._neutral_damage_base):
            return self._neutral_damage_base[-1]
        else:
            return self._neutral_damage_base[self.skill_level - 1]

    @neutral_damage_base.setter
    def neutral_damage_base(self, neutral_damage_base):
        if isinstance(neutral_damage_base, list):
            self._neutral_damage_base = neutral_damage_base
        else:
            self._neutral_damage_base = [neutral_damage_base]

    @property
    def neutral_damage_rand(self):
        if not self._neutral_damage_rand:
            return 0
        elif self.skill_level > len(self._neutral_damage_rand):
            return self._neutral_damage_rand[-1]
        else:
            return self._neutral_damage_rand[self.skill_level - 1]

    @neutral_damage_rand.setter
    def neutral_damage_rand(self, neutral_damage_rand):
        if isinstance(neutral_damage_rand, list):
            self._neutral_damage_rand = neutral_damage_rand
        else:
            self._neutral_damage_rand = [neutral_damage_rand]

    @property
    def neutral_attack_power_gain(self):
        if not self._neutral_attack_power_gain:
            return 0
        elif self.skill_level > len(self._neutral_attack_power_gain):
            return self._neutral_attack_power_gain[-1]
        else:
            return self._neutral_attack_power_gain[self.skill_level - 1]

    @neutral_attack_power_gain.setter
    def neutral_attack_power_gain(self, neutral_attack_power_gain):
        if isinstance(neutral_attack_power_gain, list):
            self._neutral_attack_power_gain = neutral_attack_power_gain
        else:
            self._neutral_attack_power_gain = [neutral_attack_power_gain]

    @property
    def neutral_critical_strike_rate(self):
        if not self._neutral_critical_strike_rate:
            return self.neutral_critical_strike_rate_extra
        elif self.skill_level > len(self._neutral_critical_strike_rate):
            return self._neutral_critical_strike_rate[-1] + self.neutral_critical_strike_rate_extra
        else:
            return self._neutral_critical_strike_rate[self.skill_level - 1] + self.neutral_critical_strike_rate_extra

    @neutral_critical_strike_rate.setter
    def neutral_critical_strike_rate(self, neutral_critical_strike_rate):
        if isinstance(neutral_critical_strike_rate, list):
            self._neutral_critical_strike_rate = neutral_critical_strike_rate
        else:
            self._neutral_critical_strike_rate = [neutral_critical_strike_rate]

    @property
    def neutral_critical_power_rate(self):
        if not self._neutral_critical_power_rate:
            return self.neutral_critical_power_rate_extra
        elif self.skill_level > len(self._neutral_critical_power_rate):
            return self._neutral_critical_power_rate[-1] + self.neutral_critical_power_rate_extra
        else:
            return self._neutral_critical_power_rate[self.skill_level - 1] + self.neutral_critical_power_rate_extra

    @neutral_critical_power_rate.setter
    def neutral_critical_power_rate(self, neutral_critical_power_rate):
        if isinstance(neutral_critical_power_rate, list):
            self._neutral_critical_power_rate = neutral_critical_power_rate
        else:
            self._neutral_critical_power_rate = [neutral_critical_power_rate]

    @property
    def neutral_shield_gain(self):
        if not self._neutral_shield_gain:
            return self.neutral_shield_gain_extra
        elif self.skill_level > len(self._neutral_shield_gain):
            return self._neutral_shield_gain[-1] + self.neutral_shield_gain_extra
        else:
            return self._neutral_shield_gain[self.skill_level - 1] + self.neutral_shield_gain_extra

    @neutral_shield_gain.setter
    def neutral_shield_gain(self, neutral_shield_gain):
        if isinstance(neutral_shield_gain, list):
            self._neutral_shield_gain = neutral_shield_gain
        else:
            self._neutral_shield_gain = [neutral_shield_gain]

    def neutral_damage_chain(self, damage: int, attribute: Attribute):
        damage = damage_addition_result(damage, attribute.magical_damage_addition, self.move_state_damage_addition)
        damage = overcome_result(
            damage, attribute.neutral_overcome, attribute.all_shield_ignore,
            attribute.target.neutral_shield, attribute.target.shield_constant
        )
        damage, critical_damage = self.general_damage_chain(damage, attribute)
        damage = damage_cof_result(damage, attribute.target.neutral_damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.target.neutral_damage_cof)
        return damage, critical_damage

    def call_neutral_damage(self, attribute: Attribute):
        damage = init_result(
            self.neutral_damage_base, self.neutral_damage_rand, attribute.damage_gain,
            self.magical_attack_power_cof, attribute.neutral_attack_power,
            0, 0, 0, 0, attribute.global_damage_factor
        )
        if damage:
            return self.neutral_damage_chain(damage, attribute)
        return 0, 0

    def call_neutral_surplus(self, attribute: Attribute):
        if damage := self.call_surplus(attribute):
            return self.neutral_damage_chain(damage, attribute)
        return 0, 0

    def pre_damage(self, attribute):
        attribute.neutral_attack_power_gain += self.neutral_attack_power_gain
        attribute.neutral_critical_strike_rate += self.neutral_critical_strike_rate
        attribute.neutral_critical_power_rate += self.neutral_critical_power_rate
        attribute.target.neutral_shield_gain += self.neutral_shield_gain

    def post_damage(self, attribute):
        attribute.neutral_attack_power_gain -= self.neutral_attack_power_gain
        attribute.neutral_critical_strike_rate -= self.neutral_critical_strike_rate
        attribute.neutral_critical_power_rate -= self.neutral_critical_power_rate
        attribute.target.neutral_shield_gain -= self.neutral_shield_gain


class PoisonDamage(BaseDamage):
    _poison_damage_call: List[int] = []
    _poison_surplus_call: List[int] = []

    _poison_damage_base: List[int] = []
    _poison_damage_rand: List[int] = []

    _poison_attack_power_gain: List[int] = []
    _poison_critical_strike_rate: List[int] = []
    poison_critical_strike_rate_extra: int = 0
    _poison_critical_power_rate: List[int] = []
    poison_critical_power_rate_extra: int = 0
    _poison_shield_gain: List[int] = []
    poison_shield_gain_extra: int = 0

    @property
    def poison_damage_call(self):
        if not self._poison_damage_call:
            return 0
        elif self.skill_level > len(self._poison_damage_call):
            return self._poison_damage_call[-1]
        else:
            return self._poison_damage_call[self.skill_level - 1]

    @poison_damage_call.setter
    def poison_damage_call(self, poison_damage_call):
        if isinstance(poison_damage_call, list):
            self._poison_damage_call = poison_damage_call
        else:
            self._poison_damage_call = [poison_damage_call]

    @property
    def poison_surplus_call(self):
        if not self._poison_surplus_call:
            return 0
        elif self.skill_level > len(self._poison_surplus_call):
            return self._poison_surplus_call[-1]
        else:
            return self._poison_surplus_call[self.skill_level - 1]

    @poison_surplus_call.setter
    def poison_surplus_call(self, poison_surplus_call):
        if isinstance(poison_surplus_call, list):
            self._poison_surplus_call = poison_surplus_call
        else:
            self._poison_surplus_call = [poison_surplus_call]

    @property
    def poison_damage_base(self):
        if not self._poison_damage_base:
            return 0
        elif self.skill_level > len(self._poison_damage_base):
            return self._poison_damage_base[-1]
        else:
            return self._poison_damage_base[self.skill_level - 1]

    @poison_damage_base.setter
    def poison_damage_base(self, poison_damage_base):
        if isinstance(poison_damage_base, list):
            self._poison_damage_base = poison_damage_base
        else:
            self._poison_damage_base = [poison_damage_base]

    @property
    def poison_damage_rand(self):
        if not self._poison_damage_rand:
            return 0
        elif self.skill_level > len(self._poison_damage_rand):
            return self._poison_damage_rand[-1]
        else:
            return self._poison_damage_rand[self.skill_level - 1]

    @poison_damage_rand.setter
    def poison_damage_rand(self, poison_damage_rand):
        if isinstance(poison_damage_rand, list):
            self._poison_damage_rand = poison_damage_rand
        else:
            self._poison_damage_rand = [poison_damage_rand]

    @property
    def poison_attack_power_gain(self):
        if not self._poison_attack_power_gain:
            return 0
        elif self.skill_level > len(self._poison_attack_power_gain):
            return self._poison_attack_power_gain[-1]
        else:
            return self._poison_attack_power_gain[self.skill_level - 1]

    @poison_attack_power_gain.setter
    def poison_attack_power_gain(self, poison_attack_power_gain):
        if isinstance(poison_attack_power_gain, list):
            self._poison_attack_power_gain = poison_attack_power_gain
        else:
            self._poison_attack_power_gain = [poison_attack_power_gain]

    @property
    def poison_critical_strike_rate(self):
        if not self._poison_critical_strike_rate:
            return self.poison_critical_strike_rate_extra
        elif self.skill_level > len(self._poison_critical_strike_rate):
            return self._poison_critical_strike_rate[-1] + self.poison_critical_strike_rate_extra
        else:
            return self._poison_critical_strike_rate[self.skill_level - 1] + self.poison_critical_strike_rate_extra

    @poison_critical_strike_rate.setter
    def poison_critical_strike_rate(self, poison_critical_strike_rate):
        if isinstance(poison_critical_strike_rate, list):
            self._poison_critical_strike_rate = poison_critical_strike_rate
        else:
            self._poison_critical_strike_rate = [poison_critical_strike_rate]

    @property
    def poison_critical_power_rate(self):
        if not self._poison_critical_power_rate:
            return self.poison_critical_power_rate_extra
        elif self.skill_level > len(self._poison_critical_power_rate):
            return self._poison_critical_power_rate[-1] + self.poison_critical_power_rate_extra
        else:
            return self._poison_critical_power_rate[self.skill_level - 1] + self.poison_critical_power_rate_extra

    @poison_critical_power_rate.setter
    def poison_critical_power_rate(self, poison_critical_power_rate):
        if isinstance(poison_critical_power_rate, list):
            self._poison_critical_power_rate = poison_critical_power_rate
        else:
            self._poison_critical_power_rate = [poison_critical_power_rate]

    @property
    def poison_shield_gain(self):
        if not self._poison_shield_gain:
            return self.poison_shield_gain_extra
        elif self.skill_level > len(self._poison_shield_gain):
            return self._poison_shield_gain[-1] + self.poison_shield_gain_extra
        else:
            return self._poison_shield_gain[self.skill_level - 1] + self.poison_shield_gain_extra

    @poison_shield_gain.setter
    def poison_shield_gain(self, poison_shield_gain):
        if isinstance(poison_shield_gain, list):
            self._poison_shield_gain = poison_shield_gain
        else:
            self._poison_shield_gain = [poison_shield_gain]

    def poison_damage_chain(self, damage: int, attribute: Attribute):
        damage = damage_addition_result(damage, attribute.magical_damage_addition, self.move_state_damage_addition)
        damage = overcome_result(
            damage, attribute.poison_overcome, attribute.all_shield_ignore,
            attribute.target.poison_shield, attribute.target.shield_constant
        )
        damage, critical_damage = self.general_damage_chain(damage, attribute)
        damage = damage_cof_result(damage, attribute.target.poison_damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.target.poison_damage_cof)
        return damage, critical_damage

    def call_poison_damage(self, attribute: Attribute):
        damage = init_result(
            self.poison_damage_base, self.poison_damage_rand, attribute.damage_gain,
            self.magical_attack_power_cof, attribute.poison_attack_power,
            0, 0, 0, 0, attribute.global_damage_factor
        )
        if damage:
            return self.poison_damage_chain(damage, attribute)
        return 0, 0

    def call_poison_surplus(self, attribute: Attribute):
        if damage := self.call_surplus(attribute):
            return self.poison_damage_chain(damage, attribute)
        return 0, 0

    def pre_damage(self, attribute):
        attribute.poison_attack_power_gain += self.poison_attack_power_gain
        attribute.poison_critical_strike_rate += self.poison_critical_strike_rate
        attribute.poison_critical_power_rate += self.poison_critical_power_rate
        attribute.target.poison_shield_gain += self.poison_shield_gain

    def post_damage(self, attribute):
        attribute.poison_attack_power_gain -= self.poison_attack_power_gain
        attribute.poison_critical_strike_rate -= self.poison_critical_strike_rate
        attribute.poison_critical_power_rate -= self.poison_critical_power_rate
        attribute.target.poison_shield_gain -= self.poison_shield_gain


class MagicalDamage(SolarDamage, LunarDamage, NeutralDamage, PoisonDamage):
    @property
    def magical_damage_call(self):
        return self.solar_damage_call or self.lunar_damage_call or self.neutral_damage_call or self.poison_damage_call

    @property
    def magical_surplus_call(self):
        return (self.solar_surplus_call or self.lunar_surplus_call or self.neutral_surplus_call or
                self.poison_surplus_call)

    def pre_damage(self, attribute):
        SolarDamage.pre_damage(self, attribute)
        LunarDamage.pre_damage(self, attribute)
        NeutralDamage.pre_damage(self, attribute)
        PoisonDamage.pre_damage(self, attribute)

    def post_damage(self, attribute):
        SolarDamage.post_damage(self, attribute)
        LunarDamage.post_damage(self, attribute)
        NeutralDamage.post_damage(self, attribute)
        PoisonDamage.post_damage(self, attribute)


class AdaptiveDamage(BaseDamage):
    _adaptive_damage_call: List[int] = []

    _adaptive_damage_base: List[int] = []
    _adaptive_damage_rand: List[int] = []

    @property
    def adaptive_damage_call(self):
        if not self._adaptive_damage_call:
            return 0
        elif self.skill_level > len(self._adaptive_damage_call):
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
    def adaptive_damage_base(self):
        if not self._adaptive_damage_base:
            return 0
        elif self.skill_level > len(self._adaptive_damage_base):
            return self._adaptive_damage_base[-1]
        else:
            return self._adaptive_damage_base[self.skill_level - 1]

    @adaptive_damage_base.setter
    def adaptive_damage_base(self, adaptive_damage_base):
        if isinstance(adaptive_damage_base, list):
            self._adaptive_damage_base = adaptive_damage_base
        else:
            self._adaptive_damage_base = [adaptive_damage_base]

    @property
    def adaptive_damage_rand(self):
        if not self._adaptive_damage_rand:
            return 0
        elif self.skill_level > len(self._adaptive_damage_rand):
            return self._adaptive_damage_rand[-1]
        else:
            return self._adaptive_damage_rand[self.skill_level - 1]

    @adaptive_damage_rand.setter
    def adaptive_damage_rand(self, adaptive_damage_rand):
        if isinstance(adaptive_damage_rand, list):
            self._adaptive_damage_rand = adaptive_damage_rand
        else:
            self._adaptive_damage_rand = [adaptive_damage_rand]

    def adaptive_damage_chain(self, damage: int, attribute: Attribute):
        damage = damage_addition_result(
            damage, attribute.damage_addition, self.move_state_damage_addition
        )
        damage = overcome_result(
            damage, attribute.overcome, attribute.all_damage_addition,
            attribute.target_shield, attribute.target.shield_constant
        )
        damage, critical_damage = self.general_damage_chain(damage, attribute)
        damage = damage_cof_result(damage, attribute.target_damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.target_damage_cof)
        return damage, critical_damage

    def call_adaptive_damage(self, attribute: Attribute):
        if isinstance(attribute, PhysicalAttribute):
            attack_power_cof = self.physical_attack_power_cof
        else:
            attack_power_cof = self.magical_attack_power_cof

        damage = init_result(
            self.adaptive_damage_base, self.adaptive_damage_rand, attribute.damage_gain,
            attack_power_cof, attribute.attack_power,
            0, 0, 0, 0, attribute.global_damage_factor
        )
        if damage:
            return self.adaptive_damage_chain(damage, attribute)
        return 0, 0


class Damage(PhysicalDamage, MagicalDamage, AdaptiveDamage):

    @property
    def attack_power_call(self):
        return self.physical_damage_call or self.magical_damage_call or self.adaptive_damage_call

    @property
    def surplus_call(self):
        return self.physical_surplus_call or self.magical_surplus_call

    @property
    def damage_call(self):
        return self.surplus_call or self.attack_power_call

    def pre_damage(self, attribute: Attribute):
        BaseDamage.pre_damage(self, attribute)
        PhysicalDamage.pre_damage(self, attribute)
        MagicalDamage.pre_damage(self, attribute)

    def post_damage(self, attribute: Attribute):
        BaseDamage.post_damage(self, attribute)
        PhysicalDamage.post_damage(self, attribute)
        MagicalDamage.post_damage(self, attribute)

    def __call__(self, attribute: Attribute):
        self.pre_damage(attribute)
        total_damage, total_critical_damage = 0, 0
        if self.physical_damage_call:
            damage, critical_damage = self.call_physical_damage(attribute)
            total_damage += damage * self.physical_damage_call
            total_critical_damage += critical_damage * self.physical_damage_call
        if self.solar_damage_call:
            damage, critical_damage = self.call_solar_damage(attribute)
            total_damage += damage * self.solar_damage_call
            total_critical_damage += critical_damage * self.solar_damage_call
        if self.lunar_damage_call:
            damage, critical_damage = self.call_lunar_damage(attribute)
            total_damage += damage * self.lunar_damage_call
            total_critical_damage += critical_damage * self.lunar_damage_call
        if self.neutral_damage_call:
            damage, critical_damage = self.call_neutral_damage(attribute)
            total_damage += damage * self.neutral_damage_call
            total_critical_damage += critical_damage * self.neutral_damage_call
        if self.poison_damage_call:
            damage, critical_damage = self.call_poison_damage(attribute)
            total_damage += damage * self.poison_damage_call
            total_critical_damage += critical_damage * self.poison_damage_call
        if self.adaptive_damage_call:
            damage, critical_damage = self.call_adaptive_damage(attribute)
            total_damage += damage * self.adaptive_damage_call
            total_critical_damage += critical_damage * self.adaptive_damage_call
        if self.physical_surplus_call:
            damage, critical_damage = self.call_physical_surplus(attribute)
            total_damage += damage * self.physical_surplus_call
            total_critical_damage += critical_damage * self.physical_surplus_call
        if self.solar_surplus_call:
            damage, critical_damage = self.call_solar_surplus(attribute)
            total_damage += damage * self.solar_surplus_call
            total_critical_damage += critical_damage * self.solar_surplus_call
        if self.lunar_surplus_call:
            damage, critical_damage = self.call_lunar_surplus(attribute)
            total_damage += damage * self.lunar_surplus_call
            total_critical_damage += critical_damage * self.lunar_surplus_call
        if self.neutral_surplus_call:
            damage, critical_damage = self.call_neutral_surplus(attribute)
            total_damage += damage * self.neutral_surplus_call
            total_critical_damage += critical_damage * self.neutral_surplus_call
        if self.poison_surplus_call:
            damage, critical_damage = self.call_poison_surplus(attribute)
            total_damage += damage * self.poison_surplus_call
            total_critical_damage += critical_damage * self.poison_surplus_call

        critical_strike = min(self.critical_strike(attribute), 1)
        expected_damage = total_damage * (1 - critical_strike) + total_critical_damage * critical_strike
        self.post_damage(attribute)
        return int(total_damage), int(total_critical_damage), critical_strike, expected_damage


@dataclass
class Skill(Damage):
    skill_id: int

    activate: bool = True

    max_level: int = 0

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
        damage_tuple = ((self.skill_id, self.skill_level), tuple(), tuple())
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
        (dot_id, dot_level, dot_stack), (dot_skill_id, dot_skill_level), _ = damage_tuple
        parser.current_dot_ticks[dot_id] += 1
        if not self.consume_tick:
            tick = parser.current_dot_ticks[dot_id]
        else:
            tick = min(parser.current_dot_ticks[dot_id], self.consume_tick)
        new_damage_tuple = (
            (dot_id, dot_level, dot_stack * tick), (dot_skill_id, dot_skill_level), (self.skill_id, self.skill_level)
        )
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
            0, 0, 0, 0, attribute.global_damage_factor
        )
        if damage:
            return self.physical_damage_chain(damage, attribute)
        return 0, 0


class PetSkill(Skill):
    def call_poison_damage(self, attribute: Attribute):
        attack_power = int(attribute.poison_attack_power * 0.87 + attribute.surplus * DEFAULT_SURPLUS_COF * 59 / 1664)
        damage = init_result(
            self.poison_damage_base, self.poison_damage_rand, attribute.damage_gain,
            self.magical_attack_power_cof, attack_power,
            0, 0, 0, 0, attribute.global_damage_factor
        )
        if damage:
            damage = damage_addition_result(damage, attribute.magical_damage_addition, self.move_state_damage_addition)
            damage = overcome_result(
                damage, attribute.poison_overcome, 0,
                attribute.target.poison_shield, attribute.target.shield_constant
            )
            damage, critical_damage = self.general_damage_chain(damage, attribute)
            damage = damage_cof_result(damage, attribute.target.poison_damage_cof)
            critical_damage = damage_cof_result(critical_damage, attribute.target.poison_damage_cof)
            return damage, critical_damage
        return 0, 0


class PureSkill(Skill):
    damage_base: int = 0

    def __call__(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, 0, 0,
            0, 0, 0, 0, 0, 0, attribute.global_damage_factor
        )

        damage = level_reduction_result(damage, attribute.level_reduction)
        damage = damage_cof_result(damage, attribute.target_damage_cof)

        return damage, damage, 0, damage
