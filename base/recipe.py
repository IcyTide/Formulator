from dataclasses import dataclass
from typing import Dict, Union

from assets.recipes import RECIPES
from base.attribute import Attribute
from base.buff import Buff
from base.dot import Dot
from base.skill import Skill


@dataclass
class Recipe:
    recipe_id: int
    recipe_level: int
    recipe_name: str = ""

    def __post_init__(self):
        if not self.recipe_name:
            self.recipe_name = type(self).__name__

    def set_asset(self, attrs):
        for attr, value in RECIPES.get(self.recipe_id, {}).get(self.recipe_level, {}).items():
            setattr(self, attr, value)
        for attr, value in attrs.items():
            setattr(self, attr, value)

    def add_attribute(self, attribute: Attribute):
        pass

    def add_buffs(self, buffs: Dict[int, Buff]):
        pass

    def add_dots(self, dots: Dict[int, Dot]):
        pass

    def add_skills(self, skills: Dict[int, Skill]):
        pass

    def add(self, attribute: Attribute, buffs: Dict[int, Buff], dots: Dict[int, Dot], skills: Dict[int, Skill]):
        self.add_attribute(attribute)
        self.add_buffs(buffs)
        self.add_dots(dots)
        return self.add_skills(skills)

    def sub_attribute(self, attribute: Attribute):
        pass

    def sub_skills(self, skills: Dict[int, Skill]):
        pass

    def sub_buffs(self, buffs: Dict[int, Buff]):
        pass

    def sub_dots(self, dots: Dict[int, Dot]):
        pass

    def sub(self, attribute: Attribute, buffs: Dict[int, Buff], dots: Dict[int, Dot], skills: Dict[int, Skill]):
        self.sub_attribute(attribute)
        self.sub_buffs(buffs)
        self.sub_dots(dots)
        self.sub_skills(skills)


class SkillRecipe(Recipe):
    skill_id = None
    recipe_type = None
    recipe_mask = 0

    clone_id = None

    damage_addition: int = 0
    prepare_frame: int = 0
    value: Union[int, float, tuple] = 0

    def check_skill(self, skill: Skill):
        if skill.skill_id == self.skill_id or skill.skill_id == self.clone_id:
            return True
        if skill.recipe_type == self.recipe_type or skill.recipe_type == self.clone_id:
            return True
        if skill.recipe_mask & self.recipe_mask:
            return True
        return False

    def _add_skill(self, skill: Skill):
        skill.damage_addition_add += self.damage_addition
        skill.prepare_frame_add += self.prepare_frame

    def add_skill(self, skill: Skill):
        pass

    def add_skills(self, skills: Dict[int, Skill]):
        return_tag = False
        for skill in skills.values():
            if self.check_skill(skill):
                self._add_skill(skill)
                self.add_skill(skill)
                return_tag = True
        return return_tag

    def _sub_skill(self, skill: Skill):
        skill.damage_addition_add -= self.damage_addition
        skill.prepare_frame_add -= self.prepare_frame

    def sub_skill(self, skill: Skill):
        pass

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if self.check_skill(skill):
                self._sub_skill(skill)
                self.sub_skill(skill)


class DotRecipe(Recipe):
    buff_id: int = None
    clone_id: int = None

    interval: int = 0
    tick: int = 0

    def check_dot(self, dot: Dot):
        if dot.buff_id == self.buff_id or dot.buff_id == self.clone_id:
            return True
        return False

    def add_dot(self, dot: Dot):
        dot.interval_add += self.interval
        dot.tick_add += self.interval

    def add_dots(self, dots: Dict[int, Dot]):
        for dot in dots.values():
            if self.check_dot(dot):
                self.add_dot(dot)

    def sub_dot(self, dot: Dot):
        dot.interval_add -= self.interval
        dot.tick_add -= self.interval

    def sub_dots(self, dots: Dict[int, Dot]):
        for dot in dots.values():
            if self.check_dot(dot):
                self.sub_dot(dot)


class CriticalStrikeRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.physical_critical_strike_rate_add += self.value
        skill.solar_critical_strike_rate_add += self.value
        skill.neutral_critical_strike_rate_add += self.value
        skill.lunar_critical_strike_rate_add += self.value
        skill.poison_critical_strike_rate_add += self.value

    def sub_skill(self, skill: Skill):
        skill.physical_critical_strike_rate_add -= self.value
        skill.solar_critical_strike_rate_add -= self.value
        skill.neutral_critical_strike_rate_add -= self.value
        skill.lunar_critical_strike_rate_add -= self.value
        skill.poison_critical_strike_rate_add -= self.value


