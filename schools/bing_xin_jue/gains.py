from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.bing_xin_jue.buffs import BUFFS

GAINS = {
    1916: CriticalSet(1437, BUFFS[1437]),
    1547: DamageAdditionRecipe(102, 2707, 2707),
    1524: DamageAdditionRecipe(51, 2707, 2707),
    1525: DamageAdditionRecipe(51, 553, 553),
    1137: CriticalStrikeRecipe(500, 561, 561),
    1977: CriticalStrikeRecipe(500, 2716, 2716),
    2416: Gain(),
    1930: Gain(),
    17380: Gain(),
    17381: Gain(),
    **EQUIPMENT_GAINS,
}
