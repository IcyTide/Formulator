from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.jing_yu_jue.buffs import BUFFS

GAINS = {
    (1919,): CriticalSet(3401, BUFFS[3401]),
    946: DamageAdditionRecipe(102, 3095, 3095),
    1969: DamageAdditionRecipe(102, 0, 3093),
    1534: DamageAdditionRecipe(51, 3095, 3095),
    1535: DamageAdditionRecipe(51, 3093, 3093),
    1145: CriticalStrikeRecipe(500, 3095, 0),
    1978: CriticalStrikeRecipe(500, 3093, 3093),
    (2411,): Gain(),
    (1936,): Gain(),
    17435: Gain(),
    17436: Gain(),
    **EQUIPMENT_GAINS,
}
