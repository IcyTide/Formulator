from kungfus.mo_wen.attribute import Attribute
from kungfus.mo_wen.buffs import BUFFS
from kungfus.mo_wen.dots import DOTS
from kungfus.mo_wen.gains import GAINS
from kungfus.mo_wen.recipes import RECIPE_CHOICES, RECIPES
from kungfus.mo_wen.skills import SKILLS
from kungfus.mo_wen.talents import TALENTS


def prepare(self, player_id):
    if 14350 in self.select_talents[player_id]:
        self.buff_stacks[player_id][9437][1] = 1
    if 18727 in self.select_talents[player_id]:
        self.buff_stacks[player_id][30464][1] = 1
