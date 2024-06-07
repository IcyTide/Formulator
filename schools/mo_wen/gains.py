from base.recipe import DamageAdditionRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.mo_wen.buffs import BUFFS

GAINS = {
    1924: CriticalSet(9586, BUFFS[9586]),
    2209: DamageAdditionRecipe(102, 14064, 14064),
    2210: DamageAdditionRecipe(102, 14067, 14067),
    2401: DamageAdditionRecipe(51, 14064, 14064),
    2402: DamageAdditionRecipe(51, 14068, 14068),
    2415: Gain(),
    1941: Gain(),
    17306: Gain(),
    17314: Gain(),
    **EQUIPMENT_GAINS,
}
