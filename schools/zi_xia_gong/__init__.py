from schools.zi_xia_gong.attribute import Attribute
from schools.zi_xia_gong.buffs import BUFFS
from schools.zi_xia_gong.dots import DOTS
from schools.zi_xia_gong.gains import GAINS
from schools.zi_xia_gong.recipes import RECIPE_CHOICES, RECIPES
from schools.zi_xia_gong.skills import SKILLS
from schools.zi_xia_gong.talents import TALENT_CHOICES, TALENTS


def prepare(self, player_id):
    self.buff_stacks[player_id][17918][1] = 1
