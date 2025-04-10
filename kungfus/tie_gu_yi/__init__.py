from kungfus.tie_gu_yi.attribute import Attribute
from kungfus.tie_gu_yi.buffs import BUFFS
from kungfus.tie_gu_yi.dots import DOTS
from kungfus.tie_gu_yi.gains import GAINS
from kungfus.tie_gu_yi.recipes import RECIPE_CHOICES, RECIPES
from kungfus.tie_gu_yi.skills import SKILLS
from kungfus.tie_gu_yi.talents import TALENTS


def prepare(self, player_id):
    if 39045 in self.select_talents[player_id]:
        self.buff_stacks[player_id][-9889][1] = 1
