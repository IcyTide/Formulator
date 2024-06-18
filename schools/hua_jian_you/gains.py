from base.gain import Gain
from base.recipe import ChannelIntervalRecipe, DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.hua_jian_you.buffs import BUFFS

GAINS = {
    1912: CriticalSet(1440, BUFFS[1440]),
    817: ChannelIntervalRecipe(1.15, 189, 189),
    1546: DamageAdditionRecipe(102, 2636, 2636),
    1516: DamageAdditionRecipe(51, 179, 179),
    1517: DamageAdditionRecipe(51, 2636, 2636),
    1131: CriticalStrikeRecipe(500, 179, 0),
    1979: CriticalStrikeRecipe(500, 2636, 2636),
    2417: Gain(),
    1929: Gain(),
    17399: Gain(),
    17400: Gain(),
    **EQUIPMENT_GAINS,
}
