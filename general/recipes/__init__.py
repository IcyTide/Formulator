from base.recipe import SkillRecipe
from base.skill import Skill
from general.recipes import equipment

GENERAL_RECIPES = {
    **equipment.RECIPES
}


class CriticalStrikeRateRecipe(SkillRecipe):
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


class CriticalStrikeRateRecipe_200(CriticalStrikeRateRecipe):
    value = 200


class CriticalStrikeRateRecipe_300(CriticalStrikeRateRecipe):
    value = 300


class CriticalStrikeRateRecipe_400(CriticalStrikeRateRecipe):
    value = 400


class CriticalStrikeRateRecipe_500(CriticalStrikeRateRecipe):
    value = 500


class CriticalStrikeRateRecipe_306(CriticalStrikeRateRecipe):
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


class PhysicalShieldGainRecipe(SkillRecipe):
    def add_skill(self, skill: Skill):
        super().add_skill(skill)
        skill.physical_shield_gain_extra += self.value

    def sub_skill(self, skill: Skill):
        super().sub_skill(skill)
        skill.physical_shield_gain_extra -= self.value
