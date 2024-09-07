from kungfus.tai_xuan_jing.attribute import Attribute
from kungfus.tai_xuan_jing.buffs import BUFFS
from kungfus.tai_xuan_jing.dots import DOTS
from kungfus.tai_xuan_jing.gains import GAINS
from kungfus.tai_xuan_jing.recipes import RECIPE_CHOICES, RECIPES
from kungfus.tai_xuan_jing.skills import SKILLS
from kungfus.tai_xuan_jing.talents import TALENT_CHOICES, TALENTS


def prepare(self, player_id):
    if 25072 in self.select_talents[player_id]:
        self.buff_stacks[player_id][18174][1] = 1
