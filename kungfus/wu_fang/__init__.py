from kungfus.wu_fang.attribute import Attribute
from kungfus.wu_fang.buffs import BUFFS
from kungfus.wu_fang.dots import DOTS
from kungfus.wu_fang.gains import GAINS
from kungfus.wu_fang.recipes import RECIPE_CHOICES, RECIPES
from kungfus.wu_fang.skills import SKILLS
from kungfus.wu_fang.talents import TALENTS


def prepare(self, player_id):
    if 28419 in self.select_talents[player_id]:
        self.buff_stacks[player_id][30352][1] = 1
    if 28426 in self.select_talents[player_id]:
        self.buff_stacks[player_id][20699][1] = 1
