from schools.ao_xue_zhan_yi.attribute import Attribute
from schools.ao_xue_zhan_yi.buffs import BUFFS
from schools.ao_xue_zhan_yi.dots import DOTS
from schools.ao_xue_zhan_yi.gains import GAINS
from schools.ao_xue_zhan_yi.recipes import RECIPE_CHOICES, RECIPES
from schools.ao_xue_zhan_yi.skills import SKILLS
from schools.ao_xue_zhan_yi.talents import TALENT_CHOICES, TALENTS, TALENT_DECODER, TALENT_ENCODER


def prepare(self, player_id):
    self.buff_stacks[player_id][-1][1] = 5
