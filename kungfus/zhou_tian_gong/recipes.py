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


SCHOOL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        5610: {}, 5620: {}, 5636: {}, 5637: {}, 5638: {}, 5639: {},
    },
    CriticalStrikeRecipe_200: {
    },
    CriticalStrikeRecipe_300: {
    },
    CriticalStrikeRecipe_400: {
    },
    CriticalStrikeRecipe_500: {
    },
    CriticalStrikeRecipe_306: {
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
}
RECIPES: Dict[Tuple[int, int], Recipe] = {**GENERAL_RECIPES}
for recipe_class, recipes in SCHOOL_RECIPES.items():
    for recipe_key, attrs in recipes.items():
        if not isinstance(recipe_key, tuple):
            recipe_key = (recipe_key, 1)
        RECIPES[recipe_key] = recipe = recipe_class(*recipe_key)
        recipe.set_asset(attrs)
RECIPE_CHOICES: Dict[str, Dict[str, int]] = {
}
RECIPE_CHOICES: Dict[str, Dict[str, Tuple[int, int]]] = {
    skill: {
        desc: recipe_key if isinstance(recipe_key, tuple) else (recipe_key, 1)
        for desc, recipe_key in recipes.items()
    } for skill, recipes in RECIPE_CHOICES.items()
}
