from kungfus.yi_jin_jing.attribute import Attribute
from kungfus.yi_jin_jing.buffs import BUFFS
from kungfus.yi_jin_jing.dots import DOTS
from kungfus.yi_jin_jing.gains import GAINS
from kungfus.yi_jin_jing.recipes import RECIPE_CHOICES, RECIPES
from kungfus.yi_jin_jing.skills import SKILLS
from kungfus.yi_jin_jing.talents import TALENT_CHOICES, TALENTS


def prepare(self, player_id):
    self.buff_stacks[player_id][10023][1] = 1
