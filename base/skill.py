from base.attribute import Attribute
from base.constant import *
from utils.damage import *

from typing import List, Union
from dataclasses import dataclass


class BaseSkill:
    _skill_name: Union[List[str], str] = ""
    skill_level: int = 0
    skill_stack: int = 1

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


class BaseDot(BaseSkill):
    _damage_base: List[int] = 0
    _interval: List[int] = []
    interval_extra: int = 0
    _tick: List[int] = []
    tick_extra: int = 0
    _max_stack: List[int] = []

    @property
    def damage_base(self):
        if not self._damage_base:
            return 0
        if self.skill_level > len(self._damage_base):
            return self._damage_base[-1]
        else:
            return self._damage_base[self.skill_level - 1]

    @damage_base.setter
    def damage_base(self, damage_base):
        if isinstance(damage_base, list):
            self._damage_base = damage_base
        else:
            self._damage_base = [damage_base]

    @property
    def interval(self):
        if not self._interval:
            return 0
        if self.skill_level > len(self._interval):
            return self._interval[-1] + self.interval_extra
        else:
            return self._interval[self.skill_level - 1] + self.interval_extra

    @interval.setter
    def interval(self, interval):
        if isinstance(interval, list):
            self._interval = interval
        else:
            self._interval = [interval]

    @property
    def tick(self):
        if not self._tick:
            return 0
        if self.skill_level > len(self._tick):
            return self._tick[-1] + self.tick_extra
        else:
            return self._tick[self.skill_level - 1] + self.tick_extra

    @tick.setter
    def tick(self, tick):
        if isinstance(tick, list):
            self._tick = tick
        else:
            self._tick = [tick]

    @property
    def max_stack(self):
        if not self._max_stack:
            return 0
        if self.skill_level > len(self._max_stack):
            return self._max_stack[-1]
        else:
            return self._max_stack[self.skill_level - 1]

    @max_stack.setter
    def max_stack(self, max_stack):
        if isinstance(max_stack, list):
            self._max_stack = max_stack
        else:
            self._max_stack = [max_stack]


