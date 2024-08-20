from schools.tian_luo_gui_dao.attribute import Attribute
from schools.tian_luo_gui_dao.buffs import BUFFS
from schools.tian_luo_gui_dao.dots import DOTS
from schools.tian_luo_gui_dao.gains import GAINS
from schools.tian_luo_gui_dao.recipes import RECIPE_CHOICES, RECIPES
from schools.tian_luo_gui_dao.skills import SKILLS
from schools.tian_luo_gui_dao.talents import TALENT_CHOICES, TALENTS, TALENT_DECODER, TALENT_ENCODER


def prepare(self, player_id):
    if 14857 in self.select_talents[player_id]:
        self.buff_stacks[player_id][13165][1] = 1
        self.buff_stacks[player_id][27405][1] = 1
    if 37326 in self.select_talents[player_id]:
        self.buff_stacks[player_id][28228][1] = 3
    if 6506 in self.select_talents[player_id]:
        self.buff_stacks[player_id][6112][1] = 1
