from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.bei_ao_jue.buffs import BUFFS

GAINS = {
    (1925,): CriticalSet(11378, BUFFS[11378]),
    4290: DamageAdditionRecipe(102, 16027, 16027),
    4291: DamageAdditionRecipe(102, 16627, 16627),
    4294: DamageAdditionRecipe(51, 16027, 16027),
    4295: DamageAdditionRecipe(51, 16601, 16601),
    4296: CriticalStrikeRecipe(500, 16601, 16601),
    4297: CriticalStrikeRecipe(500, 16085, 16085),
    (2430,): Gain(),
    (1942,): Gain(),
    17374: Gain(),
    17375: Gain(),
    **EQUIPMENT_GAINS,
}
