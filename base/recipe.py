from typing import List

from base.gain import Gain


class Recipe(Gain):
    def __init__(self, gain_name: str, skill_ids: List[int], value: int):
        super().__init__(gain_name)
        self.skill_ids = skill_ids
        self.value = value


class DamageAdditionRecipe(Recipe):
    def add(self, other):
        if isinstance(other, dict):
            for skill_id in self.skill_ids:
                other[skill_id].skill_damage_addition += self.value

    def sub(self, other):
        if isinstance(other, dict):
            for skill_id in self.skill_ids:
                other[skill_id].skill_damage_addition -= self.value


class CriticalStrikeRecipe(Recipe):
    def add(self, other):
        if isinstance(other, dict):
            for skill_id in self.skill_ids:
                other[skill_id].skill_critical_strike += self.value

    def sub(self, other):
        if isinstance(other, dict):
            for skill_id in self.skill_ids:
                other[skill_id].skill_critical_strike -= self.value


def damage_addition_recipe(skill_ids, value, name="伤害增加"):
    return DamageAdditionRecipe(name, skill_ids, value)


def critical_strike_recipe(skill_ids, value, name="会心增加"):
    return CriticalStrikeRecipe(name, skill_ids, value)
