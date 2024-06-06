from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.zi_xia_gong.buffs import BUFFS

GAINS = {
    1914: CriticalSet(1439, BUFFS[1439]),
    818: DamageAdditionRecipe(102, 18640, 18640),
    4602: DamageAdditionRecipe(102, 18796, 18796),
    1520: DamageAdditionRecipe(51, 367, 367),
    1521: DamageAdditionRecipe(51, 306, 306),
    1136: CriticalStrikeRecipe(500, 0, 367),
    2418: Gain(),
    1931: Gain(),
    17300: Gain(),
    17312: Gain(),
    **EQUIPMENT_GAINS,
}
