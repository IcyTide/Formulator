from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.ling_hai_jue.buffs import BUFFS

GAINS = {
    (1926,): CriticalSet(14353, BUFFS[14353]),
    4816: DamageAdditionRecipe(102, 20259, 20259),
    4817: DamageAdditionRecipe(102, 20715, 20715),
    4818: DamageAdditionRecipe(51, 19818, 19818),
    4819: DamageAdditionRecipe(51, 19827, 19827),
    4820: CriticalStrikeRecipe(500, 19818, 19818),
    4821: CriticalStrikeRecipe(500, 20715, 20715),
    (2423,): Gain(),
    (1943,): Gain(),
    17409: Gain(),
    17410: Gain(),
    **EQUIPMENT_GAINS,
}