class BaseDamage(BaseSkill):
    PHYSICAL_KINDS = ["Physics"]
    MAGICAL_KINDS = ["SolarMagic", "LunarMagic", "NeutralMagic", "Poison"]
    kind_type: str = ""
    physical_call: int = 0
    magical_call: int = 0
    surplus_call: int = 0

    _physical_damage_base: List[int] = []
    _physical_damage_rand: List[int] = []
    _magical_damage_base: List[int] = []
    _magical_damage_rand: List[int] = []

    _prepare_frame: List[int] = []
    _channel_interval: List[int] = []
    _weapon_damage_cof: List[int] = []
    _global_damage_cof: List[float] = []

    prepare_frame_extra: int = 0
    channel_interval_extra: float = 1.
    global_damage_cof_extra: float = 1.

    damage_addition: int = 0
    damage_addition_extra: int = 0

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
        return self.physical_call or self.magical_call

    @property
    def damage_call(self):
        return self.surplus_call or self.attack_power_call

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
        return PHYSICAL_ATTACK_POWER_COF(self.channel_interval + self.prepare_frame)

    @property
    def magical_attack_power_cof(self):
        return MAGICAL_ATTACK_POWER_COF(self.channel_interval + self.prepare_frame)

    def pre_damage(self, attribute):
        attribute.global_damage_cof *= self.global_damage_cof
        attribute.physical_attack_power_gain += self.physical_attack_power_gain
        attribute.magical_attack_power_gain += self.magical_attack_power_gain
        attribute.physical_critical_strike_rate += self.physical_critical_strike_rate
        attribute.magical_critical_strike_rate += self.magical_critical_strike_rate
        attribute.physical_critical_power_rate += self.physical_critical_power_rate
        attribute.magical_critical_power_rate += self.magical_critical_power_rate
        attribute.physical_shield_gain += self.physical_shield_gain
        attribute.magical_shield_gain += self.magical_shield_gain
        attribute.pve_addition += self.pve_addition

    def post_damage(self, attribute):
        attribute.global_damage_cof /= self.global_damage_cof
        attribute.physical_attack_power_gain -= self.physical_attack_power_gain
        attribute.magical_attack_power_gain -= self.magical_attack_power_gain
        attribute.physical_critical_strike_rate -= self.physical_critical_strike_rate
        attribute.magical_critical_strike_rate -= self.magical_critical_strike_rate
        attribute.physical_critical_power_rate -= self.physical_critical_power_rate
        attribute.magical_critical_power_rate -= self.magical_critical_power_rate
        attribute.physical_shield_gain -= self.physical_shield_gain
        attribute.magical_shield_gain -= self.magical_shield_gain
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

    def call_physical_damage(self, attribute: Attribute):
        damage = init_result(
            self.physical_damage_base, self.physical_damage_rand, attribute.damage_gain,
            self.physical_attack_power_cof, attribute.physical_attack_power,
            self.weapon_damage_cof, attribute.weapon_damage,
            0, 0
        ) * attribute.global_damage_cof
        if not damage:
            return 0, 0
        damage = damage_addition_result(
            damage, attribute.physical_damage_addition + self.damage_addition, self.damage_addition_extra
        )
        damage = overcome_result(
            damage, attribute.physical_overcome, attribute.level_shield_base + attribute.physical_shield_base,
            attribute.physical_shield_gain, attribute.physical_shield_ignore, attribute.shield_constant
        )
        critical_damage = critical_result(damage, self.critical_power(attribute))
        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.strain)
        critical_damage = strain_result(critical_damage, attribute.strain)
        damage = pve_addition_result(damage, attribute.pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition)
        damage = damage_cof_result(damage, attribute.physical_damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.physical_damage_cof)
        damage = vulnerable_result(damage, attribute.physical_vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.physical_vulnerable)
        return damage, critical_damage

    def call_magical_damage(self, attribute: Attribute):
        damage = init_result(
            self.magical_damage_base, self.magical_damage_rand, attribute.damage_gain,
            self.magical_attack_power_cof, attribute.magical_attack_power,
            self.weapon_damage_cof, attribute.weapon_damage,
            0, 0
        ) * attribute.global_damage_cof
        if not damage:
            return 0, 0
        damage = damage_addition_result(
            damage, attribute.magical_damage_addition + self.damage_addition, self.damage_addition_extra
        )
        damage = overcome_result(
            damage, attribute.magical_overcome, attribute.level_shield_base + attribute.magical_shield_base,
            attribute.magical_shield_gain, attribute.magical_shield_ignore, attribute.shield_constant
        )
        critical_damage = critical_result(damage, self.critical_power(attribute))
        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.strain)
        critical_damage = strain_result(critical_damage, attribute.strain)
        damage = pve_addition_result(damage, attribute.pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition)
        damage = damage_cof_result(damage, attribute.magical_damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.magical_damage_cof)
        damage = vulnerable_result(damage, attribute.magical_vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.magical_vulnerable)
        return damage, critical_damage

    def call_surplus_damage(self, attribute: Attribute):
        damage = init_result(
            0, 0, 0, 0, 0, 0, 0, SURPLUS_COF, attribute.surplus
        ) * attribute.global_damage_cof
        if not damage:
            return 0, 0
        damage = damage_addition_result(
            damage, attribute.damage_addition + self.damage_addition, self.damage_addition_extra
        )
        damage = overcome_result(
            damage, attribute.overcome, attribute.level_shield_base + attribute.shield_base,
            attribute.shield_gain, attribute.shield_ignore, attribute.shield_constant
        )
        critical_damage = critical_result(damage, self.critical_power(attribute))
        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.strain)
        critical_damage = strain_result(critical_damage, attribute.strain)
        damage = pve_addition_result(damage, attribute.pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition)
        damage = damage_cof_result(damage, attribute.damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.damage_cof)
        damage = vulnerable_result(damage, attribute.vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.vulnerable)
        return damage, critical_damage

    def __call__(self, attribute: Attribute):
        self.pre_damage(attribute)
        total_damage, total_critical_damage = 0, 0
        if self.physical_call:
            damage, critical_damage = self.call_physical_damage(attribute)
            total_damage += damage * self.physical_call
            total_critical_damage += critical_damage * self.physical_call
        if self.magical_call:
            damage, critical_damage = self.call_magical_damage(attribute)
            total_damage += damage * self.magical_call
            total_critical_damage += critical_damage * self.magical_call
        if self.surplus_call:
            damage, critical_damage = self.call_surplus_damage(attribute)
            total_damage += damage * self.surplus_call
            total_critical_damage += critical_damage * self.surplus_call

        critical_strike = min(self.critical_strike(attribute), 1)
        expected_damage = total_damage * (1 - critical_strike) + total_critical_damage * critical_strike
        self.post_damage(attribute)
        return int(total_damage), int(total_critical_damage), critical_strike, expected_damage


