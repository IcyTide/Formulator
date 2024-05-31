from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.fen_shan_jing.buffs import BUFFS

GAINS = {
    1923: CriticalSet(1428, BUFFS[1428].gain_attributes),
    1932: damage_addition_recipe([13075], 102),
    1933: damage_addition_recipe([19409], 102),
    1937: damage_addition_recipe([13463], 51),
    1938: damage_addition_recipe([13092], 51),
    1934: critical_strike_recipe([13044], 500),
    1936: critical_strike_recipe([13092, 8249], 500),
    2408: Gain(),
    1940: Gain(),
    17447: Gain(),
    17448: Gain(),
    **EQUIPMENT_GAINS,
}
