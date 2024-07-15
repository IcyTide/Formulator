from typing import Dict

from base.dot import Dot
from base.gain import Gain
from base.skill import Skill


class PrepareFrameRecipe(Gain):
    def add_skill(self, skill: Skill):
        skill.prepare_frame_extra += self.value

    def sub_skill(self, skill: Skill):
        skill.prepare_frame_extra -= self.value


class ChannelIntervalRecipe(Gain):
    def add_skill(self, skill: Skill):
        skill.channel_interval_extra *= self.value

    def sub_skill(self, skill: Skill):
        skill.channel_interval_extra /= self.value


class DamageAdditionRecipe(Gain):
    def add_skill(self, skill: Skill):
        skill.damage_addition_extra += self.value

    def sub_skill(self, skill: Skill):
        skill.damage_addition_extra -= self.value


class MoveStateDamageAdditionRecipe(Gain):
    def add_skill(self, skill: Skill):
        skill.move_state_damage_addition += self.value

    def sub_skill(self, skill: Skill):
        skill.move_state_damage_addition -= self.value


class CriticalStrikeRecipe(Gain):
    def add_skill(self, skill: Skill):
        skill.physical_critical_strike_rate_extra += self.value
        skill.solar_critical_strike_rate_extra += self.value
        skill.lunar_critical_strike_rate_extra += self.value
        skill.neutral_critical_strike_rate_extra += self.value
        skill.poison_critical_strike_rate_extra += self.value

    def sub_skill(self, skill: Skill):
        skill.physical_critical_strike_rate_extra -= self.value
        skill.solar_critical_strike_rate_extra -= self.value
        skill.lunar_critical_strike_rate_extra -= self.value
        skill.neutral_critical_strike_rate_extra -= self.value
        skill.poison_critical_strike_rate_extra -= self.value


class PhysicalCriticalRecipe(Gain):
    def add_skill(self, skill: Skill):
        skill.physical_critical_strike_rate_extra += self.value[0]
        skill.physical_critical_power_rate_extra += self.value[1]

    def sub_skill(self, skill: Skill):
        skill.physical_critical_strike_rate_extra -= self.value[0]
        skill.physical_critical_power_rate_extra -= self.value[1]


class MagicalCriticalRecipe(Gain):
    def add_skill(self, skill: Skill):
        skill.solar_critical_strike_rate_extra += self.value[0]
        skill.lunar_critical_strike_rate_extra += self.value[0]
        skill.neutral_critical_strike_rate_extra += self.value[0]
        skill.poison_critical_strike_rate_extra += self.value[0]
        skill.solar_critical_power_rate_extra += self.value[1]
        skill.lunar_critical_power_rate_extra += self.value[1]
        skill.neutral_critical_power_rate_extra += self.value[1]
        skill.poison_critical_power_rate_extra += self.value[1]

    def sub_skill(self, skill: Skill):
        skill.solar_critical_strike_rate_extra -= self.value[0]
        skill.lunar_critical_strike_rate_extra -= self.value[0]
        skill.neutral_critical_strike_rate_extra -= self.value[0]
        skill.poison_critical_strike_rate_extra -= self.value[0]
        skill.solar_critical_power_rate_extra -= self.value[1]
        skill.lunar_critical_power_rate_extra -= self.value[1]
        skill.neutral_critical_power_rate_extra -= self.value[1]
        skill.poison_critical_power_rate_extra -= self.value[1]


class PhysicalShieldGainRecipe(Gain):
    def add_skill(self, skill: Skill):
        skill.physical_shield_gain_extra += self.value

    def sub_skill(self, skill: Skill):
        skill.physical_shield_gain_extra -= self.value


class MagicalShieldGainRecipe(Gain):
    def add_skill(self, skill: Skill):
        skill.solar_shield_gain_extra += self.value
        skill.lunar_shield_gain_extra += self.value
        skill.neutral_shield_gain_extra += self.value
        skill.poison_shield_gain_extra += self.value

    def sub_skill(self, skill: Skill):
        skill.solar_shield_gain_extra -= self.value
        skill.lunar_shield_gain_extra -= self.value
        skill.neutral_shield_gain_extra -= self.value
        skill.poison_shield_gain_extra -= self.value


class PveAdditionRecipe(Gain):
    def add_skill(self, skill: Skill):
        skill.pve_addition_extra += self.value

    def sub_skill(self, skill: Skill):
        skill.pve_addition_extra -= self.value


class ExtraTickRecipe(Gain):
    def add_dots(self, dots: Dict[int, Dot]):
        dots[self.skill_id].tick_extra += self.value

    def sub_dots(self, dots: Dict[int, Dot]):
        dots[self.skill_id].tick_extra -= self.value
