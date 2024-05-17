from base.attribute import Attribute
from base.constant import *
from utils.damage import *

from typing import List, Union
from dataclasses import dataclass


class BaseSkill:
    _skill_name: Union[List[str], str] = ""
    skill_level: int = 0
    skill_stack: int = 1

    _damage_base: Union[List[int], int] = 0
    _damage_rand: Union[List[int], int] = 0

    _attack_power_cof: Union[List[float], float] = 0.
    _surplus_cof: Union[List[float], float] = 0.
    _weapon_damage_cof: Union[List[float], float] = 0.

    damage_gain: float = 1.
    attack_power_cof_gain: float = 1.
    surplus_cof_gain: float = 1.
    weapon_damage_cof_gain: float = 1.

    global_damage_factor: float = 1.

    skill_damage_addition: int = 0
    extra_damage_addition: int = 0
    _skill_pve_addition: Union[List[int], int] = 0
    _skill_shield_gain: Union[List[int], int] = 0
    skill_critical_strike: int = 0
    skill_critical_power: int = 0

    @property
    def skill_name(self):
        if not isinstance(self._skill_name, list):
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

    @property
    def damage_base(self):
        if not isinstance(self._damage_base, list):
            return 0

        if self.skill_level > len(self._damage_base):
            damage_base = self._damage_base[-1]
        else:
            damage_base = self._damage_base[self.skill_level - 1]
        return damage_base * self.damage_gain

    @damage_base.setter
    def damage_base(self, damage_base):
        if isinstance(damage_base, list):
            self._damage_base = damage_base
        else:
            self._damage_base = [damage_base]

    @property
    def damage_rand(self):
        if not isinstance(self._damage_rand, list):
            return 0

        if self.skill_level > len(self._damage_rand):
            damage_rand = self._damage_rand[-1]
        else:
            damage_rand = self._damage_rand[self.skill_level - 1]
        return damage_rand * self.damage_gain

    @damage_rand.setter
    def damage_rand(self, damage_rand):
        if isinstance(damage_rand, list):
            self._damage_rand = damage_rand
        else:
            self._damage_rand = [damage_rand]

    @property
    def attack_power_cof(self):
        if not isinstance(self._attack_power_cof, list):
            return 0

        if self.skill_level > len(self._attack_power_cof):
            attack_power_cof = self._attack_power_cof[-1]
        else:
            attack_power_cof = self._attack_power_cof[self.skill_level - 1]
        return attack_power_cof * self.attack_power_cof_gain

    @attack_power_cof.setter
    def attack_power_cof(self, attack_power_cof):
        if isinstance(attack_power_cof, list):
            self._attack_power_cof = attack_power_cof
        else:
            self._attack_power_cof = [attack_power_cof]

    @property
    def surplus_cof(self):
        if not isinstance(self._surplus_cof, list):
            return 0

        if self.skill_level > len(self._surplus_cof):
            surplus_cof = self._surplus_cof[-1]
        else:
            surplus_cof = self._surplus_cof[self.skill_level - 1]
        return SURPLUS_COF(surplus_cof * self.surplus_cof_gain)

    @surplus_cof.setter
    def surplus_cof(self, surplus_cof):
        if isinstance(surplus_cof, list):
            self._surplus_cof = surplus_cof
        else:
            self._surplus_cof = [surplus_cof]

    @property
    def weapon_damage_cof(self):
        if not isinstance(self._weapon_damage_cof, list):
            return 0

        if self.skill_level > len(self._weapon_damage_cof):
            weapon_damage_cof = self._weapon_damage_cof[-1]
        else:
            weapon_damage_cof = self._weapon_damage_cof[self.skill_level - 1]
        return WEAPON_DAMAGE_COF(weapon_damage_cof * self.weapon_damage_cof_gain)

    @weapon_damage_cof.setter
    def weapon_damage_cof(self, weapon_damage_cof):
        if isinstance(weapon_damage_cof, list):
            self._weapon_damage_cof = weapon_damage_cof
        else:
            self._weapon_damage_cof = [weapon_damage_cof]

    @property
    def skill_shield_gain(self):
        if not isinstance(self._skill_shield_gain, list):
            return 0

        if self.skill_level > len(self._skill_shield_gain):
            return self._skill_shield_gain[-1]
        else:
            return self._skill_shield_gain[self.skill_level - 1]

    @skill_shield_gain.setter
    def skill_shield_gain(self, skill_shield_gain):
        if isinstance(skill_shield_gain, list):
            self._skill_shield_gain = skill_shield_gain
        else:
            self._skill_shield_gain = [skill_shield_gain]

    @property
    def skill_pve_addition(self):
        if not isinstance(self._skill_pve_addition, list):
            return 0

        if self.skill_level > len(self._skill_pve_addition):
            return self._skill_pve_addition[-1]
        else:
            return self._skill_pve_addition[self.skill_level - 1]

    @skill_pve_addition.setter
    def skill_pve_addition(self, skill_pve_addition):
        if isinstance(skill_pve_addition, list):
            self._skill_pve_addition = skill_pve_addition
        else:
            self._skill_pve_addition = [skill_pve_addition]


