from schools.zi_xia_gong.attribute import ZiXiaGong
from schools.zi_xia_gong.buffs import BUFFS
from schools.zi_xia_gong.gains import GAINS
from schools.zi_xia_gong.recipes import RECIPE_GAINS, RECIPES
from schools.zi_xia_gong.skills import SKILLS, DOTS
from schools.zi_xia_gong.talents import TALENT_GAINS, TALENTS, TALENT_DECODER, TALENT_ENCODER


def prepare(self, player_id):
    self.buff_stacks[player_id][(17918, 1)] = 1
