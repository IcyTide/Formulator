from schools.fen_shan_jing.attribute import Attribute
from schools.fen_shan_jing.buffs import BUFFS
from schools.fen_shan_jing.dots import DOTS
from schools.fen_shan_jing.gains import GAINS
from schools.fen_shan_jing.recipes import RECIPE_CHOICES, RECIPES
from schools.fen_shan_jing.skills import SKILLS
from schools.fen_shan_jing.talents import TALENT_CHOICES, TALENTS, TALENT_DECODER, TALENT_ENCODER


def prepare(self, player_id):
    if 14838 in self.select_talents[player_id]:
        self.buff_stacks[player_id][-9889][1] = 1
