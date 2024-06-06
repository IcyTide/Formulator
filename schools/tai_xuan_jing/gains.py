from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.tai_xuan_jing.buffs import BUFFS

GAINS = {
    1956: CriticalSet(18555, BUFFS[18555].attributes),
    5321: DamageAdditionRecipe(102, 24371, 24371),
    5322: DamageAdditionRecipe(102, 24372, 24372),
    5325: DamageAdditionRecipe(51, 24369, 24369),
    5326: DamageAdditionRecipe(51, 24371, 24371),
    5327: CriticalStrikeRecipe(500, 24371, 24371),
    2413: Gain(),
    1962: Gain(),
    17414: Gain(),
    17415: Gain(),
    **EQUIPMENT_GAINS,
}
