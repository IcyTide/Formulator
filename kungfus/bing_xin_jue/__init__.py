from kungfus.bing_xin_jue.attribute import Attribute
from kungfus.bing_xin_jue.buffs import BUFFS
from kungfus.bing_xin_jue.dots import DOTS
from kungfus.bing_xin_jue.gains import GAINS
from kungfus.bing_xin_jue.recipes import RECIPE_CHOICES, RECIPES
from kungfus.bing_xin_jue.skills import SKILLS
from kungfus.bing_xin_jue.talents import TALENTS


def prepare(self, player_id):
    if not self.players[player_id].platform:
        self.buff_stacks[player_id][409][21] = 10
    if 24996 in self.select_talents[player_id]:
        self.buff_stacks[player_id][17969][1] = 1
