from kungfus.tai_xu_jian_yi.attribute import Attribute
from kungfus.tai_xu_jian_yi.buffs import BUFFS
from kungfus.tai_xu_jian_yi.dots import DOTS
from kungfus.tai_xu_jian_yi.gains import GAINS
from kungfus.tai_xu_jian_yi.recipes import RECIPE_CHOICES, RECIPES
from kungfus.tai_xu_jian_yi.skills import SKILLS
from kungfus.tai_xu_jian_yi.talents import TALENTS


def prepare(self, player_id):
    if 14833 in self.select_talents[player_id]:
        self.buff_stacks[player_id][9949][1] = 3
