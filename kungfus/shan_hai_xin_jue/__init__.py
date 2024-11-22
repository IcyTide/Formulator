from kungfus.shan_hai_xin_jue.attribute import Attribute
from kungfus.shan_hai_xin_jue.buffs import BUFFS
from kungfus.shan_hai_xin_jue.dots import DOTS
from kungfus.shan_hai_xin_jue.gains import GAINS
from kungfus.shan_hai_xin_jue.recipes import RECIPE_CHOICES, RECIPES
from kungfus.shan_hai_xin_jue.skills import SKILLS
from kungfus.shan_hai_xin_jue.talents import TALENTS


def prepare(self, player_id):
    if not self.players[player_id].platform:
        self.buff_stacks[player_id][26857][1] = 5
    if 35733 in self.select_talents[player_id]:
        self.buff_stacks[player_id][27099][1] = 1
