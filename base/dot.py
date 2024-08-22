from dataclasses import dataclass
from typing import List

from assets.dots import DOTS
from base.attribute import Attribute
from base.buff import BaseBuff
from base.constant import PHYSICAL_DOT_ATTACK_POWER_COF, MAGICAL_DOT_ATTACK_POWER_COF
from base.skill import Skill
from utils.damage import init_result


class BaseDot(BaseBuff):
    bind_skill: Skill
    consume_skill: Skill

    physical_damage_call: int = 0
    solar_damage_call: int = 0
    lunar_damage_call: int = 0
    neutral_damage_call: int = 0
    poison_damage_call: int = 0

    _damage_base: List[int] = 0
    _interval: List[int] = []
    interval_extra: int = 0
    _tick: List[int] = []
    tick_extra: int = 0

    def set_asset(self, attrs):
        for attr, value in DOTS.get(self.buff_id, {}).items():
            setattr(self, attr, value)
        for attr, value in attrs.items():
            setattr(self, attr, value)

    @property
    def magical_damage_call(self):
        return self.solar_damage_call or self.lunar_damage_call or self.neutral_damage_call or self.poison_damage_call

    @property
    def attack_power_call(self):
        return self.physical_damage_call or self.magical_damage_call

    @property
    def surplus_call(self):
        return False

    @property
    def damage_call(self):
        return self.attack_power_call or self.surplus_call

    @property
    def damage_base(self):
        if not self._damage_base:
            return 0
        if self.buff_level > len(self._damage_base):
            return self._damage_base[-1]
        else:
            return self._damage_base[self.buff_level - 1]

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
        if self.buff_level > len(self._interval):
            return self._interval[-1] + self.interval_extra
        else:
            return self._interval[self.buff_level - 1] + self.interval_extra

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
        if self.buff_level > len(self._tick):
            return self._tick[-1] + self.tick_extra
        else:
            return self._tick[self.buff_level - 1] + self.tick_extra

    @tick.setter
    def tick(self, tick):
        if isinstance(tick, list):
            self._tick = tick
        else:
            self._tick = [tick]

    @property
    def origin_tick(self):
        return self.tick - self.tick_extra


@dataclass
class Dot(BaseDot):
    buff_id: int

    activate: bool = True

    @property
    def display_name(self):
        if self.consume_skill:
            return f"{super().display_name}({self.bind_skill.display_name}|{self.consume_skill.display_name})"
        else:
            return f"{super().display_name}({self.bind_skill.display_name})"

    def damage(self, actual_critical_strike, actual_damage, parser):
        dot_skill_id, dot_skill_level = parser.current_dot_skills[self.buff_id]
        buff_stack = min(self.max_stack, parser.current_dot_stacks[self.buff_id])
        damage_tuple = ((self.buff_id, self.buff_level, buff_stack), (dot_skill_id, dot_skill_level), tuple())
        status_tuple = parser.dot_status
        parser.current_dot_ticks[self.buff_id] -= 1
        parser.current_last_dot[self.buff_id] = (damage_tuple, status_tuple)
        parser.current_records[damage_tuple][status_tuple].append(
            (parser.current_frame - parser.start_frame, actual_critical_strike, actual_damage)
        )

    def parse(self, actual_critical_strike, actual_damage, parser):
        self.damage(actual_critical_strike, actual_damage, parser)

    @property
    def physical_attack_power_cof(self):
        if not self.bind_skill.platform:
            return PHYSICAL_DOT_ATTACK_POWER_COF(self.bind_skill.channel_interval, self.interval, self.origin_tick)
        else:
            return PHYSICAL_DOT_ATTACK_POWER_COF(self.bind_skill.dot_cof, self.interval, self.origin_tick)

    @property
    def magical_attack_power_cof(self):
        if not self.bind_skill.platform:
            return MAGICAL_DOT_ATTACK_POWER_COF(self.bind_skill.channel_interval, self.interval, self.origin_tick)
        else:
            return MAGICAL_DOT_ATTACK_POWER_COF(self.bind_skill.dot_cof, self.interval, self.origin_tick)

    def call_physical_damage(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, 0, 0,
            self.physical_attack_power_cof, attribute.physical_attack_power,
            0, 0, 0, 0, attribute.global_damage_factor, self.buff_stack
        )
        if damage:
            return self.bind_skill.physical_damage_chain(damage, attribute)
        return 0, 0

    def call_solar_damage(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, 0, 0,
            self.magical_attack_power_cof, attribute.solar_attack_power,
            0, 0, 0, 0, attribute.global_damage_factor, self.buff_stack
        )
        if damage:
            return self.bind_skill.solar_damage_chain(damage, attribute)
        return 0, 0

    def call_lunar_damage(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, 0, 0,
            self.magical_attack_power_cof, attribute.lunar_attack_power,
            0, 0, 0, 0, attribute.global_damage_factor, self.buff_stack
        )
        if damage:
            return self.bind_skill.lunar_damage_chain(damage, attribute)
        return 0, 0

    def call_neutral_damage(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, 0, 0,
            self.magical_attack_power_cof, attribute.neutral_attack_power,
            0, 0, 0, 0, attribute.global_damage_factor, self.buff_stack
        )
        if damage:
            return self.bind_skill.neutral_damage_chain(damage, attribute)
        return 0, 0

    def call_poison_damage(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, 0, 0,
            self.magical_attack_power_cof, attribute.poison_attack_power,
            0, 0, 0, 0, attribute.global_damage_factor, self.buff_stack
        )
        if damage:
            return self.bind_skill.poison_damage_chain(damage, attribute)
        return 0, 0

    def pre_damage(self, attribute: Attribute):
        if self.consume_skill:
            attribute.global_damage_factor *= self.consume_skill.global_damage_factor
        self.bind_skill.pre_damage(attribute)
        attribute.all_damage_addition -= self.bind_skill.damage_addition

    def post_damage(self, attribute: Attribute):
        if self.consume_skill:
            attribute.global_damage_factor /= self.consume_skill.global_damage_factor
        self.bind_skill.post_damage(attribute)
        attribute.all_damage_addition += self.bind_skill.damage_addition

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

        critical_strike = min(self.bind_skill.critical_strike(attribute), 1)
        expected_damage = total_damage * (1 - critical_strike) + total_critical_damage * critical_strike
        self.post_damage(attribute)
        return int(total_damage), int(total_critical_damage), critical_strike, expected_damage
