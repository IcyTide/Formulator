from schools.wen_shui_jue.attribute import Attribute
from schools.wen_shui_jue.buffs import BUFFS
from schools.wen_shui_jue.dots import DOTS
from schools.wen_shui_jue.gains import GAINS
from schools.wen_shui_jue.recipes import RECIPE_GAINS, RECIPES
from schools.wen_shui_jue.skills import SKILLS
from schools.wen_shui_jue.talents import TALENT_GAINS, TALENTS, TALENT_DECODER, TALENT_ENCODER


def prepare(self, player_id):
    self.buff_stacks[player_id][(-1, 1)] = 1
    if 5957 in self.select_talents[player_id]:
        self.buff_stacks[player_id][(12317, 1)] = 1
