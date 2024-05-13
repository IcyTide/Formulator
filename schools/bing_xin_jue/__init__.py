from schools.bing_xin_jue.skills import SKILLS
from schools.bing_xin_jue.buffs import BUFFS
from schools.bing_xin_jue.talents import TALENT_GAINS, TALENTS, TALENT_DECODER, TALENT_ENCODER
from schools.bing_xin_jue.recipes import RECIPE_GAINS, RECIPES
from schools.bing_xin_jue.gains import GAINS
from schools.bing_xin_jue.attribute import BingXinJue


def prepare(self, player_id):
    self.buff_stacks[player_id][(409, 21)] = 10
    self.buff_stacks[player_id][(17969, 1)] = 1
