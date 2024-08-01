from schools.hua_jian_you.attribute import HuaJianYou
from schools.hua_jian_you.buffs import BUFFS
from schools.hua_jian_you.gains import GAINS
from schools.hua_jian_you.recipes import RECIPE_GAINS, RECIPES
from schools.hua_jian_you.skills import SKILLS, DOTS
from schools.hua_jian_you.talents import TALENT_GAINS, TALENTS, TALENT_DECODER, TALENT_ENCODER


def prepare(self, player_id):
    self.buff_stacks[player_id][(14636, 1)] = 1
