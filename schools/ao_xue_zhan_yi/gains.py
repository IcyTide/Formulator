from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.ao_xue_zhan_yi.buffs import BUFFS

GAINS = {
    1913: CriticalSet(1428, BUFFS[1428].attributes),
    817: DamageAdditionRecipe(102, 415, 415),
    1508: DamageAdditionRecipe(51, 400, 400),
    1509: DamageAdditionRecipe(51, 403, 403),
    1133: CriticalStrikeRecipe(500, 415, 415),
    2424: Gain(),
    1933: Gain(),
    1942: Gain(),
    17362: Gain(),
    17367: Gain(),
    **EQUIPMENT_GAINS,
}
