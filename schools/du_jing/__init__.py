from schools.du_jing.attribute import Attribute
from schools.du_jing.buffs import BUFFS
from schools.du_jing.dots import DOTS
from schools.du_jing.gains import GAINS
from schools.du_jing.recipes import RECIPE_GAINS, RECIPES
from schools.du_jing.skills import SKILLS
from schools.du_jing.talents import TALENT_GAINS, TALENTS, TALENT_DECODER, TALENT_ENCODER


def prepare(self, player_id):
    if 6879 in self.select_talents[player_id]:
        self.buff_stacks[player_id][(12497, 1)] = 1
