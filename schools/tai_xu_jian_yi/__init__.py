from schools.tai_xu_jian_yi.attribute import Attribute
from schools.tai_xu_jian_yi.buffs import BUFFS
from schools.tai_xu_jian_yi.dots import DOTS
from schools.tai_xu_jian_yi.gains import GAINS
from schools.tai_xu_jian_yi.recipes import RECIPE_CHOICES, RECIPES
from schools.tai_xu_jian_yi.skills import SKILLS
from schools.tai_xu_jian_yi.talents import TALENT_CHOICES, TALENTS, TALENT_DECODER, TALENT_ENCODER


def prepare(self, player_id):
    if 14833 in self.select_talents[player_id]:
        self.buff_stacks[player_id][9949][1] = 3