@dataclass
class Skill(BaseSkill):
    skill_id: int

    activate: bool = True

    interval: int = 0
    bind_skill: int = 0
    tick: int = 1
    max_stack: int = 1
    last_dot: bool = True

    pre_effects: list = None
    pre_buffs: dict = None
    pre_target_buffs: dict = None
    post_effects: list = None
    post_buffs: dict = None
    post_target_buffs: dict = None

    def __post_init__(self):
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

    def record(self, parser):
        pass

    def post_record(self, parser):
        for (buff_id, buff_level), buff_stack in self.post_buffs.items():
            buff_level = buff_level if buff_level else self.skill_level
            parser.refresh_buff(buff_id, buff_level, buff_stack)
        for (buff_id, buff_level), buff_stack in self.post_target_buffs.items():
            buff_level = buff_level if buff_level else self.skill_level
            parser.refresh_target_buff(buff_id, buff_level, buff_stack)
        for effect in self.post_effects:
            effect(parser)

    def parse(self, parser):
        self.pre_record(parser)
        self.record(parser)
        self.post_record(parser)

    def __call__(self, attribute: Attribute):
        return 0, 0, 0., 0


class DotSkill(Skill):
    def record(self, parser):
        super().record(parser)
        bind_skill = parser.current_school.skills[self.bind_skill]
        if not parser.current_dot_ticks[self.bind_skill]:
            parser.current_dot_stacks[self.bind_skill] = 0
        parser.current_dot_ticks[self.bind_skill] = bind_skill.tick
        parser.current_dot_stacks[self.bind_skill] = min(
            parser.current_dot_stacks.get(self.bind_skill, 0) + 1, bind_skill.max_stack
        )
        parser.current_dot_buffs[self.bind_skill] = parser.current_index


class DotConsumeSkill(Skill):
    def consume_next(self, parser):
        tick = min(parser.current_dot_ticks[self.bind_skill], self.tick)
        parser.current_next_dot[self.bind_skill] = tick

    def consume_last(self, parser):
        if not (last_dot_index := parser.current_last_dot.pop(self.bind_skill, None)):
            return
        parser.current_dot_ticks[self.bind_skill] += 1
        tick = min(parser.current_dot_ticks[self.bind_skill], self.tick)
        parser.records.current_records[last_dot_index]['skill_stack'] *= tick
        parser.current_dot_ticks[self.bind_skill] -= tick

    def record(self, parser):
        super().record(parser)
        if self.last_dot:
            self.consume_last(parser)
        else:
            self.consume_next(parser)


class Damage(Skill):
    pass


class DotDamage(Damage):
    def record(self, parser):
        super().record(parser)
        parser.current_record['skill_stack'] = parser.current_dot_stacks[self.skill_id]
        parser.current_record['snapshot_index'] = parser.current_dot_buffs[self.skill_id]
        if tick := parser.current_next_dot.pop(self.skill_id, None):
            parser.current_record['skill_stack'] *= tick
            parser.current_dot_ticks[self.skill_id] -= tick
        else:
            parser.current_last_dot[self.skill_id] = parser.current_index
            parser.current_dot_ticks[self.skill_id] -= 1


