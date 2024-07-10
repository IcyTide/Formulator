from schools.tai_xuan_jing.attribute import TaiXuanJing
from schools.tai_xuan_jing.buffs import BUFFS
from schools.tai_xuan_jing.gains import GAINS
from schools.tai_xuan_jing.recipes import RECIPE_GAINS, RECIPES
from schools.tai_xuan_jing.skills import SKILLS, DOTS
from schools.tai_xuan_jing.talents import TALENT_GAINS, TALENTS, TALENT_DECODER, TALENT_ENCODER


def prepare(self, player_id):
    if 25072 in self.select_talents[player_id]:
        self.buff_stacks[player_id][(18174, 1)] = 1
