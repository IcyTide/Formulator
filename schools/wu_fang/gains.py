from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.wu_fang.buffs import BUFFS

GAINS = {
    (2125,): CriticalSet(21758, BUFFS[21758]),
    2839: DamageAdditionRecipe(102, 27556, 27556),
    2840: DamageAdditionRecipe(102, 27551, 27551),
    2842: DamageAdditionRecipe(51, 27556, 27556),
    2843: DamageAdditionRecipe(51, 27554, 27554),
    2841: CriticalStrikeRecipe(500, 27556, 27556),
    (2414,): Gain(),
    (2138,): Gain(),
    17458: DamageAdditionRecipe(21, 0, 0, 1),
    17459: CriticalStrikeRecipe(306, 0, 0, 3),
    **EQUIPMENT_GAINS,
}
