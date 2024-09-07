from kungfus.ao_xue_zhan_yi.attribute import Attribute
from kungfus.ao_xue_zhan_yi.buffs import BUFFS
from kungfus.ao_xue_zhan_yi.dots import DOTS
from kungfus.ao_xue_zhan_yi.gains import GAINS
from kungfus.ao_xue_zhan_yi.recipes import RECIPE_CHOICES, RECIPES
from kungfus.ao_xue_zhan_yi.skills import SKILLS
from kungfus.ao_xue_zhan_yi.talents import TALENT_CHOICES, TALENTS


def prepare(self, player_id):
    self.buff_stacks[player_id][-1][1] = 5
