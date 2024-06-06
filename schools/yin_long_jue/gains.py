from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.yin_long_jue.buffs import BUFFS

GAINS = {
    (36726, 1): Gain(),
    1927: CriticalSet(16025, BUFFS[16025].attributes),
    5037: DamageAdditionRecipe(102, 22327, 22327),
    5038: DamageAdditionRecipe(102, 22144, 22144),
    5091: DamageAdditionRecipe(51, 22143, 22143),
    5092: DamageAdditionRecipe(51, 22327, 22327),
    5093: CriticalStrikeRecipe(500, 22327, 22327),
    17348: Gain(),
    2428: Gain(),
    1944: Gain(),
    17324: Gain(),
    17330: Gain(),
    **EQUIPMENT_GAINS,
}
