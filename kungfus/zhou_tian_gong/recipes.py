from general.recipes import *


class 断脉双会提高10(NeutralCriticalRecipe):
    value = (1000, 102)

    def add_skill(self, skill: Skill):
        if skill.skill_id == 38084:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 38084:
            super().sub_skill(skill)


class 引窍增幅增加(SkillRecipe):
    channel_interval: list

    def add_skill(self, skill: Skill):
        if skill.skill_id == 38438:
            new_channel_interval = [1000 * (1 + 0.05 * level) for level in range(skill.max_level)]
            self.channel_interval, skill.channel_interval = skill.all_channel_interval, new_channel_interval

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 38438:
            skill.channel_interval = self.channel_interval


class 芒渺静止增伤(MoveStateDamageAdditionRecipe):
    value = 358


class 滃从递增雾刃飞光(ChannelIntervalRecipe):
    values = {
        5645: 1.2,
        5646: 1.2 ** 2,
        5647: 1.2 ** 3
    }

    @property
    def value(self):
        return self.values[self.recipe_id]


RECIPES: Dict[int, Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]]] = {
    0: {
        SkillRecipe: {
            5610: {}, 5620: {}, 5636: {}, 5637: {}, 5638: {}, 5639: {},
        },
        断脉双会提高10: {
            5578: {}
        },
        引窍增幅增加: {
            5617: {}
        },
        芒渺静止增伤: {
            5640: {}
        },
        滃从递增雾刃飞光: {
            5645: {}, 5646: {}, 5647: {}
        }
    },
    1: {}
}
RECIPE_CHOICES: Dict[int, Dict[str, Dict[str, int]]] = {
    0: {},
    1: {}
}
