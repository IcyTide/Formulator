from schools.ao_xue_zhan_yi.attribute import AoXueZhanYi
from schools.ao_xue_zhan_yi.buffs import BUFFS
from schools.ao_xue_zhan_yi.gains import GAINS
from schools.ao_xue_zhan_yi.recipes import RECIPE_GAINS, RECIPES
from schools.ao_xue_zhan_yi.skills import SKILLS
from schools.ao_xue_zhan_yi.talents import TALENT_GAINS, TALENTS, TALENT_DECODER, TALENT_ENCODER


def prepare(self, player_id):
    self.buff_stacks[player_id][(-1, 1)] = 5
