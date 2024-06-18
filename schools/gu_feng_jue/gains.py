from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.gu_feng_jue.buffs import BUFFS

GAINS = {
    1925: CriticalSet(11378, BUFFS[11378]),
    3188: DamageAdditionRecipe(102, 32145, 32145),
    3186: DamageAdditionRecipe(51, 32601, 32601),
    3187: DamageAdditionRecipe(51, 32145, 32145),
    3185: CriticalStrikeRecipe(500, 32601, 32601),
    2391: Gain(),
    2392: Gain(),
    17358: Gain(),
    17359: Gain(),
    **EQUIPMENT_GAINS,
}
