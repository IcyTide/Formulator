from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.tai_xu_jian_yi.buffs import BUFFS

GAINS = {
    (1915,): CriticalSet(1438, BUFFS[1438]),
    818: DamageAdditionRecipe(102, 365, 365),
    1522: DamageAdditionRecipe(51, 365, 365),
    1523: DamageAdditionRecipe(51, 2699, 2699),
    1135: CriticalStrikeRecipe(500, 365, 365),
    (2419,): Gain(),
    (1932,): Gain(),
    17301: DamageAdditionRecipe(21, 0, 0, 1),
    17313: CriticalStrikeRecipe(306, 0, 0, 3),
    **EQUIPMENT_GAINS,
}
