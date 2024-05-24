from typing import List, Dict

from base.gain import Gain
from base.skill import Skill


class RecipeGain(Gain):
    def __init__(self, gain_name: str, skill_ids: List[int], value: int):
        super().__init__(gain_name)
        self.skill_ids = skill_ids
        self.value = value


class DoubleRecipeGain(Gain):
    def __init__(self, gain_name, attack_skill_ids, damage_skill_ids, attack_value, damage_value):
        super().__init__(gain_name)
        self.attack_skill_ids = attack_skill_ids
        self.damage_skill_ids = damage_skill_ids
        self.attack_value = attack_value
        self.damage_value = damage_value


class IntervalRecipe(RecipeGain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].interval += self.value

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].interval -= self.value


class AttackPowerRecipe(RecipeGain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].attack_power_cof_gain *= self.value

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].attack_power_cof_gain /= self.value


class DamageAdditionRecipe(RecipeGain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].skill_damage_addition += self.value

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].skill_damage_addition -= self.value


class DoubleAdditionRecipe(DoubleRecipeGain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.attack_skill_ids:
            skills[skill_id].attack_power_cof_gain *= self.attack_value
        for skill_id in self.damage_skill_ids:
            skills[skill_id].skill_damage_addition += self.damage_value

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.attack_skill_ids:
            skills[skill_id].attack_power_cof_gain /= self.attack_value
        for skill_id in self.damage_skill_ids:
            skills[skill_id].skill_damage_addition /= self.damage_value


class CriticalStrikeRecipe(RecipeGain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].skill_critical_strike += self.value

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].skill_critical_strike -= self.value


class PveAdditionRecipe(RecipeGain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].skill_pve_addition += self.value

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].skill_pve_addition -= self.value


class ShieldGainRecipe(RecipeGain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].skill_shield_gain += self.value

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].skill_shield_gain -= self.value


def interval_recipe(skill_ids, value, name="减少运功时间"):
    return IntervalRecipe(name, skill_ids, value)


def attack_power_recipe(skill_ids, value, name="系数增加"):
    return AttackPowerRecipe(name, skill_ids, value)


def damage_addition_recipe(skill_ids, value, name="伤害增加"):
    return DamageAdditionRecipe(name, skill_ids, value)


def critical_strike_recipe(skill_ids, value, name="会心增加"):
    return CriticalStrikeRecipe(name, skill_ids, value)


def pve_addition_recipe(skill_ids, value, name="非侠伤害增加"):
    return PveAdditionRecipe(name, skill_ids, value)


def shield_gain_recipe(skill_ids, value, name="无视防御"):
    return ShieldGainRecipe(name, skill_ids, value)


def double_addition_recipe(
        attack_power_skill_ids, damage_addition_skill_ids, attack_power_value, damage_addition_value, name="伤害增加"
):
    return DoubleAdditionRecipe(
        name, attack_power_skill_ids, damage_addition_skill_ids, attack_power_value, damage_addition_value
    )
