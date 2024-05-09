from schools.zi_xia_gong.skills import SKILLS
from schools.zi_xia_gong.buffs import BUFFS
from schools.zi_xia_gong.talents import TALENT_GAINS, TALENTS, TALENT_DECODER, TALENT_ENCODER
from schools.zi_xia_gong.recipes import RECIPE_GAINS, RECIPES
from schools.zi_xia_gong.gains import GAINS
from schools.zi_xia_gong.attribute import ZiXiaGong


def prepare(self, player_id):
    self.player_buffs[player_id][(17918, 1)] = 1
