from kungfus.hua_jian_you.attribute import Attribute
from kungfus.hua_jian_you.buffs import BUFFS
from kungfus.hua_jian_you.dots import DOTS
from kungfus.hua_jian_you.gains import GAINS
from kungfus.hua_jian_you.recipes import RECIPE_CHOICES, RECIPES
from kungfus.hua_jian_you.skills import SKILLS
from kungfus.hua_jian_you.talents import TALENT_CHOICES, TALENTS


def prepare(self, player_id):
    if not self.players[player_id].platform:
        self.buff_stacks[player_id][14636][1] = 1
