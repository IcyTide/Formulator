from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.fen_shan_jing.buffs import BUFFS

GAINS = {
    1923: CriticalSet(1428, BUFFS[1428]),
    1932: DamageAdditionRecipe(102, 13055, 13055),
    1933: DamageAdditionRecipe(102, 13045, 13045),
    1937: DamageAdditionRecipe(51, 13050, 13050),
    1938: DamageAdditionRecipe(51, 13054, 13054),
    1934: CriticalStrikeRecipe(500, 13044, 13044),
    1936: CriticalStrikeRecipe(500, 13054, 13054),
    2408: Gain(),
    1940: Gain(),
    17447: Gain(),
    17448: Gain(),
    **EQUIPMENT_GAINS,
}
