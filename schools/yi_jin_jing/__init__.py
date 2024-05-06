from schools.yi_jin_jing.skills import SKILLS
from schools.yi_jin_jing.buffs import BUFFS
from schools.yi_jin_jing.talents import TALENT_GAINS, TALENTS, TALENT_DECODER, TALENT_ENCODER
from schools.yi_jin_jing.recipes import RECIPE_GAINS, RECIPES
from schools.yi_jin_jing.gains import GAINS
from schools.yi_jin_jing.attribute import YiJinJing


def prepare(self, player_id):
    self.status[player_id][(10023, 1)] = 1
