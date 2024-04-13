from base.recipe import damage_addition_recipe
from general.gains.equipment import EQUIPMENT_GAINS, PhysicalCriticalSet
from base.gain import Gain

GAINS = {
    (22035, 1): Gain(),
    1925: PhysicalCriticalSet(0.8),
    4290: damage_addition_recipe([16610], 51),
    4291: damage_addition_recipe([16803, 16802, 16801, 16800, 17043, 19423, 19424, 32859], 51),
    4294: damage_addition_recipe([16610], 51),
    4295: damage_addition_recipe([16760, 16382], 51),
    2430: Gain(),
    1942: Gain(),
    **EQUIPMENT_GAINS,
}
