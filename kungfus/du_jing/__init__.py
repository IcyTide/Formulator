from kungfus.du_jing.attribute import Attribute
from kungfus.du_jing.buffs import BUFFS
from kungfus.du_jing.dots import DOTS
from kungfus.du_jing.gains import GAINS
from kungfus.du_jing.recipes import RECIPE_CHOICES, RECIPES
from kungfus.du_jing.skills import SKILLS
from kungfus.du_jing.talents import TALENT_CHOICES, TALENTS


def prepare(self, player_id):
    if 6879 in self.select_talents[player_id]:
        self.buff_stacks[player_id][12497][1] = 1
