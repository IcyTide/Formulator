from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain

GAINS = {
    1956: CriticalSet(18555),
    5321: damage_addition_recipe([24813, 24811, 24812, 24814], 102),
    5322: damage_addition_recipe([24823, 24821, 24822, 24824, 34683], 102),
    5325: damage_addition_recipe([24676, 24558, 24675, 24677], 51),
    5326: damage_addition_recipe([24813, 24811, 24812, 24814], 51),
    5327: critical_strike_recipe([24813, 24811, 24812, 24814], 500),
    2413: Gain(),
    1962: Gain(),
    17414: Gain(),
    17415: Gain(),
    **EQUIPMENT_GAINS,
}