class NpcDamage(Damage):
    pass


class PetDamage(Damage):
    def __call__(self, attribute: Attribute):
        attack_power = int(attribute.attack_power * 0.87 + attribute.surplus * 59 / 1664)
        damage = init_result(
            self.damage_base, self.damage_rand,
            self.attack_power_cof, attack_power, 0, 0, 0, 0
        ) * self.skill_stack * self.global_damage_factor * attribute.global_damage_factor

        damage = damage_addition_result(
            damage, attribute.damage_addition + self.skill_damage_addition, self.extra_damage_addition
        )
        damage = overcome_result(damage, attribute.overcome,
                                 attribute.level_shield_base + attribute.shield_base,
                                 attribute.shield_gain + self.skill_shield_gain,
                                 0,
                                 attribute.shield_constant)

        critical_power_gain = attribute.critical_power_gain + self.skill_critical_power
        critical_damage = critical_result(damage, attribute.base_critical_power, critical_power_gain)

        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.base_strain, attribute.strain_gain)
        critical_damage = strain_result(critical_damage, attribute.base_strain, attribute.strain_gain)
        damage = pve_addition_result(damage, attribute.pve_addition + self.skill_pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition + self.skill_pve_addition)
        damage = vulnerable_result(damage, attribute.vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.vulnerable)
        critical_strike = min(1, attribute.critical_strike + self.skill_critical_strike / DECIMAL_SCALE)

        expected_damage = critical_strike * critical_damage + (1 - critical_strike) * damage

        return damage, critical_damage, critical_strike, expected_damage


class PureSkill(Skill):
    def __call__(self, attribute: Attribute):
        damage = init_result(self.damage_base, self.damage_rand, 0, 0, 0, 0, 0, 0)

        damage = level_reduction_result(damage, attribute.level_reduction)
        damage = vulnerable_result(damage, attribute.vulnerable)

        return damage, damage, 0, damage


class PhysicalSkill(Skill):
    def __call__(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, self.damage_rand,
            self.attack_power_cof, attribute.physical_attack_power,
            self.weapon_damage_cof, attribute.weapon_damage,
            self.surplus_cof, attribute.surplus
        ) * self.skill_stack * self.global_damage_factor * attribute.global_damage_factor

        damage = damage_addition_result(
            damage, attribute.physical_damage_addition + self.skill_damage_addition, self.extra_damage_addition
        )
        damage = overcome_result(damage, attribute.physical_overcome,
                                 attribute.level_shield_base + attribute.physical_shield_base,
                                 attribute.physical_shield_gain + self.skill_shield_gain,
                                 attribute.physical_shield_ignore,
                                 attribute.shield_constant)

        critical_power_gain = attribute.physical_critical_power_gain + self.skill_critical_power
        critical_damage = critical_result(damage, attribute.base_physical_critical_power, critical_power_gain)

        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.base_strain, attribute.strain_gain)
        critical_damage = strain_result(critical_damage, attribute.base_strain, attribute.strain_gain)
        damage = pve_addition_result(damage, attribute.pve_addition + self.skill_pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition + self.skill_pve_addition)
        damage = vulnerable_result(damage, attribute.physical_vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.physical_vulnerable)
        critical_strike = min(1, attribute.physical_critical_strike + self.skill_critical_strike / DECIMAL_SCALE)

        expected_damage = critical_strike * critical_damage + (1 - critical_strike) * damage

        return damage, critical_damage, critical_strike, expected_damage


