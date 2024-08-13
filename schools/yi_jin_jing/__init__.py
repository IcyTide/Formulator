from schools.yi_jin_jing.attribute import Attribute
from schools.yi_jin_jing.buffs import BUFFS
from schools.yi_jin_jing.dots import DOTS
from schools.yi_jin_jing.gains import GAINS
from schools.yi_jin_jing.recipes import RECIPE_GAINS, RECIPES
from schools.yi_jin_jing.skills import SKILLS
from schools.yi_jin_jing.talents import TALENT_GAINS, TALENTS, TALENT_DECODER, TALENT_ENCODER


def prepare(self, player_id):
    self.buff_stacks[player_id][(10023, 1)] = 1
