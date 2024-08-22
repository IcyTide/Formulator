from schools.hua_jian_you.attribute import Attribute
from schools.hua_jian_you.buffs import BUFFS
from schools.hua_jian_you.dots import DOTS
from schools.hua_jian_you.gains import GAINS
from schools.hua_jian_you.recipes import RECIPE_CHOICES, RECIPES
from schools.hua_jian_you.skills import SKILLS
from schools.hua_jian_you.talents import TALENT_CHOICES, TALENTS


def prepare(self, player_id):
    if not self.players[player_id].platform:
        self.buff_stacks[player_id][14636][1] = 1
