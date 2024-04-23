from typing import List, Dict

from base.gain import Gain
from base.skill import Skill


class RecipeGain(Gain):
    def __init__(self, gain_name: str, skill_ids: List[int], value: int):
        super().__init__(gain_name)
        self.skill_ids = skill_ids
        self.value = value


class DamageAdditionRecipe(RecipeGain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].skill_damage_addition += self.value

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].skill_damage_addition -= self.value


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


def damage_addition_recipe(skill_ids, value, name="伤害增加"):
    return DamageAdditionRecipe(name, skill_ids, value)


def critical_strike_recipe(skill_ids, value, name="会心增加"):
    return CriticalStrikeRecipe(name, skill_ids, value)


def pve_addition_recipe(skill_ids, value, name="非侠伤害增加"):
    return PveAdditionRecipe(name, skill_ids, value)
