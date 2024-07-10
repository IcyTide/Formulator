from schools.tai_xu_jian_yi.attribute import TaiXuJianYi
from schools.tai_xu_jian_yi.buffs import BUFFS
from schools.tai_xu_jian_yi.gains import GAINS
from schools.tai_xu_jian_yi.recipes import RECIPE_GAINS, RECIPES
from schools.tai_xu_jian_yi.skills import SKILLS, DOTS
from schools.tai_xu_jian_yi.talents import TALENT_GAINS, TALENTS, TALENT_DECODER, TALENT_ENCODER


def prepare(self, player_id):
    self.buff_stacks[player_id][(9949, 1)] = 3
