from kungfus.wen_shui_jue.attribute import Attribute
from kungfus.wen_shui_jue.buffs import BUFFS
from kungfus.wen_shui_jue.dots import DOTS
from kungfus.wen_shui_jue.gains import GAINS
from kungfus.wen_shui_jue.recipes import RECIPE_CHOICES, RECIPES
from kungfus.wen_shui_jue.skills import SKILLS
from kungfus.wen_shui_jue.talents import TALENT_CHOICES, TALENTS


def prepare(self, player_id):
    self.buff_stacks[player_id][-1][1] = 1
    if 5957 in self.select_talents[player_id]:
        self.buff_stacks[player_id][12317][1] = 1
