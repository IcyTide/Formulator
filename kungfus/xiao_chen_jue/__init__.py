from kungfus.xiao_chen_jue.attribute import Attribute
from kungfus.xiao_chen_jue.buffs import BUFFS
from kungfus.xiao_chen_jue.dots import DOTS
from kungfus.xiao_chen_jue.gains import GAINS
from kungfus.xiao_chen_jue.recipes import RECIPE_CHOICES, RECIPES
from kungfus.xiao_chen_jue.skills import SKILLS
from kungfus.xiao_chen_jue.talents import TALENTS


def prepare(self, player_id):
    self.buff_stacks[player_id][30400][1] = 1
    if 6832 in self.select_talents[player_id]:
        self.buff_stacks[player_id][5994][4] = 1
