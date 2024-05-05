from schools.bing_xin_jue.skills import SKILLS
from schools.bing_xin_jue.buffs import BUFFS
from schools.bing_xin_jue.talents import TALENT_GAINS, TALENTS, TALENT_DECODER, TALENT_ENCODER
from schools.bing_xin_jue.recipes import RECIPE_GAINS, RECIPES
from schools.bing_xin_jue.gains import GAINS
from schools.bing_xin_jue.attribute import WuFang


def prepare(self, player_id):
    self.status_buffer[player_id][(409, 1)] = (10, self.current_frame)
    self.status_buffer[player_id][(17969, 1)] = (1, self.current_frame)
