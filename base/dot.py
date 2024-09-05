from dataclasses import dataclass
from typing import List

from assets.dots import DOTS
from base.attribute import Attribute
from base.buff import BaseBuff
from base.constant import PHYSICAL_DOT_ATTACK_POWER_COF, MAGICAL_DOT_ATTACK_POWER_COF
from base.skill import Skill
from utils.damage import init_result


class BaseDot(BaseBuff):
    dot_skill: Skill = None
    consume_skill: Skill = None

    dot_stack: int = 1
    consume_tick: int = 1

    physical_damage_call: int = 0
    solar_damage_call: int = 0
    lunar_damage_call: int = 0
    neutral_damage_call: int = 0
    poison_damage_call: int = 0

    _damage_base: List[int] = 0
    _interval: List[int] = []
    interval_add: int = 0
    _tick: List[int] = []
    tick_add: int = 0

    def set_asset(self, attrs):
        for attr, value in DOTS.get(self.buff_id, {}).items():
            setattr(self, attr, value)
        for attr, value in attrs.items():
            setattr(self, attr, value)

    @property
    def buff_stack(self):
        return self.dot_stack * self.consume_tick

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
            return self._interval[-1] + self.interval_add
        else:
            return self._interval[self.buff_level - 1] + self.interval_add

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
            return self._tick[-1] + self.tick_add
        else:
            return self._tick[self.buff_level - 1] + self.tick_add

    @tick.setter
    def tick(self, tick):
        if isinstance(tick, list):
            self._tick = tick
        else:
            self._tick = [tick]

    @property
    def origin_tick(self):
        return self.tick - self.tick_add


@dataclass
class Dot(BaseDot):
    buff_id: int

    activate: bool = True

    @property
    def display_name(self):
        if not self.dot_skill:
            return super().display_name
        if not self.consume_skill:
            return f"{super().display_name}({self.dot_skill.display_name})"
        else:
            return f"{super().display_name}({self.dot_skill.display_name}|{self.consume_skill.display_name})"

    def damage(self, actual_critical_strike, actual_damage, parser):
        dot_skill_id, dot_skill_level = parser.current_dot_skills[self.buff_id]
        dot_stack = min(self.max_stack, parser.current_dot_stacks[self.buff_id])
        damage_tuple = ((self.buff_id, self.buff_level), (dot_skill_id, dot_skill_level, dot_stack), tuple())
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
        if not self.dot_skill.platform:
            dot_cof = PHYSICAL_DOT_ATTACK_POWER_COF(self.dot_skill.channel_interval, self.interval, self.origin_tick)
        else:
            dot_cof = PHYSICAL_DOT_ATTACK_POWER_COF(self.dot_skill.dot_cof, self.interval, self.origin_tick)
        if self.consume_skill:
            return dot_cof * self.consume_skill.global_damage_factor
        else:
            return dot_cof

    @property
    def magical_attack_power_cof(self):
        if not self.dot_skill.platform:
            dot_cof = MAGICAL_DOT_ATTACK_POWER_COF(self.dot_skill.channel_interval, self.interval, self.origin_tick)
        else:
            dot_cof = MAGICAL_DOT_ATTACK_POWER_COF(self.dot_skill.dot_cof, self.interval, self.origin_tick)
        if self.consume_skill:
            return dot_cof * self.consume_skill.global_damage_factor
        else:
            return dot_cof

    def call_physical_damage(self, attribute: Attribute):
        damage = init_result(
            damage_base=self.damage_base, multi_stack=self.buff_stack,
            attack_power_cof=self.physical_attack_power_cof, attack_power=attribute.physical_attack_power
        )
        if damage:
            return self.dot_skill.physical_damage_chain(damage, attribute)
        return 0, 0

    def call_solar_damage(self, attribute: Attribute):
        damage = init_result(
            damage_base=self.damage_base, multi_stack=self.buff_stack,
            attack_power_cof=self.magical_attack_power_cof, attack_power=attribute.solar_attack_power
        )
        if damage:
            return self.dot_skill.solar_damage_chain(damage, attribute)
        return 0, 0

    def call_lunar_damage(self, attribute: Attribute):
        damage = init_result(
            damage_base=self.damage_base, multi_stack=self.buff_stack,
            attack_power_cof=self.magical_attack_power_cof, attack_power=attribute.lunar_attack_power
        )
        if damage:
            return self.dot_skill.lunar_damage_chain(damage, attribute)
        return 0, 0

    def call_neutral_damage(self, attribute: Attribute):
        damage = init_result(
            damage_base=self.damage_base, multi_stack=self.buff_stack,
            attack_power_cof=self.magical_attack_power_cof, attack_power=attribute.neutral_attack_power
        )
        if damage:
            return self.dot_skill.neutral_damage_chain(damage, attribute)
        return 0, 0

    def call_poison_damage(self, attribute: Attribute):
        damage = init_result(
            damage_base=self.damage_base, multi_stack=self.buff_stack,
            attack_power_cof=self.magical_attack_power_cof, attack_power=attribute.poison_attack_power
        )
        if damage:
            return self.dot_skill.poison_damage_chain(damage, attribute)
        return 0, 0

    def pre_damage(self, attribute: Attribute):
        self.dot_skill.pre_damage(attribute)
        attribute.all_damage_addition -= self.dot_skill.damage_addition

    def post_damage(self, attribute: Attribute):
        self.dot_skill.post_damage(attribute)
        attribute.all_damage_addition += self.dot_skill.damage_addition

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

        critical_strike = min(self.dot_skill.critical_strike(attribute), 1)
        expected_damage = total_damage * (1 - critical_strike) + total_critical_damage * critical_strike
        self.post_damage(attribute)
        return int(total_damage), int(total_critical_damage), critical_strike, expected_damage
