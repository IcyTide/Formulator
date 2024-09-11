from kungfus.zi_xia_gong.attribute import Attribute
from kungfus.zi_xia_gong.buffs import BUFFS
from kungfus.zi_xia_gong.dots import DOTS
from kungfus.zi_xia_gong.gains import GAINS
from kungfus.zi_xia_gong.recipes import RECIPE_CHOICES, RECIPES
from kungfus.zi_xia_gong.skills import SKILLS
from kungfus.zi_xia_gong.talents import TALENTS


def prepare(self, player_id):
    self.buff_stacks[player_id][17918][1] = 1
