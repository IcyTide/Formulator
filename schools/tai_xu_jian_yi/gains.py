from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.tai_xu_jian_yi.buffs import BUFFS

GAINS = {
    1915: CriticalSet(1438, BUFFS[1438].attributes),
    818: DamageAdditionRecipe(102, 365, 365),
    1522: DamageAdditionRecipe(51, 365, 365),
    1523: DamageAdditionRecipe(51, 2699, 2699),
    1135: CriticalStrikeRecipe(500, 365, 365),
    2419: Gain(),
    1932: Gain(),
    17301: Gain(),
    17313: Gain(),
    **EQUIPMENT_GAINS,
}