@dataclass
class Skill(BaseDamage, BaseDot):
    skill_id: int

    activate: bool = True

    recipe_type: int = 0
    event_mask_1: int = 0
    event_mask_2: int = 0

    bind_dot: int = 0
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

    @property
    def display_name(self):
        return f"{self.skill_name}#{self.skill_id}-{self.skill_level}-{self.skill_stack}"

    def pre_record(self, parser):
        for (buff_id, buff_level), buff_stack in self.pre_buffs.items():
            buff_level = buff_level if buff_level else self.skill_level
            parser.refresh_buff(buff_id, buff_level, buff_stack)
        for (buff_id, buff_level), buff_stack in self.pre_target_buffs.items():
            buff_level = buff_level if buff_level else self.skill_level
            parser.refresh_target_buff(buff_id, buff_level, buff_stack)
        for effect in self.pre_effects:
            effect(parser)

    def record(self, critical, parser):
        if self.bind_dot:
            self.dot_add(parser)
        if self.consume_dot:
            self.dot_consume(parser)
        if self.pet_buffs:
            self.pet_create(parser)
        if self.damage_call:
            self.damage(critical, parser)

    def post_record(self, parser):
        for (buff_id, buff_level), buff_stack in self.post_buffs.items():
            buff_level = buff_level if buff_level else self.skill_level
            parser.refresh_buff(buff_id, buff_level, buff_stack)
        for (buff_id, buff_level), buff_stack in self.post_target_buffs.items():
            buff_level = buff_level if buff_level else self.skill_level
            parser.refresh_target_buff(buff_id, buff_level, buff_stack)
        for effect in self.post_effects:
            effect(parser)

    def parse(self, critical, parser):
        self.pre_record(parser)
        self.record(critical, parser)
        self.post_record(parser)

    def damage(self, critical, parser):
        skill_tuple = ((self.skill_id, self.skill_level), tuple())
        status_tuple = parser.status
        parser.current_records[skill_tuple][status_tuple].append((parser.current_frame - parser.start_frame, critical))

    def pet_create(self, parser):
        pet_buffs = {}
        for (buff_id, buff_level), buff_stack in self.pet_buffs.items():
            buff_level = buff_level if buff_level else self.skill_level
            pet_buffs[(buff_id, buff_level)] = buff_stack
        for _ in range(self.pet_count):
            parser.current_next_pet_buff_stacks.append(pet_buffs.copy())

    def dot_add(self, parser):
        bind_dot: Dot = parser.current_school.skills[self.bind_dot]
        if not parser.current_dot_ticks.get(self.bind_dot):
            parser.current_dot_stacks[self.bind_dot] = 0
        parser.current_dot_ticks[self.bind_dot] = bind_dot.tick
        parser.current_dot_stacks[self.bind_dot] = parser.current_dot_stacks.get(self.bind_dot, 0) + 1
        parser.current_dot_skills[self.bind_dot] = (self.skill_id, self.skill_level)
        parser.current_dot_snapshot[self.bind_dot] = parser.current_buff_stacks.copy()

    def dot_consume(self, parser):
        if not (last_dot := parser.current_last_dot.pop(self.consume_dot, None)):
            return
        skill_tuple, status_tuple = last_dot

        (skill_id, skill_level), (dot_skill_id, dot_skill_level, dot_skill_stack) = skill_tuple
        parser.current_dot_ticks[skill_id] += 1
        if not self.consume_tick:
            tick = parser.current_dot_ticks[skill_id]
        else:
            tick = min(parser.current_dot_ticks[skill_id], self.consume_tick)
        new_skill_tuple = ((skill_id, skill_level), (dot_skill_id, dot_skill_level, dot_skill_stack * tick))
        parser.current_records[new_skill_tuple][status_tuple].append(
            parser.current_records[skill_tuple][status_tuple].pop()
        )
        parser.current_dot_ticks[skill_id] -= tick