class CriticalStrikeRecipe_200(CriticalStrikeRecipe):
    value = 200


class CriticalStrikeRecipe_300(CriticalStrikeRecipe):
    value = 300


class CriticalStrikeRecipe_400(CriticalStrikeRecipe):
    value = 400


class CriticalStrikeRecipe_500(CriticalStrikeRecipe):
    value = 500


class CriticalStrikeRecipe_306(CriticalStrikeRecipe):
    value = 306


class ChannelIntervalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.channel_interval_add *= self.value

    def sub_skill(self, skill: Skill):
        skill.channel_interval_add /= self.value


class DamageAdditionRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.damage_addition += self.value

    def sub_skill(self, skill: Skill):
        skill.damage_addition -= self.value


class MoveStateDamageAdditionRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.move_state_damage_addition += self.value

    def sub_skill(self, skill: Skill):
        skill.move_state_damage_addition -= self.value


class PhysicalCriticalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.physical_critical_strike_rate_add += self.value[0]
        skill.physical_critical_power_rate_add += self.value[1]

    def sub_skill(self, skill: Skill):
        skill.physical_critical_strike_rate_add -= self.value[0]
        skill.physical_critical_power_rate_add -= self.value[1]


class SolarAttackPowerGainRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.solar_attack_power_gain_add += self.value

    def sub_skill(self, skill: Skill):
        skill.solar_attack_power_gain_add -= self.value


class LunarAttackPowerGainRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.lunar_attack_power_gain_add += self.value

    def sub_skill(self, skill: Skill):
        skill.lunar_attack_power_gain_add -= self.value


class SolarCriticalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.solar_critical_strike_rate_add += self.value[0]
        skill.solar_critical_power_rate_add += self.value[1]

    def sub_skill(self, skill: Skill):
        skill.solar_critical_strike_rate_add -= self.value[0]
        skill.solar_critical_power_rate_add -= self.value[1]


class LunarCriticalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.lunar_critical_strike_rate_add += self.value[0]
        skill.lunar_critical_power_rate_add += self.value[1]

    def sub_skill(self, skill: Skill):
        skill.lunar_critical_strike_rate_add -= self.value[0]
        skill.lunar_critical_power_rate_add -= self.value[1]


class NeutralCriticalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.neutral_critical_strike_rate_add += self.value[0]
        skill.neutral_critical_power_rate_add += self.value[1]

    def sub_skill(self, skill: Skill):
        skill.neutral_critical_strike_rate_add -= self.value[0]
        skill.neutral_critical_power_rate_add -= self.value[1]


class PoisonCriticalStrikeRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.poison_critical_strike_rate_add += self.value

    def sub_skill(self, skill: Skill):
        skill.poison_critical_strike_rate_add -= self.value


class SolarLunarCriticalStrikeRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.solar_critical_strike_rate_add += self.value
        skill.lunar_critical_strike_rate_add += self.value

    def sub_skill(self, skill: Skill):
        skill.solar_critical_strike_rate_add -= self.value
        skill.lunar_critical_strike_rate_add -= self.value


class SolarLunarCriticalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.solar_critical_strike_rate_add += self.value[0]
        skill.lunar_critical_strike_rate_add += self.value[0]
        skill.solar_critical_power_rate_add += self.value[1]
        skill.lunar_critical_power_rate_add += self.value[1]

    def sub_skill(self, skill: Skill):
        skill.solar_critical_strike_rate_add -= self.value[0]
        skill.lunar_critical_strike_rate_add -= self.value[0]
        skill.solar_critical_power_rate_add -= self.value[1]
        skill.lunar_critical_power_rate_add -= self.value[1]


class PhysicalShieldGainRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.physical_shield_gain_add += self.value

    def sub_skill(self, skill: Skill):
        skill.physical_shield_gain_add -= self.value


class MagicalShieldGainRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.solar_shield_gain_add += self.value
        skill.lunar_shield_gain_add += self.value
        skill.neutral_shield_gain_add += self.value
        skill.poison_shield_gain_add += self.value

    def sub_skill(self, skill: Skill):
        skill.solar_shield_gain_add -= self.value
        skill.lunar_shield_gain_add -= self.value
        skill.neutral_shield_gain_add -= self.value
        skill.poison_shield_gain_add -= self.value


class PveAdditionRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        skill.pve_addition_add += self.value

    def sub_skill(self, skill: Skill):
        skill.pve_addition_add -= self.value
