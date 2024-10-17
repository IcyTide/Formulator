from kungfus.bei_ao_jue.attribute import Attribute
from kungfus.bei_ao_jue.buffs import BUFFS
from kungfus.bei_ao_jue.dots import DOTS
from kungfus.bei_ao_jue.gains import GAINS
from kungfus.bei_ao_jue.recipes import RECIPE_CHOICES, RECIPES
from kungfus.bei_ao_jue.skills import SKILLS
from kungfus.bei_ao_jue.talents import TALENTS


def prepare(self, player_id):
    if 16728 in self.select_talents[player_id]:
        self.buff_stacks[player_id][-29478][1] = 1