class Dot(Skill):
    bind_skill: Skill

    @property
    def display_name(self):
        return f"{super().display_name}({self.bind_skill.skill_id}-{self.bind_skill.skill_level})"

    @property
    def physical_attack_power_cof(self):
        return PHYSICAL_DOT_ATTACK_POWER_COF(self.bind_skill.channel_interval, self.interval, self.tick)

    @property
    def magical_attack_power_cof(self):
        return MAGICAL_DOT_ATTACK_POWER_COF(self.bind_skill.channel_interval, self.interval, self.tick)

    def critical_strike(self, attribute: Attribute):
        return self.bind_skill.critical_strike(attribute)

    def critical_power(self, attribute: Attribute):
        return self.bind_skill.critical_power(attribute)

    def call_physical_damage(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, 0, attribute.damage_gain,
            self.physical_attack_power_cof, attribute.physical_attack_power, 0, 0, 0, 0
        ) * attribute.global_damage_cof
        if not damage:
            return 0, 0
        damage = damage_addition_result(damage, attribute.physical_damage_addition, self.damage_addition_extra)
        damage = overcome_result(
            damage, attribute.physical_overcome, attribute.level_shield_base + attribute.physical_shield_base,
            attribute.physical_shield_gain, attribute.physical_shield_ignore, attribute.shield_constant
        )
        critical_damage = critical_result(damage, self.critical_power(attribute))
        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.strain)
        critical_damage = strain_result(critical_damage, attribute.strain)
        damage = pve_addition_result(damage, attribute.pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition)
        damage = damage_cof_result(damage, attribute.physical_damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.physical_damage_cof)
        damage = vulnerable_result(damage, attribute.physical_vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.physical_vulnerable)
        return damage, critical_damage

    def call_magical_damage(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, 0, attribute.damage_gain,
            self.magical_attack_power_cof, attribute.magical_attack_power, 0, 0, 0, 0
        ) * attribute.global_damage_cof
        if not damage:
            return 0, 0
        damage = damage_addition_result(damage, attribute.magical_damage_addition, self.damage_addition_extra)
        damage = overcome_result(
            damage, attribute.magical_overcome, attribute.level_shield_base + attribute.magical_shield_base,
            attribute.magical_shield_gain, attribute.magical_shield_ignore, attribute.shield_constant
        )
        critical_damage = critical_result(damage, self.critical_power(attribute))
        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.strain)
        critical_damage = strain_result(critical_damage, attribute.strain)
        damage = pve_addition_result(damage, attribute.pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition)
        damage = damage_cof_result(damage, attribute.magical_damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.magical_damage_cof)
        damage = vulnerable_result(damage, attribute.magical_vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.magical_vulnerable)
        return damage, critical_damage

    def damage(self, critical, parser):
        dot_skill_id, dot_skill_level = parser.current_dot_skills[self.skill_id]
        dot_skill_stack = min(self.max_stack, parser.current_dot_stacks[self.skill_id])
        skill_tuple = ((self.skill_id, self.skill_level), (dot_skill_id, dot_skill_level, dot_skill_stack))
        status_tuple = parser.status
        parser.current_dot_ticks[self.skill_id] -= 1
        parser.current_last_dot[self.skill_id] = (skill_tuple, status_tuple)
        parser.current_records[skill_tuple][status_tuple].append((parser.current_frame - parser.start_frame, critical))

    def __call__(self, attribute: Attribute):
        self.bind_skill.pre_damage(attribute)
        total_damage, total_critical_damage = 0, 0
        if self.physical_call:
            damage, critical_damage = self.call_physical_damage(attribute)
            total_damage += damage * self.skill_stack
            total_critical_damage += critical_damage * self.skill_stack
        if self.magical_call:
            damage, critical_damage = self.call_magical_damage(attribute)
            total_damage += damage * self.skill_stack
            total_critical_damage += critical_damage * self.skill_stack

        critical_strike = min(self.critical_strike(attribute), 1)
        expected_damage = total_damage * (1 - critical_strike) + total_critical_damage * critical_strike
        self.bind_skill.post_damage(attribute)
        return int(total_damage), int(total_critical_damage), critical_strike, expected_damage


class NpcSkill(Skill):
    pass


class PetSkill(Skill):
    def call_magical_damage(self, attribute: Attribute):
        attack_power = int(attribute.magical_attack_power * 0.87 + attribute.surplus * 59 / 1664)
        damage = init_result(
            self.magical_damage_base, self.magical_damage_rand, attribute.damage_gain,
            self.magical_attack_power_cof, attack_power,
            self.weapon_damage_cof, attribute.weapon_damage,
            0, 0
        ) * attribute.global_damage_cof
        if not damage:
            return 0, 0
        damage = damage_addition_result(damage, attribute.magical_damage_addition, self.damage_addition_extra)
        damage = overcome_result(
            damage, attribute.magical_overcome, attribute.level_shield_base + attribute.magical_shield_base,
            attribute.magical_shield_gain, 0, attribute.shield_constant
        )
        critical_damage = critical_result(damage, self.critical_power(attribute))
        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.strain)
        critical_damage = strain_result(critical_damage, attribute.strain)
        # damage = pve_addition_result(damage, attribute.pve_addition)
        # critical_damage = pve_addition_result(critical_damage, attribute.pve_addition)
        damage = damage_cof_result(damage, attribute.magical_damage_cof)
        critical_damage = damage_cof_result(critical_damage, attribute.magical_damage_cof)
        damage = vulnerable_result(damage, attribute.magical_vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.magical_vulnerable)
        return damage, critical_damage


class PureSkill(Skill):
    damage_base: int = 0

    def __call__(self, attribute: Attribute):
        damage = init_result(self.damage_base, 0, 0, 0, 0, 0, 0, 0)

        damage = level_reduction_result(damage, attribute.level_reduction)
        damage = damage_cof_result(damage, attribute.damage_cof)

        return damage, damage, damage, 0
