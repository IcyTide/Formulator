from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.shan_hai_xin_jue.buffs import BUFFS

GAINS = {
    (2568,): CriticalSet(16025, BUFFS[16025]),
    5438: DamageAdditionRecipe(102, 35661, 35661),
    5461: DamageAdditionRecipe(51, 36157, 36157),
    5462: DamageAdditionRecipe(51, 35661, 35661),
    5463: CriticalStrikeRecipe(500, 36157, 36157),
    (2572,): Gain(),
    (2571,): Gain(),
    17470: DamageAdditionRecipe(21, 0, 0, 1),
    17471: CriticalStrikeRecipe(306, 0, 0, 3),
    **EQUIPMENT_GAINS,
}
