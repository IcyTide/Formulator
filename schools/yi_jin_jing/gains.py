from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.yi_jin_jing.buffs import BUFFS

GAINS = {
    1911: CriticalSet(1436, BUFFS[1436]),
    818: DamageAdditionRecipe(102, 233, 233),
    1147: DamageAdditionRecipe(102, 243, 243),
    1512: DamageAdditionRecipe(51, 232, 0),
    1513: DamageAdditionRecipe(51, 2572, 2572),
    1139: CriticalStrikeRecipe(500, 233, 233),
    2410: Gain(),
    1928: Gain(),
    17351: Gain(),
    17352: Gain(),
    **EQUIPMENT_GAINS,
}
