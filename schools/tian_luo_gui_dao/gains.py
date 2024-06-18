from base.gain import Gain
from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.tian_luo_gui_dao.buffs import BUFFS

GAINS = {
    1918: CriticalSet(3401, BUFFS[3401]),
    947: DamageAdditionRecipe(205, 3108, 3108),
    4120: DamageAdditionRecipe(102, 3093, 3093),
    1532: DamageAdditionRecipe(51, 3105, 3105),
    1533: DamageAdditionRecipe(51, 3108, 3108),
    1146: CriticalStrikeRecipe(500, 3105, 0),
    1978: CriticalStrikeRecipe(500, 3093, 3093),
    2412: Gain(),
    1935: Gain(),
    17429: Gain(),
    17430: Gain(),
    **EQUIPMENT_GAINS,
}
