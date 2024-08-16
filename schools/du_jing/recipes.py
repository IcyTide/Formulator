from typing import Dict, List

from base.gain import Gain
from base.recipe import ChannelIntervalRecipe, DamageAdditionRecipe, CriticalStrikeRecipe
from base.skill import Skill


class 蝎心伤害提高(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id == 13476:
            skill.channel_interval_extra *= self.value[0]
        skill.damage_addition += self.value[1]

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 13476:
            skill.channel_interval_extra /= self.value[0]
        skill.damage_addition -= self.value[1]


RECIPE_GAINS: Dict[str, Dict[str, Gain]] = {
    "蝎心": {
        "4%伤害": 蝎心伤害提高((1.04, 41), 2209, 2209),
        "3%伤害": 蝎心伤害提高((1.03, 31), 2209, 2209),
        "3%会心": CriticalStrikeRecipe(300, 2209, 2209),
        "2%会心": CriticalStrikeRecipe(200, 2209, 2209),
    },
    "蛇影": {
        "5%伤害": ChannelIntervalRecipe(1.05, 2211, 2211),
        "4%伤害": ChannelIntervalRecipe(1.04, 2211, 2211),
        "4%会心": CriticalStrikeRecipe(400, 2211, 2211),
        "3%会心": CriticalStrikeRecipe(300, 2211, 2211),
        "2%会心": CriticalStrikeRecipe(200, 2211, 2211),
    },
    "百足": {
        "10%伤害": ChannelIntervalRecipe(1.1, 2212, 2212),
        "5%伤害": ChannelIntervalRecipe(1.05, 2212, 2212),
    },
    "灵蛊": {
        "10%伤害": DamageAdditionRecipe(102, 18584, 18584),
    },
}

RECIPES: Dict[str, List[str]] = {
    "蝎心": ["4%伤害", "3%伤害", "3%会心", "2%会心"],
    "蛇影": ["5%伤害", "4%伤害", "4%会心", "3%会心", "2%会心"],
    "百足": ["10%伤害", "10%伤害", "5%伤害"],
    "灵蛊": ["10%伤害", "10%伤害", "10%伤害"],
}
