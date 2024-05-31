from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.bei_ao_jue.buffs import BUFFS

GAINS = {
    (22035, 1): Gain(),
    1925: CriticalSet(11378, BUFFS[11378].gain_attributes),
    4290: damage_addition_recipe([16610], 102),
    4291: damage_addition_recipe([16803, 16802, 16801, 16800, 17043, 19423, 19424, 32859], 102),
    4294: damage_addition_recipe([16610], 51),
    4295: damage_addition_recipe([16760, 16382], 51),
    4296: critical_strike_recipe([16760, 16382], 500),
    4297: Gain(),
    2430: Gain(),
    1942: Gain(),
    17374: Gain(),
    17375: Gain(),
    **EQUIPMENT_GAINS,
}