class MagicalSkill(Skill):
    def __call__(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, self.damage_rand,
            self.attack_power_cof, attribute.magical_attack_power,
            self.weapon_damage_cof, attribute.weapon_damage,
            self.surplus_cof, attribute.surplus
        ) * self.skill_stack * self.global_damage_factor * attribute.global_damage_factor

        damage = damage_addition_result(
            damage, attribute.magical_damage_addition + self.skill_damage_addition, self.extra_damage_addition
        )
        damage = overcome_result(damage, attribute.magical_overcome,
                                 attribute.level_shield_base + attribute.magical_shield_base,
                                 attribute.magical_shield_gain + self.skill_shield_gain,
                                 attribute.magical_shield_ignore,
                                 attribute.shield_constant)

        critical_power_gain = attribute.magical_critical_power_gain + self.skill_critical_power
        critical_damage = critical_result(damage, attribute.base_magical_critical_power, critical_power_gain)

        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.base_strain, attribute.strain_gain)
        critical_damage = strain_result(critical_damage, attribute.base_strain, attribute.strain_gain)
        damage = pve_addition_result(damage, attribute.pve_addition + self.skill_pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition + self.skill_pve_addition)
        damage = vulnerable_result(damage, attribute.magical_vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.magical_vulnerable)
        critical_strike = min(1, attribute.magical_critical_strike + self.skill_critical_strike / DECIMAL_SCALE)

        expected_damage = critical_strike * critical_damage + (1 - critical_strike) * damage

        return damage, critical_damage, critical_strike, expected_damage


class AdaptiveSkill(Skill):
    def __call__(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, self.damage_rand,
            self.attack_power_cof, attribute.attack_power,
            self.weapon_damage_cof, attribute.weapon_damage,
            self.surplus_cof, attribute.surplus
        ) * self.skill_stack * self.global_damage_factor * attribute.global_damage_factor

        damage = damage_addition_result(
            damage, attribute.damage_addition + self.skill_damage_addition, self.extra_damage_addition
        )
        damage = overcome_result(damage, attribute.overcome,
                                 attribute.level_shield_base + attribute.shield_base,
                                 attribute.shield_gain + self.skill_shield_gain,
                                 attribute.shield_ignore,
                                 attribute.shield_constant)

        critical_power_gain = attribute.critical_power_gain + self.skill_critical_power
        critical_damage = critical_result(damage, attribute.base_critical_power, critical_power_gain)

        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.base_strain, attribute.strain_gain)
        critical_damage = strain_result(critical_damage, attribute.base_strain, attribute.strain_gain)
        damage = pve_addition_result(damage, attribute.pve_addition + self.skill_pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition + self.skill_pve_addition)
        damage = vulnerable_result(damage, attribute.vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.vulnerable)
        critical_strike = min(1, attribute.critical_strike + self.skill_critical_strike / DECIMAL_SCALE)

        expected_damage = critical_strike * critical_damage + (1 - critical_strike) * damage

        return damage, critical_damage, critical_strike, expected_damage


class PureDamage(PureSkill, Damage):
    pass


class PhysicalDamage(PhysicalSkill, Damage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return PHYSICAL_ATTACK_POWER_COF(super().attack_power_cof + self.interval)


class MagicalDamage(MagicalSkill, Damage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return MAGICAL_ATTACK_POWER_COF(super().attack_power_cof + self.interval)


class MixingDamage(AdaptiveSkill, Damage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return MAGICAL_ATTACK_POWER_COF(super().attack_power_cof + self.interval)


class PhysicalDotDamage(PhysicalSkill, DotDamage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return PHYSICAL_DOT_ATTACK_POWER_COF(super().attack_power_cof, self.interval)


class MagicalDotDamage(MagicalSkill, DotDamage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return MAGICAL_DOT_ATTACK_POWER_COF(super().attack_power_cof, self.interval)


class MixingDotDamage(AdaptiveSkill, DotDamage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return MAGICAL_DOT_ATTACK_POWER_COF(super().attack_power_cof, self.interval)


class PhysicalNpcDamage(PhysicalSkill, NpcDamage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return PHYSICAL_ATTACK_POWER_COF(super().attack_power_cof + self.interval)


class MagicalNpcDamage(MagicalSkill, NpcDamage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return MAGICAL_ATTACK_POWER_COF(super().attack_power_cof + self.interval)


class MagicalPetDamage(MagicalSkill, PetDamage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return MAGICAL_ATTACK_POWER_COF(super().attack_power_cof + self.interval)
