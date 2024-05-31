from base.recipe import damage_addition_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.mo_wen.buffs import BUFFS

GAINS = {
    1924: CriticalSet(9586, BUFFS[9586].gain_attributes),
    2209: damage_addition_recipe([18860], 102),
    2210: damage_addition_recipe([14227, 18859], 102),
    2401: damage_addition_recipe([18860], 51),
    2402: damage_addition_recipe([14100], 51),
    2415: Gain(),
    1941: Gain(),
    17306: Gain(),
    17314: Gain(),
    **EQUIPMENT_GAINS,
}
