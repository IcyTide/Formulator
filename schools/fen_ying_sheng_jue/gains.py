from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.fen_ying_sheng_jue.buffs import BUFFS

GAINS = {
    1922: CriticalSet(4671, BUFFS[4671]),
    948: DamageAdditionRecipe(102, 0, 3967),
    1542: DamageAdditionRecipe(51, 3979, 3979),
    1543: DamageAdditionRecipe(51, 3967, 3967),
    1148: CriticalStrikeRecipe(500, 3960, 3960),
    1149: CriticalStrikeRecipe(500, 3963, 3963),
    2421: Gain(),
    1938: Gain(),
    17332: Gain(),
    17334: Gain(),
    **EQUIPMENT_GAINS,
}
