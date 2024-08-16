from base.recipe import SkillRecipe
from base.skill import Skill
from general.recipes import equipment

GENERAL_RECIPES = {
    **equipment.RECIPES
}


class CriticalStrikeRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.physical_critical_strike_rate_extra += self.value
        skill.solar_critical_strike_rate_extra += self.value
        skill.neutral_critical_strike_rate_extra += self.value
        skill.lunar_critical_strike_rate_extra += self.value
        skill.poison_critical_strike_rate_extra += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.physical_critical_strike_rate_extra -= self.value
        skill.solar_critical_strike_rate_extra -= self.value
        skill.neutral_critical_strike_rate_extra -= self.value
        skill.lunar_critical_strike_rate_extra -= self.value
        skill.poison_critical_strike_rate_extra -= self.value


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
        skill.channel_interval_extra *= self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.channel_interval_extra /= self.value


class PhysicalCriticalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.physical_critical_strike_rate_extra += self.value[0]
        skill.physical_critical_power_rate_extra += self.value[1]

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.physical_critical_strike_rate_extra -= self.value[0]
        skill.physical_critical_power_rate_extra -= self.value[1]


class LunarCriticalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.lunar_critical_strike_rate_extra += self.value[0]
        skill.lunar_critical_power_rate_extra += self.value[1]

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.lunar_critical_strike_rate_extra -= self.value[0]
        skill.lunar_critical_power_rate_extra -= self.value[1]


class NeutralCriticalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.neutral_critical_strike_rate_extra += self.value[0]
        skill.neutral_critical_power_rate_extra += self.value[1]

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.neutral_critical_strike_rate_extra -= self.value[0]
        skill.neutral_critical_power_rate_extra -= self.value[1]


class PoisonCriticalStrikeRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.poison_critical_strike_rate_extra += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.poison_critical_strike_rate_extra -= self.value


class SolarLunarCriticalStrikeRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.solar_critical_strike_rate_extra += self.value
        skill.lunar_critical_strike_rate_extra += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.solar_critical_strike_rate_extra -= self.value
        skill.lunar_critical_strike_rate_extra -= self.value


class SolarLunarCriticalRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.solar_critical_strike_rate_extra += self.value[0]
        skill.lunar_critical_strike_rate_extra += self.value[0]
        skill.solar_critical_power_rate_extra += self.value[1]
        skill.lunar_critical_power_rate_extra += self.value[1]

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.solar_critical_strike_rate_extra -= self.value[0]
        skill.lunar_critical_strike_rate_extra -= self.value[0]
        skill.solar_critical_power_rate_extra -= self.value[1]
        skill.lunar_critical_power_rate_extra -= self.value[1]


class PhysicalShieldGainRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.physical_shield_gain_extra += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.physical_shield_gain_extra -= self.value


class PveAdditionRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.pve_addition_extra += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.pve_addition_extra -= self.value
