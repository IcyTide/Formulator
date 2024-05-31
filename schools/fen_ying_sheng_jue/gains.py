from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.fen_ying_sheng_jue.buffs import BUFFS

GAINS = {
    1922: CriticalSet(4671, BUFFS[4671].gain_attributes),
    948: damage_addition_recipe([4483 + i for i in range(8)] + [4476] + [26916], 102),
    1542: damage_addition_recipe([4480, 4482], 51),
    1543: damage_addition_recipe([4483 + i for i in range(8)] + [4476] + [26916], 51),
    1148: critical_strike_recipe([13468, 4202], 500),
    1149: critical_strike_recipe([3963], 500),
    2421: Gain(),
    1938: Gain(),
    17332: Gain(),
    17334: Gain(),
    **EQUIPMENT_GAINS,
}
