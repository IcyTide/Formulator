from base.recipe import SkillRecipe
from base.skill import Skill
from general.recipes import equipment
from general.recipes import school

GENERAL_RECIPES = {
    **equipment.RECIPES,
    **school.RECIPES
}


class CriticalStrikeRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.physical_critical_strike_rate_add += self.value
        skill.solar_critical_strike_rate_add += self.value
        skill.neutral_critical_strike_rate_add += self.value
        skill.lunar_critical_strike_rate_add += self.value
        skill.poison_critical_strike_rate_add += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
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
        super().add_skill(skill)
        skill.channel_interval_add *= self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.channel_interval_add /= self.value


class MoveStateDamageAdditionRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.move_state_damage_addition += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.move_state_damage_addition -= self.value


class PhysicalCriticalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.physical_critical_strike_rate_add += self.value[0]
        skill.physical_critical_power_rate_add += self.value[1]

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.physical_critical_strike_rate_add -= self.value[0]
        skill.physical_critical_power_rate_add -= self.value[1]


class SolarAttackPowerGainRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.solar_attack_power_gain_add += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.solar_attack_power_gain_add -= self.value


class LunarAttackPowerGainRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.lunar_attack_power_gain_add += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.lunar_attack_power_gain_add -= self.value


class SolarCriticalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.solar_critical_strike_rate_add += self.value[0]
        skill.solar_critical_power_rate_add += self.value[1]

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.solar_critical_strike_rate_add -= self.value[0]
        skill.solar_critical_power_rate_add -= self.value[1]


class LunarCriticalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.lunar_critical_strike_rate_add += self.value[0]
        skill.lunar_critical_power_rate_add += self.value[1]

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.lunar_critical_strike_rate_add -= self.value[0]
        skill.lunar_critical_power_rate_add -= self.value[1]


class NeutralCriticalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.neutral_critical_strike_rate_add += self.value[0]
        skill.neutral_critical_power_rate_add += self.value[1]

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.neutral_critical_strike_rate_add -= self.value[0]
        skill.neutral_critical_power_rate_add -= self.value[1]


class PoisonCriticalStrikeRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.poison_critical_strike_rate_add += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.poison_critical_strike_rate_add -= self.value


class SolarLunarCriticalStrikeRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.solar_critical_strike_rate_add += self.value
        skill.lunar_critical_strike_rate_add += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.solar_critical_strike_rate_add -= self.value
        skill.lunar_critical_strike_rate_add -= self.value


class SolarLunarCriticalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.solar_critical_strike_rate_add += self.value[0]
        skill.lunar_critical_strike_rate_add += self.value[0]
        skill.solar_critical_power_rate_add += self.value[1]
        skill.lunar_critical_power_rate_add += self.value[1]

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.solar_critical_strike_rate_add -= self.value[0]
        skill.lunar_critical_strike_rate_add -= self.value[0]
        skill.solar_critical_power_rate_add -= self.value[1]
        skill.lunar_critical_power_rate_add -= self.value[1]


class PhysicalShieldGainRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.physical_shield_gain_add += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.physical_shield_gain_add -= self.value


class MagicalShieldGainRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.solar_shield_gain_add += self.value
        skill.lunar_shield_gain_add += self.value
        skill.neutral_shield_gain_add += self.value
        skill.poison_shield_gain_add += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.solar_shield_gain_add -= self.value
        skill.lunar_shield_gain_add -= self.value
        skill.neutral_shield_gain_add -= self.value
        skill.poison_shield_gain_add -= self.value


class PveAdditionRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.pve_addition_add += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.pve_addition_add -= self.value
